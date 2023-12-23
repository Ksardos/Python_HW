# -*- coding: cp1251 -*-
import collections

# Задание 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = [x for x in [factorial(y) for y in range(6, 0, -1)]]
print(result[:10])


# Задание 2
def create():
    last = collections.deque(pets, maxlen=1)[0]
    nickname = input("Введите имя питомца:")
    kind = input("Введите вид питомца:")
    name = input("Введите имя хозяина:")
    age = int(input("Введите возраст питомца:"))
    pets.update({last + 1: {nickname: {'Вид питомца': kind, 'Возраст питомца': age, 'Имя владельца': name}}})

def pet_info_id():
    nicknames = {}
    for i in pets:
        nicknames.update({list(pets[i].keys())[0]: i})
    return nicknames

def print_info(nicknames, nickname):
    id = int(nicknames[nickname])
    print('%s по кличке "%s". Возраст питомца: %a %s. Имя владельца: %s.' % (
    get_pet(id)[nickname]['Вид питомца'], nickname,
    get_pet(id)[nickname]['Возраст питомца'],
    get_suffix(get_pet(id)[nickname]['Возраст питомца']),
    get_pet(id)[nickname]['Имя владельца']))
def read():
    nickname = input("Введите имя питомца:")
    print_info(pet_info_id(), nickname)

def update():
    nickname = input("Введите имя питомца:")
    id = int(pet_info_id()[nickname])
    nickname = input("Введите имя питомца:")
    kind = input("Введите вид питомца:")
    name = input("Введите имя хозяина:")
    age = int(input("Введите возраст питомца:"))
    pets.update({id: {nickname: {'Вид питомца': kind, 'Возраст питомца': age, 'Имя владельца': name}}})


def delete():
    nickname = input("Введите имя питомца:")
    id = int(pet_info_id()[nickname])
    pets.pop(id)


def get_pet(id):
  return pets[id] if id in pets.keys() else False


def get_suffix(n):
    if n % 10 == 1 and n % 100 != 11:
        return 'год'
    elif 2 <= n % 10 <= 4 and not (11 <= n % 100 <= 14):
        return 'года'
    else:
        return 'лет'


def pets_list():
    for i in pets:
        nickname = list(get_pet(i).keys())[0]
        #print(nickname)
        #print(pets[i][nickname])
        print('%i. %s по кличке "%s". Возраст питомца: %a %s. Имя владельца: %s.' % (i,
        get_pet(i)[nickname]['Вид питомца'], nickname, get_pet(i)[nickname]['Возраст питомца'], get_suffix(get_pet(i)[nickname]['Возраст питомца']),
        get_pet(i)[nickname]['Имя владельца']))

def menu():
    print("""1. Создать питомца — create
2. Узнать информацию о питомце — read
3. Добавить питомца — update
4. Удалить питомца — delete
5. Выйти из программы — stop
6. Список питомцев — list""")

pets = {

    1:

        {

            "Мухтар": {

                "Вид питомца": "Собака",

                "Возраст питомца": 9,

                "Имя владельца": "Павел"

            },

        },

    2:

        {

            "Каа": {

                "Вид питомца": "желторотый питон",

                "Возраст питомца": 19,

                "Имя владельца": "Саша"

            },

        },

}

command = ""
menu()
while command != "stop":
    if command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    command = input("Выберите команду:")
