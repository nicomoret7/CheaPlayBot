import logging
from .sites import sites
from concurrent.futures import ThreadPoolExecutor, as_completed
from .sites.funcs import load_selenium


def single(site, name, driver):
    logging.info("Scanning %s for search: %s" % (site, name))
    price = sites[site](name, driver)
    logging.info("%s: %s for search: %s" % (site, price, name))

    return {"name": site, "price": price}


def scrap(name):
    logging.info("Performing search for game: %s" % name)

    prices = []

    driver = load_selenium()

    with ThreadPoolExecutor(max_workers=len(sites)) as executor:
        for out in as_completed([executor.submit(single, site, name, driver)
                                 for site in sites]):
            prices.append(out.result())

    driver.quit()
    logging.info("Search for '%s' done." % name)

    return prices
