import logging
from bs4 import BeautifulSoup
from .funcs import parse_price, load_selenium


def scrapG2A(name):

    # Selenium (heavy on javascript or scrap-blocking page)
    driver = load_selenium()

    driver.get("https://www.g2a.com/category/games-c189?f[device][0]=1118&f[drm]["
               "0]=1&query=%s&sort=price-lowest-first&___currency=EUR" % name)
    parser = BeautifulSoup(driver.page_source, features="lxml")
    driver.close()

    try:
        price = parser.find('span', attrs={'class': 'fhiSmq'}).text
        price = parse_price(price)
    except AttributeError:
        logging.error("%s couldn't find a price" % scrapG2A.__name__)
        price = "Not found"

    return price
