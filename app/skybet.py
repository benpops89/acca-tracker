"""
Scrape data with selenium
"""

import sys
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import re

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests

class SkyBet:
    """
    Login to SkyBet and extract the bet data
    """

    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.login_url = 'https://www.skybet.com/secure/identity/m/login/skybet'
        self.bet_url = 'https://www.skybet.com/secure/identity/m/history/betting'

        self.create()
        self.session = self.login()

    def create(self):
        """ Create the driver """
        
        self.driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )

        return self

    def destroy(self):
        """ Close the driver """
        self.driver.quit()

        return self
    
    def login(self):
        """ Login to SkyBet """
        
        self.driver.get(self.login_url)
        form = self.driver.find_element_by_xpath('//form')
        username = form.find_element_by_id('username')
        pin = form.find_element_by_id('pin')
        
        username.send_keys(self.username)
        pin.send_keys(self.pin)
        form.submit()

        session = requests.Session()
        for cookie in self.driver.get_cookies():
            session.cookies.set(cookie['name'], cookie['value'])

        return session

    def get_query_string(self, period):
        """ Create the data query string for post request """

        date = datetime.strptime(period, '%Y-%m')
        date_dict = {
            'fromDate': date.strftime('%Y-%m-%d %H:%M:%S'),
            'toDate': (date + relativedelta(months=1) - timedelta(seconds=1)).strftime('%Y-%m-%d %H:%M:%S')
        }

        params = {
            'settled': 'Y',
            'pageNumber': 0,
            'pageSize': 20,
            **date_dict
        }

        return params
    
    def run(self, period=None):
        """ Get the bets """
        
        if period is not None:
            params = self.get_query_string(period)
        else:
            params = {'settled': 'N'}
        
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest'
        }

        res = self.session.post(
            self.bet_url,
            params=params,
            headers=headers
        )

        nfl_accas = res.json()['children']['body'][0]['children']['transactions-list'][0]['data']['transactions']
        self.destroy()

        if not nfl_accas:
            print('No accas available')

        re_handicap = re.compile(r'\((.*)\)')
        accas = []
        for acca in nfl_accas:
            bets = []
            if 'Accumulator' in acca['type']:
                bet_id = acca['betId']
                for bet in acca['bet']['group'][0]['selections']:
                    bet_type = bet['marketType']
                    if bet_type == 'Handicap':
                        spread = float(re_handicap.search(
                            bet['handicap']
                        ).group(1))
                    else:
                        spread = 0.0
                    
                    bets.append({
                        'type': bet_type,
                        'teams': bet['event'],
                        'selection': bet['selection'],
                        'spread': spread
                    })
                accas.append({
                    'id': bet_id,
                    'bets': bets
                })

        return accas

if __name__ == '__main__':
    import json
    skybet = SkyBet('<username>', '<password>')
    bets = skybet.run('2018-10')
    
    with open(r'skybet\bets.json', 'w') as f:
        json.dump(bets, f)
