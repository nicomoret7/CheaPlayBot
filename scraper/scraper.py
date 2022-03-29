from .sites import sites


def scrap(name):

    prices = []

    for site in sites:
        prices.append({"name": site, "price": sites[site](name)})

    return prices
