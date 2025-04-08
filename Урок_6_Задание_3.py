#Вводятся целые числа A и B. Гарантируется, что A ≤ B.
#Выведите все четные числа на заданном отрезке через пробел.

from socket import setdefaulttimeout


print("Введите число А:")
a = int(input())

print("Введите число B, (число B не должно быть меньше чем А):")
b = int(input())

out = ""
x = 0
s = ''
if b<a:
    print("Число B меньше числа А")
else:

    for i in range(a,b+1):
        x = i % 2
        if x == 0:
            s = str(i)
            out += s
            out += " "
   
print(out)