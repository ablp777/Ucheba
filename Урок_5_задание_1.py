﻿#Пользователь вводит целое число. 
#Выведите его строку-описание вида "отрицательное четное число", 
#"нулевое число", "положительное нечетное число", например, 
#численным описанием числа 190 является строка "положительное четное число".
#Если число не является четным - выведите сообщение "число не является четным"
f
print("Введите целочисленное")
x = int(input())


if (x < 0) and ((x % 2) == 0):
    print("отрицательное четное число")
elif x == 0:
    print("нулевое число")
elif (x > 0) and ((x % 2) != 0):
    print("положительное нечетное число")
elif (x > 0) and ((x % 2) == 0):
    print("положительное четное число")

if ( (x%2) != 0):
    print("число не является четным")
  


