import logging
from bs4 import BeautifulSoup
from .funcs import load_selenium, parse_price


def scrapIG(name):

    # Selenium (heavy on javascript or scrap-blocking page)
    driver = load_selenium()

    driver.get("https://www.instant-gaming.com/en/search/?platform[]=&type[]=steam&query=%s" % name)
    parser = BeautifulSoup(driver.page_source, features="lxml")
    driver.close()

    try:
        listing = parser.find(attrs={'class': 'listing-games'})
        price = listing.find('div', attrs={'class': 'price'}).text
        price = parse_price(price)
    except AttributeError:
        logging.error("%s couldn't find a price" % scrapIG.__name__)
        price = "Not found"

    return price
