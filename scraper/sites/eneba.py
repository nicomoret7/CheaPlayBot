import requests
from bs4 import BeautifulSoup
from .funcs import parse_price, load_selenium


def scrapEneba(name):

    page = requests.get("https://www.eneba.com/store/steam-games?page=1&platforms[]=STEAM&regions[]=europe&regions["
                        "]=global&sortBy=PRICE_ASC&text=%s&types[]=game" % name)
    parser = BeautifulSoup(page.text, features="lxml")

    # name = ''

    '''
    try:
        file = open("eneba_log.html", "w")
        file.write(parser.text)
        file.close()
    except IOError:
        print("I/O Error")
    '''

    try:
        price = parser.find('span', attrs={'class': 'DTv7Ag'}).find('span', attrs={'class': 'L5ErLT'}).text
        price = parse_price(price)
        # name = parser.find('span', attrs={'class': 'YLosEL'}).text
    except AttributeError:
        price = "Not found"

    return price
