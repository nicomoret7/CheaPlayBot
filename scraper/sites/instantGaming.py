import logging
from bs4 import BeautifulSoup
from .funcs import parse_price, load_selenium


def scrapIG(name):

    driver = load_selenium()
    driver.get("https://www.instant-gaming.com/en/search/?platform[]=&type[]=steam&query=%s" % name)
    parser = BeautifulSoup(driver.page_source, features="lxml")
    driver.quit()

    try:
        listing = parser.find(attrs={'class': 'listing-games'})
        price = listing.find('div', attrs={'class': 'price'}).text
        price = parse_price(price)
    except AttributeError:
        logging.error("%s couldn't find a price" % scrapIG.__name__)
        price = "Not found"

    return price
