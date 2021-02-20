from bs4 import BeautifulSoup
import os
from pathlib import PureWindowsPath
import json


def cinema(film):
    soup = BeautifulSoup(film, features="lxml")
    raw_film_name = soup.find_all('h1')[1].find('a')
    film_href = f"https://www.kinopoisk.ru{raw_film_name.get('href')}"
    film_name = raw_film_name.text
    raw_actors_list = soup.find_all('div', class_="name")

    clear_actor_list = []
    for i in range(len(raw_actors_list)):
        actor_name = raw_actors_list[i].find('a').text.strip()
        actor_href = raw_actors_list[i].find('a').get('href')
        clear_actor_list.append(dict(actor_name=actor_name, actor_href=f"https://www.kinopoisk.ru/{actor_href}"))

    return dict(film_name=film_name, film_href=film_href, actors=clear_actor_list)


def get_clear_list(soup):
    raw_href_list = soup.find_all('a')
    raw_film_list = []
    for href in raw_href_list:
        if str(href).count('styles_mainTitle'):
            raw_film_list.append(href)

    clear_film_list = []
    for raw_film in raw_film_list:
        film_name = raw_film.find('span').text
        film_href = raw_film.get('href')
        clear_film_list.append(dict(film_name=film_name,
                                    film_href=f"https://www.kinopoisk.ru/{film_href}".replace('//', '/')))
    return clear_film_list


def get_clear_list_by_table(soup):
    raw_href_list_by_table = soup.find('div', {'class': ["personPageItems"]}).find_all('table')
    raw_film_list = []
    for film in raw_href_list_by_table:
        film = film.find('a')
        film_name = film.text.strip().replace('\xa0', ' ')
        film_href = film.get('href')

        raw_film_list.append(dict(film_name=film_name,
                                    film_href=f"https://www.kinopoisk.ru/{film_href}".replace('//', '/')))

    return raw_film_list


def actors(actor):
    soup = BeautifulSoup(actor, features="lxml")
    actor_name = soup.find_all('h1')[0].text.strip()
    actor_href = soup.find(rel="canonical").get('href')

    clear_film_list = get_clear_list(soup)
    if not clear_film_list:
        clear_film_list = get_clear_list_by_table(soup)
    return dict(actor_name=actor_name, actor_href=actor_href, films=clear_film_list)


def ripper(dir_with_object, ripper_type):
    for object_type in dir_with_object:
        try:
            with open(PureWindowsPath(ripper_type, object_type), 'r', encoding='utf-8') as f:
                if ripper_type == "Films":
                    ds = cinema(f.read())
                else:
                    ds = actors(f.read())
                with open(f'Clear_{ripper_type}\\'
                          f'{"".join(x for x in ds[ripper_types[ripper_type]] if x.isalnum())}.json',
                          'w', encoding='utf-8') as g:
                    json.dump(ds, g, indent=2, ensure_ascii=False)
        except IndexError:
            print(f'Unexpected html page:{object_type}')
            continue


ripper_types = {'Films': 'film_name',
                'Actors': 'actor_name'}


def main():
    dir_with_films = os.listdir('Films')
    ripper(dir_with_films, 'Films')

    dir_with_films = os.listdir('Actors')
    ripper(dir_with_films, 'Actors')


if __name__ == '__main__':
    main()
