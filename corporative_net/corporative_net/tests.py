import requests
from django.test import TestCase
from bs4 import BeautifulSoup

from .buisneslogic.parser import _get_prices

# Create your tests here.

class ParserTestCase(TestCase):
    def setUp(self):
        print('Test starts')
        prices = []
        get_btc = requests.get('https://www.google.com/finance/quote/BTC-USD')
        get_eth = requests.get('https://www.google.com/finance/quote/ETH-USD')
        eth_soup = BeautifulSoup(get_eth.text, 'html.parser')
        btc_soup = BeautifulSoup(get_btc.text, 'html.parser')
        find_eth = eth_soup.findAll('div', class_='kf1m0')
        find_btc = btc_soup.findAll('div', class_='kf1m0')
            
        for data in find_btc:
            prices.append(float(data.find('div', 'fxKbKc').text.replace(',', '')))

        for data in find_eth:
            prices.append(float(data.find('div', 'fxKbKc').text.replace(',', '')))

        self.result = (prices[0], prices[1])

    def parsers_test(self):
         self.assertEqual(_get_prices(), self.result)