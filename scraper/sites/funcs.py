import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


def parse_price(p):
    p = re.sub("[^0-9,.a-zA-Z]", "", p).replace(',', '.')
    p += (" €" if p != "FREE" else "")

    return p


def load_selenium():
    firefoxOptions = Options()
    firefoxOptions.add_argument("--headless")
    driver = webdriver.Firefox(
        service=Service(r'./scraper/geckodriver'),
        options=firefoxOptions)

    return driver
