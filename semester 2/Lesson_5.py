# -*- coding: cp1251 -*-

# Задание 1

numb = int (input ("Введите целое число:"))

# Проверка на четность
if ( numb%2 == 0):
    even = True
else:
    even = False

    
if (numb == 0):
    print ("Вы ввели ноль")
elif (numb < 0) and (even):
    print ("Отрицательное четное число")
elif (numb < 0) and not (even):
    print ("Отрицательное нечетное число")
elif (numb > 0) and (even):
    print ("Положительное четное число")
else:  
    print ("Положительное нечетное число")
    
# Задание 2

#Создаем переменную со списком гласных
vowels =['a', 'e', 'i', 'o', 'u']
count_vowels ={'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}
count_consonants = 0

text = list (input ("Введити строку:"))


# Считаем количество каждой из гласных
for i in range(len(vowels)):
    count_vowels[vowels[i]] = text.count(vowels[i])

# Считаем количество согласных    
count_consonants = len(text) - sum(count_vowels.values())

print ("В тексте %a согласных." %count_consonants)
print ("Каждая из гласных встречаеться:")

for i in range(len(vowels)):
    if count_vowels[vowels[i]] == 0:
        print ("%s False" %(vowels[i]))  
    else:
        print ("%s %a" %(vowels[i],count_vowels[vowels[i]]))

# Задание 3

investment_amount = int (input ("Введите сумму требуемую для инвестиций:"))
mike = int (input ("Введите сколько долларов у Майка:"))
ivan = int (input ("Введите сколько долларов у Ивана:"))

if investment_amount <= mike and investment_amount <= ivan:
    print ("2")
elif investment_amount <= (mike + ivan):
    print ("1")
elif investment_amount <= mike:
    print ("Mike")
elif investment_amount <= ivan:
    print ("Ivan")    
else:
    print ("0")
