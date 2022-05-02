from webbrowser import get
import requests

from bs4 import BeautifulSoup

def get_all_prices():
    prices = []
    get_btc = requests.get('https://www.google.com/finance/quote/BTC-USD')
    get_eth = requests.get('https://www.google.com/finance/quote/ETH-USD')
    eth_soup = BeautifulSoup(get_eth.text, 'html.parser')
    btc_soup = BeautifulSoup(get_btc.text, 'html.parser')
    find_eth = eth_soup.findAll('div', class_='kf1m0')
    find_btc = btc_soup.findAll('div', class_='kf1m0')
        
    for data in find_btc:
        prices.append(data.find('div', 'fxKbKc').text)

    for data in find_eth:
        prices.append(data.find('div', 'fxKbKc').text)


    return {'BTC': prices[0] + '$', 'ETH': prices[1] + '$'}

print(get_all_prices())
