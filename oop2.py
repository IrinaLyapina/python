'''1. Получить количество учеников с сайта geekbrains.ru:
a) при помощи регулярных выражений,
b) при помощи библиотеки BeautifulSoup.'''
import re
from bs4 import BeautifulSoup as BS

file=open('my_file.html','r', encoding="utf-8")
text=file.read()
li = re.findall("Нас уже ([0-9 s]+)", text)
print(li)

soup = BS(text, "html.parser")
tag = soup.find("span", class_="total-users")
print(tag.string)

