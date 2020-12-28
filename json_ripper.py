import json

actors = [{
    "actor_name": "Александр Петров",
    "actor_href": "https://www.kinopoisk.ru//name/2286874/",
    "films": [
        {
            "film_name": "#Зановородиться",
            "film_href": "https://www.kinopoisk.ru/film/1117965/"
        },
        {
            "film_name": "#За1новородиться",
            "film_href": "https://www.kinopoisk.ru/film/11137965/"
        },
        {
            "film_name": "Анна",
            "film_href": "https://www.kinopoisk.ru/film/1049727/"
        }

    ]
},{
    "actor_name": "Ирина Старшенбаум",
    "actor_href": "https://www.kinopoisk.ru//name/3873197/",
    "films": [
        {
            "film_name": "#Зановородиться",
            "film_href": "https://www.kinopoisk.ru/film/1117965/"
        },
        {
            "film_name": "#Зановородить1ся",
            "film_href": "https://www.kinopoi1sk.ru/film/11179265/"
        }
    ]
},{
    "actor_name": "Саша Лусс",
    "actor_href": "https://www.kinopoisk.ru//name/4462805/",
    "films": [
        {
            "film_name": "Анна",
            "film_href": "https://www.kinopoisk.ru/film/1049727/"
        }
    ]
}]

temp = False
for i in range(len(actors)):
    # actors[i]
    for j in range(i+1, len(actors)):
        for film in actors[i]['films']:
            if film in actors[j]['films']:
                temp = film in actors[j]['films']
                print(actors[j]['actor_name'])



