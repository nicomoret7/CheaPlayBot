from bs4 import BeautifulSoup
from .funcs import parse_price, load_selenium


def scrapHB(name):

    # Selenium (heavy on javascript or scrap-blocking page)
    driver = load_selenium()

    driver.get("https://www.humblebundle.com/store/search?sort=bestselling&search=%s&drm=steam" % name)
    parser = BeautifulSoup(driver.page_source, features="lxml")
    driver.close()

    try:
        price = parser.find('span', attrs={'class': 'price'}).text
        price = parse_price(price)
    except AttributeError:
        price = "Not found"

    return price
