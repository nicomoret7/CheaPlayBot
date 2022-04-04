import logging
from bs4 import BeautifulSoup
from .funcs import parse_price


def scrapIG(name, driver):

    driver.get("https://www.instant-gaming.com/en/search/?platform[]=&type[]=steam&query=%s" % name)
    parser = BeautifulSoup(driver.page_source, features="lxml")

    try:
        listing = parser.find(attrs={'class': 'listing-games'})
        price = listing.find('div', attrs={'class': 'price'}).text
        price = parse_price(price)
    except AttributeError:
        logging.error("%s couldn't find a price" % scrapIG.__name__)
        price = "Not found"

    return price
