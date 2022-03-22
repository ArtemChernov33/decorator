import bs4
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from datetime import datetime
from typing import Callable
import os

url = 'https://habr.com/ru/all'

parametrs = '1.txt'

def parametrizeddecor(parametrs):
    def decorator(old_loger):
        def loger(*args, **kwargs):
            p = os.path.abspath(parametrs)
            date_time = datetime.now()
            fun_name = old_loger.__name__
            result = old_loger(*args, **kwargs)
            with open(parametrs, 'w' ) as outfile:
                outfile.write(f'Дата и время вызова функции {date_time}\n'
                                f'Имя функции {fun_name}\n'
                              f'Аргументы, с которыми вызвалась функция {args, kwargs} \n'
                              f'Возвращаемое значение функции {result}\n'
                              f'Путь к файлу логирования {p}'
                )
            return result
        return loger
    return decorator
@parametrizeddecor(parametrs)
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status(url)