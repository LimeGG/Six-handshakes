import json
import time

from selenium import webdriver

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}

dict_with_actors = {'Данила Козловский': 'https://www.kinopoisk.ru/name/1054956/',
                    'Сергей Безруков': 'https://www.kinopoisk.ru/name/224620/',
                    'Александр Петров': 'https://www.kinopoisk.ru/name/2286874/',
                    "Зои Дойч": 'https://www.kinopoisk.ru/name/2347339/',
                    "Джесси Айзенберг": "https://www.kinopoisk.ru/name/43221/",
                    'Бен Аффлек': 'https://www.kinopoisk.ru/name/10620/',
                    'Марго Робби': 'https://www.kinopoisk.ru/name/1682023/',
                    'Леонардо Ди Каприо': 'https://www.kinopoisk.ru/name/37859/'
                    }
driver_firefox = webdriver.Firefox()


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


login(driver_firefox)

for key in dict_with_actors.keys():
    time.sleep(2)
    with open(f'Actors\\{key}.html', 'w', encoding='utf-8') as f:
        f.write(get_actor_page(driver_firefox, dict_with_actors[key]))
        print(f'{key} was written!')

time.sleep(25)

driver_firefox.close()
