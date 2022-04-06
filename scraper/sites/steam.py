import logging
import requests
from bs4 import BeautifulSoup
from .funcs import parse_price


def scrapSteam(name):

    page = requests.get("https://store.steampowered.com/search/?term=%s" % name)
    parser = BeautifulSoup(page.text, features="lxml")

    # name = ''

    '''
    try:
        file = open("steam.html", "w")
        file.write(parser.text)
        file.close()
    except IOError as e:
        logging.error("I/O Error", exc_info=True)
    '''

    try:
        price = parser.find('div', attrs={'class': 'search_price'}).contents[-1].text
        price = parse_price(price)
        # name = parser.find('span', attrs={'class': 'YLosEL'}).text
    except AttributeError:
        logging.error("%s couldn't find a price" % scrapSteam.__name__)
        price = "Not found"

    return price
