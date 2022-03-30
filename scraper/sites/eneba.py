import logging
import requests
from bs4 import BeautifulSoup
from .funcs import parse_price, load_selenium


def scrapEneba(name):

    page = requests.get("https://www.eneba.com/store/steam-games?page=1&platforms[]=STEAM&regions[]=europe&regions["
                        "]=global&sortBy=POPULARITY_DESC&text=%s&types[]=game" % name)
    parser = BeautifulSoup(page.text, features="lxml")

    # name = ''

    '''
    try:
        file = open("eneba.html", "w")
        file.write(parser.text)
        file.close()
    except IOError as e:
        logging.error("I/O Error", exc_info=True)
    '''

    try:
        price = parser.find('span', attrs={'class': 'DTv7Ag'}).find('span', attrs={'class': 'L5ErLT'}).text
        price = parse_price(price)
        # name = parser.find('span', attrs={'class': 'YLosEL'}).text
    except AttributeError:
        logging.error("%s couldn't find a price" % scrapEneba.__name__)
        price = "Not found"

    return price
