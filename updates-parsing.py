import requests
from bs4 import BeautifulSoup

result = {}

# простой скрипт для парсинга обновлений игр с торрент-трекера

url = 'https://tuttop.com'

# делаем запрос и получаем html-файл
html_text = requests.get(url).text

# используем парсер lxml
soup = BeautifulSoup(html_text, 'lxml')

# находим все посты
game_titles = soup.find_all('div', class_ = 'main-news-title')

# достаем название каджой игры и ссылку на пост
for link in game_titles:
    result[link.get_text().strip()] = link.find('a')["href"]

# выводим результаты
for name, link in result.items():
    print(f'{name}:\n\t{link}\n')
