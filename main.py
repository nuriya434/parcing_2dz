import requests
from bs4 import BeautifulSoup

for i in range(1, 4):
    print(f'Парсим {i}-ю стр...')
    url = f'https://www.olx.kz/list/q-%D0%B5%D0%BB%D0%BA%D0%B8/?page={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    cards = soup.find_all("div", class_="css-1sw7q4x")
    names = soup.find_all("h6", class_="css-16v5mdi er34gjf0")
    
    for j in range(0, 2):
        print(f"{names[j].text}: NAMEEEEEEE")
        card_url = cards[j].a['href']
        card_response = requests.get(url=f'https://www.olx.kz{card_url}')
        card_soup = BeautifulSoup(card_response.text, 'lxml')
        descriptions = card_soup.find("div", class_="css-1t507yq er34gjf0")
        print(f"{j}:   {descriptions.text}")