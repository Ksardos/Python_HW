# -*- coding: cp1251 -*-

# Задание 1

n = int(input("Введите количество чисел:"))
count_zero = 0

for i in range(n):
    numb = int(input("Введите целое число:"))
    if numb == 0:
        count_zero += 1
print("Чисел равных нолю: %a." % count_zero)

# Задание 2

natural = int(input("Введите натуральное число:"))
count_natural = 0

if natural == 0:
    print("Вы ввели 0")
elif natural == 1:
    print("Число %a имеет 1 натуральный делитель." % natural)
else:
    for i in range(natural - 1, 1, -1):
        if natural % i == 0:
            count_natural += 1
    print("Число %a имеет %a натуральных делителей." % (natural, count_natural + 2))

# Задание 3

number = list(map(int, input("Введити два натуральных числа через пробел:").split()))
a = number[0]
natural_number = []
for i in range(number[0], number[1] + 1):
    if a % 2 == 0:
        natural_number.append(a)
    a += 1

for i in range(len(natural_number)):
    print(natural_number[i], end=' ')
