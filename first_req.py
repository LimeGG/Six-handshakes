import requests
from selenium import webdriver
import os
import time


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
      }

dc = {'Данила Козловский': 'https://www.kinopoisk.ru/name/1054956/',
      }

# f1 = requests.get('https://www.kinopoisk.ru/name/25248/', headers=headers).text
# print(f1)
# with open(f'key.html', 'w') as f:
#     f.write(f1)


# for key in dc.keys():
#     if key not in os.listdir():
#         os.mkdir(key)
#     os.chdir(key)
#     with open(f'{key}.html', 'w') as f:
#         f1 = requests.get(dc[key], headers=headers).text
#         f.write(f1)

driver = webdriver.Firefox()
driver.get("https://www.kinopoisk.ru")
time.sleep(1)
driver.get("https://www.kinopoisk.ru/name/1054956/")


time.sleep(25)

driver.close()


