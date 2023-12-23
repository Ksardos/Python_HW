# -*- coding: cp1251 -*-

# Задание 1

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list(ist, end=' '):
    if ist:
        val = ist.pop(0)
        print(val, end=end)
        return print_list(ist, end=end)
    else:
        print('Конец списка')


print_list(my_list)
