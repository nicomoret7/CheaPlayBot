from .sites import sites


def scrap(name):

    prices = []

    for site in sites:
        print("Scanning %s" % site, end='\r')
        price = sites[site](name)
        prices.append({"name": site, "price": sites[site](name)})
        print("%s: %s" % (site, price), end='\n')

    return prices
