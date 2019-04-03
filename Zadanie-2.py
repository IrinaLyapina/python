chislo = int(input("Введие число : "))
while True:
    if(chislo <=0 or chislo > 10):
      print("Число неверное, диапозон допустимых: чисел больше 0, но меньше 10 ")
      chislo = int(input("Введие число : "))
    else:
      print("Число в степени 2 : ", chislo ** 2)
      break

















