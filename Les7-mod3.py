"""
3. Напишите функцию, которая принимает на вход список. Функция создает из этого списка новый список из квадратных корней
 чисел (если число положительное) и самих чисел (если число отрицательное) и возвращает результат (желательно применить
 генератор и тернарный оператор при необходимости). В результате работы функции исходный список не должен измениться.
Например:
old_list = [1, -3, 4]
result = [1, -3, 2]
Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа. 
10-20 чисел в списке вполне достаточно.
"""
import math

old_list = [1, 4, 8, -7, -8, 9, 25, 16, -5, -11]
result = []
result = [math.sqrt(x) if x > 0 else x for x in old_list]
print(result)




