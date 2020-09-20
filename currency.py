import requests
from bs4 import BeautifulSoup
import time

DOLLAR_RUB = 'https://www.google.com/search?client=firefox-b-d&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
EURO_RUB = 'https://www.google.com/search?client=firefox-b-d&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E'

def check_currency():
    full_page_dol = requests.get(DOLLAR_RUB, headers=headers)
    soup_dol = BeautifulSoup(full_page_dol.content, 'html.parser')

    full_page_eur = requests.get(EURO_RUB, headers=headers)
    soup_eur = BeautifulSoup(full_page_eur.content, 'html.parser')

    convert_eur = soup_eur.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision':'2'})

    convert_dol = soup_dol.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision':'2'})
   
    print('Текущий курс: 1 доллар = ' + convert_dol[0].text)
    print('Текущий курс: 1 евро = ' + convert_eur[0].text)
    time.sleep(3)
    check_currency()

check_currency()
