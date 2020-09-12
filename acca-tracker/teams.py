import requests
from db import connect

@connect
def teams(driver):
    """ Get a list of NFL teams  """

    url = 'http://site.api.espn.com/apis/site/v2/sports/football/nfl/teams'
    res = requests.get(
        url,
        params={'limit': 32}
    )

    teams = res.json()['sports'][0]['leagues'][0]['teams']
    team_list = []
    for team in teams:
        team_list.append({
            'id': team['team']['id'],
            'location': team['team']['location'],
            'name': team['team'].get('name', ''),
            'display_name': team['team']['displayName'],
            'abbreviation': team['team']['abbreviation']
        })

    with driver.session() as session:
        session.run(
            """
            UNWIND $team as team
            CREATE (t:Team)
            SET t = team
            RETURN t
            """,
            team=team_list
        )

if __name__ == '__main__':
    teams()
