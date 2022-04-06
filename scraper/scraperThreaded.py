import logging
import time

from .sites import sites
from concurrent.futures import ThreadPoolExecutor, as_completed


def single(site, name):
    logging.info("Scanning %s for search: %s" % (site, name))
    price = sites[site](name)
    logging.info("%s: %s for search: %s" % (site, price, name))

    return {"name": site, "price": price}


def scrap(name):
    logging.info("Performing search for game: %s" % name)
    time_init = time.perf_counter()

    prices = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        for out in as_completed([executor.submit(single, site, name)
                                 for site in sites]):
            prices.append(out.result())

    time_finnish = time.perf_counter()
    logging.info("Search for '%s' done. Time Spent: %d" % (name, time_finnish-time_init))

    return prices
