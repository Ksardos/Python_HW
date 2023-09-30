# -*- coding: cp1251 -*-

# Задание 1

side_triangle = list (map(float, input ("Введити стороны треугольника через пробел:").split()))

#Вычисляем полупериметер
p = sum(side_triangle)/2

#Вычисляем площадь
s = (p  * (p - side_triangle[0]) * (p - side_triangle[1]) * (p - side_triangle[2])) ** 0.5

print ("Площадь треугольнка равна: %f, а его периметр равен: %f" %(s, p * 2))

#Задание 2

numb = list(map(int, str(input ("Введити пятизначное число:"))))
result = float(numb [3] ** numb [4] * numb [2] / (numb [0] - numb [1]))

print (result)
