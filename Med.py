name = input("Введие имя и фамилию : ")
age = int(input("Введие возраст : "))
weight = float(input("Введие вес : "))
if age < 30:
     if (weight > 50 and weight < 120):
          print(name, ", Вы в хорошем состоянии ")
     else: print(name, ", в 30 что-то не так! ")
else:
     if (age > 40):
          if (weight < 50 or weight > 120):
               print(name, ", Вам требуется врачебный осмотр! ")
          else: print(name, ", в 40 все ок! ")
     else:
          if (weight < 50 or weight > 120): print(name,", Вам нужно заняться собой! ")
