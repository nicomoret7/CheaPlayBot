from .eneba import scrapEneba
from .g2a import scrapG2A
from .gog import scrapGOG
from .humbleBundle import scrapHB
from .instantGaming import scrapIG
from .steam import scrapSteam

sites = {
    "Steam":            scrapSteam,
    "Eneba":            scrapEneba,
    "G2A":              scrapG2A,
    "GOG":              scrapGOG,
    "Humble Bundle":    scrapHB,
    "Instant Gaming":   scrapIG
}
