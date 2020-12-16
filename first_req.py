import requests
from selenium import webdriver
import os
import time
import json


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
      }

dc = {'Данила Козловский': 'https://www.kinopoisk.ru/name/1054956/', 'Сергей Безруков': 'https://www.kinopoisk.ru/name/224620/', 'Александр Петров': 'https://www.kinopoisk.ru/name/2286874/', "Зои Дойч": 'https://www.kinopoisk.ru/name/2347339/',
      "Джесси Айзенберг": "https://www.kinopoisk.ru/name/43221/", 'Бен Аффлек':'https://www.kinopoisk.ru/name/10620/', 'Марго Робби':'https://www.kinopoisk.ru/name/1682023/', 'Леонардо Ди Каприо':'https://www.kinopoisk.ru/name/37859/'
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
#driver.get("https://www.kinopoisk.ru/name/1054956/")
time.sleep(1)
submit_api = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/header/div/div/div[3]/div/button')
submit_api.click()
time.sleep(1)
with open('creditans.json') as f:
    cred = json.load(f)

login = driver.find_element_by_xpath('//*[@id="passp-field-login"]')
login.clear()
login.send_keys(cred['username'])

element_login = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]')
element_login.click()

login_pass = driver.find_element_by_xpath('//*[@id="passp-field-passwd"]')
login_pass.send_keys(cred['password'])

element_login = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button')
element_login.click()

try:
    phone_number = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div[3]/button')
    phone_number.click()
except:
    print()

element_search = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/header/div/div/div[2]/div/div[2]/div/form/div/input')
print(element_search)
element_search.send_keys('Александр Петров')
driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/header/div/div/div[2]/div/div[2]/div/form/div/div/button').click()



time.sleep(25)

driver.close()