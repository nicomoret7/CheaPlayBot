import logging
from bs4 import BeautifulSoup
from .funcs import parse_price, load_selenium


def scrapHB(name, driver):

    driver.get("https://www.humblebundle.com/store/search?sort=bestselling&search=%s&drm=steam" % name)
    parser = BeautifulSoup(driver.page_source, features="lxml")

    try:
        price = parser.find('span', attrs={'class': 'price'}).text
        price = parse_price(price)
    except AttributeError:
        logging.error("%s couldn't find a price" % scrapHB.__name__)
        price = "Not found"

    return price
