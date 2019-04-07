# 2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def Function(a, b, c):
   return max (a, b, c)

result = Function(int(input("Введите первое число: ")),int(input("Введите второе число: ")),int(input("Введите третье число: ")))
text = 'Наибольшее число {}'.format(result)
print(text)