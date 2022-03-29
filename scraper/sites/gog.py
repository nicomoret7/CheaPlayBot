import requests
from bs4 import BeautifulSoup
from .funcs import parse_price


def scrapGOG(name):

    page = requests.get("https://www.gog.com/en/games?query=%s&order=desc:score" % name)
    parser = BeautifulSoup(page.text, features="lxml")

    try:
        price = parser.find('span', attrs={'class': 'product-tile__price--final'}).text
        price = parse_price(price)
    except AttributeError:
        price = "Not found"

    return price
