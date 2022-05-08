import django
from corporative_net.models import Prices
import requests
from bs4 import BeautifulSoup


def get_and_write_all_prices():
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

    add_prices = Prices(
    crypt_one='BTC', price_one=prices[0], crypt_two='ETH', price_two=prices[1])
    add_prices.save()

    return ('BTC', prices[0], 'ETH', prices[1])
