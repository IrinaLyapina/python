"""
1. Получите текст из файла.
2. Разбейте текст на предложения.
3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
4. Отберите все ссылки.
5. Ссылки на страницы какого домена встречаются чаще всего?
6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
"""
import re

#задание1
file=open('my_file.txt','r', encoding="utf-8")
text=file.read()
print(text)

#задание2
for text1 in re.split(r'(?<=[.!?…]) ', text):
    print(text1)

#задание3
mass = []
s_text = r'\b[а-я]{4,15}\b'
for match in re.findall(s_text, text):
    mass.append(match)
print(max(mass))

#задание4
url = re.findall("\S*\.\S+", text)
print(url)

#задание5
mas=[]
pattern = "\.\w+"
for match in re.findall(pattern, text):
    mas.append(match)
print(max(mas))

#задание6
new_text =re.sub("\S*\.\S+", "Ссылка отобразится после регистрации", text)
print(new_text)






