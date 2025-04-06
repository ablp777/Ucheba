# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв?
# Гласными называют буквы «a», «e», «i», «o», «u».
# Для решения задачи создайте переменную и в неё положите слово с помощью input()
# А также определите количество каждой из этих гласных букв 
# Если какой-то из перечисленных букв нет - Выведите False


print("Введите слово,маленькими латинскими буквами:")
x = input()
a,e,i,o,u = 0,0,0,0,0
for z in x:
    if z == 'a':
        a += 1
    elif z == 'e': 
        e += 1
    elif z == 'i': 
        i += 1
    elif z == 'o': 
        o += 1
    elif z == 'u': 
        u += 1

      
print("Количество а: ")
if a != 0:
    print(a)
else: print("False")

print("Количество e: ")
if e != 0:
    print(e)
else : print("False")

print("Количество i: ")
if i != 0:
    print(i)
else : print("False")

print("Количество o: ")
if o != 0:
    print(o)
else : print("False")

print("Количество u: ")
if u != 0:
    print(u)
else : print("False")



