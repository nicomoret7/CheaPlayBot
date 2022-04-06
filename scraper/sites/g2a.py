import logging
from bs4 import BeautifulSoup
from .funcs import parse_price, load_selenium


def scrapG2A(name):

    driver = load_selenium()

    try:
        driver.get("https://www.g2a.com/category/games-c189?___currency=EUR&f[device][0]=1118&f[drm][0]=1&f[regions]["
                   "0]=8355&f[regions][1]=878&query=%s&sort=price-lowest-first" % name)
    except Exception as e:
        print("Connection error on G2A: " + e.__class__.__name__)

    parser = BeautifulSoup(driver.page_source, features="lxml")
    driver.quit()

    '''
    try:
        file = open("g2a.html", "w")
        file.write(driver.page_source)
        file.close()
    except IOError as e:
        logging.error("I/O Error", exc_info=True)
    '''

    try:
        price = parser.find('span', attrs={'class': 'fhiSmq'}).text
        price = parse_price(price)
    except AttributeError:
        logging.error("%s couldn't find a price" % scrapG2A.__name__)
        price = "Not found"

    return price
