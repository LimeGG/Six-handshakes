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
        actor_name = raw_actors_list[i].find('a').text
        actor_href = raw_actors_list[i].find('a').get('href')
        clear_actor_list.append(dict(actor_name=actor_name, actor_href=f"https://www.kinopoisk.ru/{actor_href}"))

    return dict(film_name=film_name, film_href=film_href, actors=clear_actor_list)


def actors(actor):
    soup = BeautifulSoup(actor, features="lxml")
    actor_name = soup.find_all('h1')[0].text
    actor_href = soup.find(rel="canonical").get('href')
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

    return dict(actor_name=actor_name, actor_href=actor_href, films=clear_film_list)


def ripper(dir_with_object, ripper_type):
    for object_type in dir_with_object:
        with open(PureWindowsPath(ripper_type, object_type), 'r', encoding='utf-8') as f:
            if ripper_type == "Films":
                ds = cinema(f.read())
                with open(f'Clear_{ripper_type}\\{ds["film_name"]}.json', 'w', encoding='utf-8') as g:
                    json.dump(ds, g, indent=2, ensure_ascii=False)
            else:
                ds = actors(f.read())
                with open(f'Clear_{ripper_type}\\{ds["actor_name"]}.json', 'w', encoding='utf-8') as g:
                    json.dump(ds, g, indent=2, ensure_ascii=False)


def main():
    dir_with_films = os.listdir('Films')
    ripper(dir_with_films, 'Films')

    dir_with_films = os.listdir('Actors')
    ripper(dir_with_films, 'Actors')


if __name__ == '__main__':
    main()
