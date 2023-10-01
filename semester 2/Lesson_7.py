# -*- coding: cp1251 -*-

# Задание 1

text = input("Введите строку:")
if text == text[::-1]:
    print("yes")
else:
    print("no")

# Задание 2

text = input("Введите строку:")
if len(text) < 1000:
    corrected_text = " ".join(text.split())
    print(corrected_text)
else:
    print("Текст слишком длинный.")
