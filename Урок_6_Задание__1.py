﻿#Сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте, сколько из них равны нулю, и выведите это количество.


print("Введите число: ") #непонятно как ввести отрицательное количество чисел(возможно имелось в виду вводится ровно N натуральных чисел?)
count = 0
n = int(input())
if n > 0:
    print("Теперь введите (",n,") целых чисел.", sep ='')
    for i in range(0, n, 1):
        j = int(input())
        if (j == 0):
            count += 1
    print("Вы ввели ",n," чисел, из которых ",count," равны нулю.")
elif n == 0:
    print("Вы ввели ",n," чисел, из которых 0 равны нулю.")
elif n < 0:
    print("Теперь введите (",n,") целых чисел.", sep ='')
    for i in range(n, 0, 1):
        j = int(input())
        if (j == 0):
            count += 1
    print("Вы ввели ",n," чисел, из которых ",count," равны нулю.")