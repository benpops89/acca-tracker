import getpass
import requests
import time
import uuid
from db import connect

@connect
def skybet(driver, period):
    username = input('Username: ')
    pin = getpass.getpass('Pin: ')

    job_id = requests.post(
        'http://127.0.0.1:5000/bets',
        json={
            'username': username,
            'pin': pin,
            'period': period
        }
    ).text

    while True:
        bets = requests.get(
            f'http://127.0.0.1:5000/results/{job_id}'
        )
        if bets.text == 'Nay!':
            time.sleep(2)
            continue

        accas = []
        for bet in bets.json():
            bet_list = []
            acca_id = str(uuid.uuid4())
            for game in bet['bets']:
                print(
                    '{home_team} v {visitor_team} -> {selection} ({spread})'.format(
                        **game
                    )
                )

                bet_list.append({
                    **game
                })

            name = input('Bet Name: ')
            accas.append({
                'bets': bet_list,
                'id': acca_id,
                'username': username,
                'name': name
            })
            print('\n')

        break

    with driver.session() as session:
        session.run(
            """
            UNWIND $accas AS acca
            MERGE (user:User {username: acca.username})
            CREATE (a:Acca {id: acca.id, name: acca.name})
            CREATE (a)-[:HAS_USER]->(user)
            WITH a, acca.bets as bets
            UNWIND bets AS bet
            MATCH (team:Team {display_name: bet.selection})
            MATCH (game:Game {date: datetime(bet.game_time)})-[:HOME_TEAM]->(home:Team {display_name: bet.home_team})
            CREATE (b:Bet {spread: bet.spread})
            CREATE (a)-[:HAS_BET]->(b)
            CREATE (b)-[:BET_ON]->(team)
            CREATE (b)-[:BET_PLACED]->(game)
            RETURN game, b
            """,
            accas=accas
        )

if __name__ == '__main__':
    skybet('2019-10')
