# -*- coding: cp1251 -*-

# Задание 1

n = int(input("Введите число строк:"))
a = []
i = 1

while i <= n:
    tmp = int(input("Введите натуральное число больше или равное 1 и меньше или равно 10000:"))
    if 1 <= tmp <= 10000:
        a.append(tmp)
        i += 1
    else:
        print("Число вне диапазона, введите другое")

print("Вы ввели: %a. Перевернутый массив: %a" % (a, a[::-1]))

# Задание 2

i = 1
j = 1
b = []
while i <= 1:
    tmp = int(input("Введите натуральное число больше или равное 1 и меньше или равно 100000:"))
    if 1 <= tmp <= 100000:
        n = tmp
        i += 1
    else:
        print("Число вне диапазона, введите другое")

while j <= n:
    tmp = int(input("Введите натуральное число больше или равное 1 и меньше или равно 2*10e9:"))
    if 1 <= tmp <= 20000000000:
        b.append(tmp)
        j += 1
    else:
        print("Число вне диапазона, введите другое")
b = b[-1:]+b[:-1]
print(b)

# Задание 3

i = 1
m = 0
fishermen = 0
weight = []
boat = []

while i <= 1:
    tmp = int(input("Введите массу которую может перенсти одна лодка. Натуральное число число больше или равное 1 и меньше или равно 1000000:"))
    if 1 <= tmp <= 1000000:
        m = tmp
        i += 1
    else:
        print("Масса вне диапазона, введите другое число")

i = 1
while i <= 1:
    tmp = int(input("Введите количество рыбаков. Натуральное число больше или равное 1 и меньше или равно 100:"))
    if 1 <= tmp <= 100:
        fishermen = tmp
        i += 1
    else:
        print("Масса вне диапазона, введите другое число")

for j in range(fishermen):
    i = 1
    while i <= 1:
        tmp = (int(input("Введите вес рыбака %a:" % int(j + 1))))
        if 1 <= tmp <= m:
            weight.append(tmp)
            i += 1
        else:
            print("Масса вне диапазона, введите другое число")

for x in range(len(weight)):
    if weight[x] + min(weight) <= m:
        boat += [[weight[x], min(weight)]]
        weight[x] += m
        weight[weight.index(min(weight))] += m
    else:
        if weight[x] > m:
            continue
        else:
            boat += [[weight[x]]]

print("Для переправки всех %a рыбаков, потребуется %a лодок." % (fishermen, len(boat)))
