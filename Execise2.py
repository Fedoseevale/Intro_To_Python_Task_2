# Задача 2
# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

from decimal import Decimal

n = int(input('Введите количество элементов: '))
my_list = [0] * n
for i in range(n):
    my_list[i] = f'{i+1}: {round((1+1/(i+1))**(i+1),2)}'
print(f'Список: {my_list}')
sum = 0
for i in range(n):
    sum = sum + round((1+1/(i+1))**(i+1),2)
print(f'Сумма элементов списка: {round((sum),2)}')