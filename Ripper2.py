import os
import json
from bs4 import BeautifulSoup


def cinema(film):
    soup = BeautifulSoup(film, features="lxml")
    raw_film_name = soup.find_all('h1')[1].find('a')
    film_href = f"https://www.kinopoisk.ru{raw_film_name.get('href')}"
    raw_film_name_str = str(raw_film_name)
    film_name = raw_film_name_str[raw_film_name_str.find('>') + 1:raw_film_name_str.find('</a')]
    raw_list = soup.find_all('div', class_="name")

    clear_list = []
    for i in range(len(raw_list)):
        temp = str(raw_list[i])
        temp_clear = temp[temp.find('f=') + 3:temp.find('</a')].split('">')
        clear_list.append(dict(actor_name=temp_clear[1], actor_href="https://www.kinopoisk.ru/" + temp_clear[0]))

    return dict(film_name=film_name, film_href=film_href, actors=clear_list)


def ripper(dir_with_films):
    for film in dir_with_films:
        with open(f'Films\\{film}', 'r', encoding='utf-8') as f:
            ds = cinema(f.read())
            with open(f'Clear_films\\{ds["film_name"]}.json', 'w') as g:
                json.dump(ds, g, indent=2)


def main():
    dir_with_films = os.listdir('Films')
    ripper(dir_with_films)


if __name__ == '__main__':
    main()
