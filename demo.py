from scraper.sites import sites


gameName = input("Insert game name: ")

for site in sites:
    print("Scanning %s" % site, end='\r')
    price = sites[site](gameName)
    print("%s: %s" % (site, price), end='\n')
