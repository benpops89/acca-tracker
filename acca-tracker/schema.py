from __future__ import annotations
import typing
from datetime import datetime
import strawberry
from db import connect

@strawberry.type
class Game:
    id: str
    home: str
    home_score: int
    visitor_score: int
    visitor: str
    quarter: int
    date: datetime

@strawberry.type
class Acca:
    id: str
    user: User
    name: str
    bets: typing.List[Bet]

@strawberry.type
class User:
    username: str

@strawberry.type
class Bet:
    spread: float
    bet_on: str
    home_bet: bool
    net_score: int
    game_id: str

@connect
def get_accas(driver, week, year):
    """ Get a list of accas from neo4j  """

    with driver.session() as session:
        data = session.run(
            """
            MATCH (w:Week {week: $week, year: $year})
            MATCH (w)-[:HAS_GAME]->(g:Game)
            MATCH (h:Team)<-[:HOME_TEAM]-(g)
            MATCH (g)<-[:BET_PLACED]-(b:Bet)<-[:HAS_BET]-(a:Acca)
            MATCH (a)-[:HAS_USER]->(u:User)
            MATCH (b)-[:BET_ON]->(t:Team)
            WITH a, u, {
                spread: b.spread,
                bet_on: t.abbreviation,
                home_bet: t.abbreviation = h.abbreviation,
                net_score: toInteger(g.home_score) - toInteger(g.visitor_score),
                game_id: g.id
            } as bet
            RETURN a, u, COLLECT(bet) AS bets
            """,
            week=week,
            year=year
        ).data()

    return [
        Acca(
            **x['a'],
            user=User(**x['u']),
            bets=[Bet(**b) for b in x['bets']]
        ) for x in data
    ]

@connect
def get_games(driver, week, year):
    """ Get a list of games from neo4j  """

    with driver.session() as session:
        data = session.run(
            """
            MATCH (w:Week {week: $week, year: $year})
            MATCH (w)-[:HAS_GAME]->(g:Game)
            MATCH (h:Team)<-[:HOME_TEAM]-(g)-[:VISITOR_TEAM]->(v:Team)
            RETURN g, h, v
            """,
            week=week,
            year=year
        ).data()

    return [
        Game(
            **x['g'],
            home=x['h']['abbreviation'],
            visitor=x['v']['abbreviation']
        ) for x in data
    ]

@strawberry.type
class Query:
    @strawberry.field
    def games(self, week: int, year: int) -> typing.List[Game]:
        return get_games(week, year)
    @strawberry.field
    def accas(self, week: int, year: int) -> typing.List[Acca]:
        return get_accas(week, year)

schema = strawberry.Schema(
    query=Query
)
