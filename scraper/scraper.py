import logging

from .sites import sites


def scrap(name):

    logging.info("Performing search for game: %s" % name)

    prices = []

    for site in sites:
        logging.info("Scanning %s" % site)
        price = sites[site](name)
        prices.append({"name": site, "price": sites[site](name)})
        logging.info("%s: %s" % (site, price))

    logging.info("Search for '%s' done." % name)

    return prices
