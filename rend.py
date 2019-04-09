#2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
#  Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.
#  Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

from random import randint, choice
spisok = input("Введите список:")

def func_rand(sp):
    if len(sp) == 0:
        result = 0
    else:
        result = choice(sp)
        return result

rand = func_rand(spisok)

print(rand)