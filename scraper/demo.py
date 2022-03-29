from .sites import sites

gameName = input("Insert game name: ")

for site in sites:
    print("Scanning %s" % site, end='\r')
    print("%s: %s" % (site, sites[site](gameName)), end='\n')
