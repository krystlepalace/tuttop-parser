import requests
from bs4 import BeautifulSoup


def get_updates():
    '''Возвращает список последних обновлений игр с сайта.'''

    result = {}

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
    
    return result

# выводим результаты
if __name__ == '__main__':
    updates = get_updates()
    for name, link in updates.items():
        print(f'{name}:\n\t{link}\n')
