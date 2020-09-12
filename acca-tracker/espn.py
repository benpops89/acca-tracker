import requests
import arrow

def espn():
    """ Extract the games for the current week  """

    url = 'http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard'

    res = requests.get(
        url
    )
    games = res.json()
    week = games['week']['number']
    year = games['season']['year']
    game_list = []
    for game in games['events']:
        game_list.append({
            'id': game['id'],
            'date': arrow.get(game['date']).to('local').isoformat()[:-6],
            'home_id': game['competitions'][0]['competitors'][0]['id'],
            'home_score': int(game['competitions'][0]['competitors'][0]['score']),
            'visitor_id': game['competitions'][0]['competitors'][1]['id'],
            'visitor_score': int(game['competitions'][0]['competitors'][1]['score']),
            'quarter': game['competitions'][0]['status']['period'],
            'week': week,
            'year': year
        })

    return game_list

if __name__ == '__main__':
    espn()
