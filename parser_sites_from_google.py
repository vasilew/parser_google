# парсер выдачи google (самостоятельный) и подсчет http и https сайтов
from pprint import pprint
from bs4 import BeautifulSoup
import requests
from analyze_https import check_https

#вводим брендовый запрос компании при этом исключаем из выдачи свои сайты
key = input("Введите брендовый запрос для компании: ")

url = f'https://www.google.com/search?q={key}&num=100'

resp = requests.get(url)

soup = BeautifulSoup(resp.text, features="lxml")

all_links = []

correct_links_with_q = []

correct_links = []

#парсим нужные ссылки

for a in soup.find_all('a', href=True):
    if a.text:
        all_links.append(a['href'])

for i in all_links:
    if '/url?q=' in i:
        correct_links.append(i[7:])

links = []

counter_https = 0

counter_http = 0

#считаем ссылки с http и https

for n in correct_links:
    links.append(n.split('&')[0])
    if 'https' in n:
        counter_https = counter_https + 1
    else:
        counter_http = counter_http + 1

#все записываем в файл

file = open('links.txt', 'w')

for line in links:
    file.write(f"{line} \n")

print("All")
