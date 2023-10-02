# -*- coding: cp1251 -*-

# Задание 1

j = 1
b = []
list1 = []
list2 = []

while True:
    tmp = int(input("Введите натуральное число больше или равное 1 и меньше или равно 100000:"))
    if 1 <= tmp <= 100000:
        n = tmp
        break
    else:
        print("Число вне диапазона, введите другое")

while j <= n:
    tmp = int(input("Введите натуральное число которое по модулю не превышает 2*10e9:"))
    if abs(tmp) <= 20000000000:
        b.append(tmp)
        j += 1
    else:
        print("Число вне диапазона, введите другое")

print(len(set(b)))

# Задание 2

while True:
    tmp = input("Введите число для первого списка, пустая строка завершает ввод:")
    if not tmp:
        print("Ввод завершен")
        break
    list1.append(int(tmp))
    if not len(list1) < 100000:
        print("Ввод завершен")
        break

while True:
    tmp = input("Введите число для второго списка:")
    if not tmp:
        print("Ввод завершен")
        break
    list1.append(int(tmp))
    if not len(list2) < 100000:
        print("Ввод завершен")
        break
print(len(list1 + list2))

# Задание 3

s = set()
numb = list(map(int, input("Введити числа через пробел:").split()))
for i in numb:
    tmp = {i}
    if tmp.issubset(s):
        print(i, 'YES')
    else:
        print(i, 'NO')
    s.add(i)
