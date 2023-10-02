# -*- coding: cp1251 -*-

# Задание 1
pets = {}

nickname = input("Введите имя питомца:")
kind = input("Введите вид питомца:")
name = input("Введите имя хозяина:")
age = int(input("Введите возраст питомца:"))
pets.update({nickname: {'Вид питомца': kind, 'Возраст питомца': age, 'Имя владельца': name}})

year_case = ''
if pets[nickname]['Возраст питомца'] % 10 == 1 and pets[nickname]['Возраст питомца'] != 11:
    if pets[nickname]['Возраст питомца'] % 100 != 11:
        year_case = 'год'
    elif 1 < pets[nickname]['Возраст питомца'] % 10 <= 4 and pets[nickname]['Возраст питомца'] != 12 and pets[nickname]['Возраст питомца'] != 13 and pets[nickname]['Возраст питомца'] != 14:
        year_case = 'года'
    else:
        year_case = 'лет'
elif 1 < pets[nickname]['Возраст питомца'] % 10 <= 4 and pets[nickname]['Возраст питомца'] != 12 and pets[nickname]['Возраст питомца'] != 13 and pets[nickname]['Возраст питомца'] != 14:
    year_case = 'года'
else:
    year_case = 'лет'

print('Это %s по кличке "%s". Возраст питомца: %a %s. Имя владельца: %s.' % (pets[nickname]['Вид питомца'], nickname, pets[nickname]['Возраст питомца'], year_case, pets[nickname] ['Имя владельца']))

# Задание 2

my_dict = {}

for i in range(10, -6, -1):
    my_dict.update({i: i**i})

print(my_dict)
