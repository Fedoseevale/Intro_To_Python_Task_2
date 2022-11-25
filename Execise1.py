# Задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

import random
from decimal import Decimal

number = round(Decimal(random.uniform(0, 10000)), 4)
print(f'Задано вещественное число: {number}')

number = str(number)
number = number.split('.')
# print(number)
number1 = int(number[0])
# print(number1)
number2 = int(number[1])
# print(number2)
digit1 = 0
while number1 >=1:
    digit1 = int(number1 % 10)+digit1
    # print(digit1)
    number1 = int(number1 / 10)
# print(digit1)
digit2 = 0
while number2 >=1:
    digit2 = int(number2 % 10)+digit2
    # print(digit2)
    number2 = int(number2 / 10)
# print(digit2)
sumDigits = digit1 + digit2
# print(sumDigits)
print(f'Сумма цифр данного вещественного числа равна: {sumDigits}')






