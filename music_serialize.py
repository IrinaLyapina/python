'''1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы,
 например: my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}
С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
 Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
'''
import pickle, json

my_favourite_group = {'name': 'Г.М.О.','tracks': ['Последний месяц осени', 'Шапито'],
                      'Albums': [{'name': 'Делать панк-рок','year': 2016},
                      {'name': 'Шапито','year': 2014}]}
#запись файлов
with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

with open('group.json', 'w', encoding ='utf-8') as f:
    json.dump(my_favourite_group, f)

#вывод результатов в терминал
with open('group.pickle', 'rb') as f:
    prt_p = pickle.load(f)
    print(prt_p)

with open('group.json', 'r') as f:
    prt_j = json.load(f)
    print(prt_j)
