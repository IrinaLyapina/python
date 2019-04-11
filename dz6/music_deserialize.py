""" 
2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
 прочитать из них информацию. Получить объект — словарь из предыдущего задания.
"""

import pickle, json, music_serialize

with open('group.pickle', 'rb') as f:
    group_p = pickle.load(f)
    print(group_p)

with open('group.json', 'r') as f:
    group_j = json.load(f)
    print(group_j)

print(music_serialize.my_favourite_group)
