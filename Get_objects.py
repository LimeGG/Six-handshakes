import os
from pathlib import PureWindowsPath
import json
import time

from selenium import webdriver
from General_Ripper import actors, cinema

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}


def log_in(driver):
    driver.get('https://www.kinopoisk.ru')
    time.sleep(1)
    submit_api = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/header/div/div/div[3]/div/button')
    submit_api.click()
    time.sleep(1)
    with open('creditans.json') as f:
        cred = json.load(f)
    time.sleep(1)
    login = driver.find_element_by_xpath('//*[@id="passp-field-login"]')
    login.clear()
    login.send_keys(cred['username'])

    element_login = driver.find_element_by_xpath(
        '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]')
    element_login.click()

    login_pass = driver.find_element_by_xpath('//*[@id="passp-field-passwd"]')
    login_pass.send_keys(cred['password'])

    element_login = driver.find_element_by_xpath(
        '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button')
    element_login.click()

    try:
        phone_number = driver.find_element_by_xpath(
            '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div[3]/button')
        phone_number.click()
    except Exception as e:
        print(e)


def get_actor_page(driver, actor_href):
    driver.get(actor_href)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(7)
    return driver.page_source


def write_html_actor_page(driver, actor_):
    with open(PureWindowsPath('Actors', f'{actor_["actor_name"]}.html'), 'w', encoding='utf-8') as f:
        f.write(get_actor_page(driver, actor_["actor_href"]))
        print(f'{actor_["actor_name"]} was written!')


def get_actors(driver, write_raw_html=True):
    dir_with_clear_films = os.listdir('Clear_Films')
    for film in dir_with_clear_films:
        with open(PureWindowsPath('Clear_Films', film), 'r', encoding='utf-8') as file:
            actors_list = json.load(file)['actors']
            exist_actors_list = os.listdir('Actors')
            for actor in actors_list:
                if actor['actor_name'] not in exist_actors_list and write_raw_html:
                    write_html_actor_page(driver, actor)
                elif not write_raw_html:
                    actors(get_actor_page(driver, actor["actor_href"]))


object_types = {'Films': 'film_name',
                'Actors': 'actor_name'}
alt_object_types = {'Films': 'actors',
                    'Actors': 'films'}


def get_object(driver, object_type, write_raw_html=True):
    alt_type = alt_object_types[object_type].title()
    dir_with_clear_alt_object = os.listdir(f'Clear_{alt_type}')
    exist_object_list = os.listdir(object_type)
    for alt_object_ in dir_with_clear_alt_object:
        with open(PureWindowsPath(f'Clear_{alt_type}', alt_object_), 'r', encoding='utf-8') as file:
            object_list = json.load(file)[object_type.lower()]
            for object_ in object_list:
                if f'{object_[object_types[object_type]]}.html' not in exist_object_list and write_raw_html:
                    write_html_object_page(driver, object_type, object_)


def get_object_page(driver, object_href):
    driver.get(object_href)
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    # driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(5)
    return driver.page_source


def write_html_object_page(driver, object_type, object_):
    with open(PureWindowsPath(object_type,
                              f'{"".join(x for x in object_[object_types[object_type]] if x.isalnum())}.html'),
              'w', encoding='utf-8') as f:
        if object_type == 'Films':
            f.write(get_object_page(driver, f'{object_["film_href"].replace("series", "film")}\\cast\\'))
            print(f'{object_["film_name"]} was written!')
        else:
            f.write(get_object_page(driver, object_["actor_href"]))
            print(f'{object_["actor_name"]} was written!')


def get_object_by_link(link):
    driver_firefox = webdriver.Firefox()
    log_in(driver_firefox)
    # with open(PureWindowsPath('Films', f'{"".join(x for x in "Мстители: Финал" if x.isalnum())}.html'), 'w', encoding='utf-8') as f:
    #
    #     f.write(get_actor_page(driver_firefox, 'https://www.kinopoisk.ru/film/843650/cast/'))
    # print(f'Роберт Дауни мл. was written!')
    with open(PureWindowsPath('Actors', 'Крис Пратт.html'), 'w', encoding='utf-8') as f:
        f.write(get_object_page(driver_firefox,link))
    # get_object(driver_firefox, 'Films')
    driver_firefox.close()
    # return result


get_object_by_link(r'https://www.kinopoisk.ru/name/224358/')