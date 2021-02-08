from bs4 import BeautifulSoup
import os
from pathlib import PureWindowsPath
import json


# for file in os.listdir('Actors'):
#     with open(PureWindowsPath('Actors', file), 'r', encoding='utf-8') as f:
#         s = f.read()
#
#     soup = BeautifulSoup(s, features="lxml")
#
#     raw_list = soup.find_all('a')
#     clear_ = []
#
#     for i in range(len(raw_list)):
#         if str(raw_list[i]).count('styles_mainTitle'):
#             clear_.append(raw_list[i])
#
#     temp = str(clear_[0])
#
#     clear_dict = {}
#     for i in range(len(clear_)):
#         temp = str(clear_[i])
#         temp_clear = temp[temp.find('span class="styles_mainTitle') + 1:temp.find('</span>')]
#         clear = temp_clear[temp_clear.find('>') + 1:]
#         clear_dict[clear] = clear_[i].get('href')
#
#     print(clear_dict)


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


def actors(actor):
    soup = BeautifulSoup(actor, features="lxml")
    raw_actor_name = soup.find_all('h1')[1].find('a')
    actor_name = raw_actor_name[raw_actor_name.find('>') + 1:raw_actor_name.find('</a')]
    raw_list = soup.find_all('a')

    clear_ = []
    for i in range(len(raw_list)):
        if str(raw_list[i]).count('styles_mainTitle'):
            clear_.append(raw_list[i])
    actor_href = f"https://www.kinopoisk.ru{raw_actor_name.get('href')}"

    clear_list = []
    for i in range(len(raw_list)):
        temp = str(raw_list[i])
        temp_clear = temp[temp.find('span class="styles_mainTitle') + 1:temp.find('</span>')]
        clear_list.append(dict(film_name=temp_clear[1], film_href="https://www.kinopoisk.ru/" + temp_clear[0]))

    return dict(actor_name=actor_name, actor_href=actor_href, films=clear_list)


def ripper(dir_with_films, ripper_type):
    for film in dir_with_films:
        with open(PureWindowsPath(ripper_type, film), 'r', encoding='utf-8') as f:
            if ripper_type == "Films":
                ds = cinema(f.read())
                with open(f'Clear_{ripper_type}\\{ds["film_name"]}.json', 'w') as g:
                    json.dump(ds, g, indent=2)
            else:
                ds = cinema(f.read())
                with open(f'Clear_{ripper_type}\\{ds["actor_name"]}.json', 'w') as g:
                    json.dump(ds, g, indent=2)


def main():
    # dir_with_films = os.listdir('Films')
    # ripper(dir_with_films, 'Films')

    dir_with_films = os.listdir('Actors')
    ripper(dir_with_films, 'Actors')


if __name__ == '__main__':
    main()
