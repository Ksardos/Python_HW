# -*- coding: cp1251 -*-
import random

# Задание 1
def gen_matrix(h, w):
    matrix = [[random.randint(-100, 100) for _ in range(w)] for _ in range(h)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)


size = list(map(int, input("Введите размеры матрицы через пробел:").split()))
matrix_1 = gen_matrix(size[0], size[1])
matrix_2 = gen_matrix(size[0], size[1])
matrix_3 = [[x + y for x, y in zip(one, two)] for (one, two) in zip(matrix_1, matrix_2)]


print("Матрица 1:")
print_matrix(matrix_1)
print("Матрица 2:")
print_matrix(matrix_2)
print("Матрица 3:")
print_matrix(matrix_3)
