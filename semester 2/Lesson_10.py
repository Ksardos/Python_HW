# -*- coding: cp1251 -*-

# ������� 1
pets = {}

nickname = input("������� ��� �������:")
kind = input("������� ��� �������:")
name = input("������� ��� �������:")
age = int(input("������� ������� �������:"))
pets.update({nickname: {'��� �������': kind, '������� �������': age, '��� ���������': name}})

year_case = ''
if pets[nickname]['������� �������'] % 10 == 1 and pets[nickname]['������� �������'] != 11:
    if pets[nickname]['������� �������'] % 100 != 11:
        year_case = '���'
    elif 1 < pets[nickname]['������� �������'] % 10 <= 4 and pets[nickname]['������� �������'] != 12 and pets[nickname]['������� �������'] != 13 and pets[nickname]['������� �������'] != 14:
        year_case = '����'
    else:
        year_case = '���'
elif 1 < pets[nickname]['������� �������'] % 10 <= 4 and pets[nickname]['������� �������'] != 12 and pets[nickname]['������� �������'] != 13 and pets[nickname]['������� �������'] != 14:
    year_case = '����'
else:
    year_case = '���'

print('��� %s �� ������ "%s". ������� �������: %a %s. ��� ���������: %s.' % (pets[nickname]['��� �������'], nickname, pets[nickname]['������� �������'], year_case, pets[nickname] ['��� ���������']))

# ������� 2

my_dict = {}

for i in range(10, -6, -1):
    my_dict.update({i: i**i})

print(my_dict)