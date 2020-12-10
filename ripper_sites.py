from bs4 import BeautifulSoup


with open('Александр Петров — фильмы — КиноПоиск.htm', 'r', encoding='utf-8') as f:
    s = f.read()

soup = BeautifulSoup(s, features="lxml")

# raw_list = soup.find_all('a', {'class': ["styles_link__2anUk"]})
# clear_dict = {}
# for i in range(len(raw_list)):
#     temp = str(raw_list[i].find('span', {'class': ["styles_mainTitle__262Pn"]}))
#     clear = temp[temp.find('>') + 1:temp.find('</')]
#     clear_dict[clear] = raw_list[i].get('href')
#
# print(clear_dict)


# raw_list = soup.find_all('a', {'class': ["styles_link__2anUk"]})
# print(raw_list)
# raw_list = soup.find_all('a', {'class': ["styles_link__"]})
raw_list = soup.find_all('a')
# print(raw_list)
clear_ = []

for i in range(len(raw_list)):
    if str(raw_list[i]).count('styles_mainTitle'):
        clear_.append(raw_list[i])

# print(clear_)
# print(clear_)
temp = str(clear_[0])

clear_dict = {}
for i in range(len(clear_)):
    temp = str(clear_[i])
    temp_clear = temp[temp.find('span class="styles_mainTitle') + 1:temp.find('</span>')]
    clear = temp_clear[temp_clear.find('>') + 1:]
    clear_dict[clear] = clear_[i].get('href')

print(clear_dict)



