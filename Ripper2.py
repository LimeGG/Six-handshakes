from bs4 import BeautifulSoup
with open('Word.html', 'r', encoding='utf-8') as f:
    s = f.read()
def cinema(s):
    soup = BeautifulSoup(s, features="lxml")
    raw_list = soup.find_all('div', class_="name")

    clear_dict = {}
    for i in range(len(raw_list)):
        temp = str(raw_list[i])
        temp_clear = temp[temp.find('f=')+3:temp.find('</a')].split('">')
        clear_dict[temp_clear[1]] = "https://www.kinopoisk.ru/" + temp_clear[0]

    return clear_dict
with open('Word.html', 'r', encoding='utf-8') as f:
    s = f.read()
with open('strel.html', 'r', encoding='utf-8') as f:
    g = f.read()
with open('ice.html', 'r', encoding='utf-8') as f:
    t = f.read()
with open('Gogol.html', 'r', encoding='utf-8') as f:
    i = f.read()
with open('Hero.html', 'r', encoding='utf-8') as f:
    y = f.read()
with open('Method.html', 'r', encoding='utf-8') as f:
    o = f.read()
with open('sad.html', 'r', encoding='utf-8') as f:
    p = f.read()
with open('vtor.html', 'r', encoding='utf-8') as f:
    n = f.read()
with open('Anna.html', 'r', encoding='utf-8') as f:
    z = f.read()
with open('born.html', 'r', encoding='utf-8') as f:
    x = f.read()

print(cinema(x))
print(cinema(z))
print(cinema(n))
print(cinema(p))
print(cinema(o))
print(cinema(y))
print(cinema(i))
print(cinema(t))
print(cinema(s))
print(cinema(g))