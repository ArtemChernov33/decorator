import bs4
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from datetime import datetime

import os

KEYWORDS = ['WFM: планирование рабочего времени и управление персоналом', 'Geo data in Python', 'Кофеин: как это работает?', '2']

url = 'https://habr.com/ru/all'

response = requests.get(url)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all("article")

def decorator(old_loger):
    def loger(*args, **kwargs):
        p = os.path.abspath(name)
        date_time = datetime.now()
        fun_name = old_loger.__name__
        result = old_loger(*args, **kwargs)
        with open(name, 'w' ) as outfile:
            outfile.write(f'Дата и время вызова функции {date_time}\n'
                            f'Имя функции {fun_name}\n'
                          f'Аргументы, с которыми вызвалась функция {args, kwargs} \n'
                          f'Возвращаемое значение функции {result}\n'
                          f'Путь к файлу логирования {p}'
            )

        return result
    return loger

@decorator
def get_data(name):
    for article in articles:
        titles = article.find_all(class_="tm-article-snippet__title tm-article-snippet__title_h2")
        titles = set(title.text.strip() for title in titles)
        for title in titles:
            if title in KEYWORDS:
                date = article.find(class_="tm-article-snippet__datetime-published").time['title']
                href = article.find(class_="tm-article-snippet__title-link").attrs['href']
                url_ = ("https://habr.com" + href)
                rezult = print(f'Дата выпуска статьи:{date}. Название статьи:{title}. Ссылка на статью:{url_}')
                pprint(rezult)
name = input('В ведите имя Лога')
if __name__ == '__main__':
    get_data(name=name)