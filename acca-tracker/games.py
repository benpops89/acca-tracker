import requests
import arrow
from espn import espn
from db import connect

@connect
def games(driver):
    """ Extract the games for the current week  """

    game_list = espn()
    with driver.session() as session:
        session.run(
            """
            UNWIND $game AS game
            MERGE (w:Week {week: game.week, year: game.year})
            WITH w, game
            MATCH (home:Team {id: game.home_id})
            MATCH (visitor:Team {id: game.visitor_id})
            CREATE (g: Game {
                id: game.id,
                date: datetime(game.date),
                home_score: game.home_score,
                visitor_score: game.visitor_score,
                quarter: game.quarter
            })
            CREATE (g)-[:HOME_TEAM]->(home)
            CREATE (g)-[:VISITOR_TEAM]->(visitor)
            CREATE (g)<-[:HAS_GAME]-(w)
            RETURN g
            """,
            game=game_list
        )

if __name__ == '__main__':
    games()
