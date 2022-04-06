import logging
from .sites import sites
from concurrent.futures import ThreadPoolExecutor, as_completed


def single(site, name):
    logging.info("Scanning %s for search: %s" % (site, name))
    price = sites[site](name)
    logging.info("%s: %s for search: %s" % (site, price, name))

    return {"name": site, "price": price}


def scrap(name):
    logging.info("Performing search for game: %s" % name)

    prices = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        for out in as_completed([executor.submit(single, site, name)
                                 for site in sites]):
            prices.append(out.result())
            print(out.result())

    logging.info("Search for '%s' done." % name)

    return prices
