import os
from pathlib import PureWindowsPath
import json
import time

from selenium import webdriver

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}


def login(driver):
    driver.get("https://www.kinopoisk.ru")
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
    # '/html/body/div[1]/div/div[2]/div[4]/div/div/div[1]/div/div/div[7]/div/div[1]/nav/div/div[1]/div/button[1]/span[2]'
    # '/html/body/div[1]/div/div[2]/div[4]/div/div/div[1]/div/div/div[7]/div/div[3]/div/div[79]/div/span'
    # WebElement
    # element = driver.findElement(By.id("id_of_element"));
    # ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", element);
    # Thread.sleep(500);
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    return driver.page_source


def main():
    driver_firefox = webdriver.Firefox()
    login(driver_firefox)
    time.sleep(25)

    dir_with_clear_films = os.listdir('Clear_Films')
    for film in dir_with_clear_films:
        with open(PureWindowsPath('Clear_Films', film), 'r', encoding='utf-8') as file:
            actors_list = json.load(file)['actors']
            for actor in actors_list:
                with open(PureWindowsPath('Actors', f'{actor["actor_name"]}.html'), 'w', encoding='utf-8') as f:
                    f.write(get_actor_page(driver_firefox, actor["actor_href"]))
                    print(f'{actor["actor_name"]} was written!')

    # for key in dict_with_actors.keys():
    #     time.sleep(2)
    #     with open(f'Actors\\{key}.html', 'w', encoding='utf-8') as f:
    #         f.write(get_actor_page(driver_firefox, dict_with_actors[key]))
    #         print(f'{key} was written!')

    driver_firefox.close()


# for key in dict_with_actors.keys():
#     time.sleep(2)
#     with open(f'Actors\\{key}.html', 'w', encoding='utf-8') as f:
#         f.write(get_actor_page(driver_firefox, dict_with_actors[key]))
#         print(f'{key} was written!')


if __name__ == '__main__':
    main()
