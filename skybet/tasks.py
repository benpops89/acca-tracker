"""
List of the tasks
"""

from skybet import SkyBet

def get_bets(username, pin, period=None):
    skybet = SkyBet(username, pin)
    bets = skybet.run(period)

    return bets
    