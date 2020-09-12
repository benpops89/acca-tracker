import requests
import arrow
from espn import espn
from db import connect
import time

@connect
def games(driver):
    """ Extract the games for the current week  """

    game_list = espn()
    with driver.session() as session:
        session.run(
            """
            UNWIND $game AS game
            MATCH (g:Game {id: game.id})
            SET g.home_score = game.home_score, g.visitor_score = game.visitor_score, g.quarter = game.quarter
            RETURN g
            """,
            game=game_list
        )

if __name__ == '__main__':
    while True:
        print('Updating games...')
        games()
        time.sleep(30)
