# Задача 3
# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
import random

arraySize = int(input('Введите размер массива: '))
array = []

for i in range(arraySize):
    array.append(random.randint(0, 100))
print(f'Имеется массив: {array}')

# Вариант 1:
for i in range(arraySize // 2):
    obj = array[i]
    array[i] = array[arraySize - 1 - i]
    array[arraySize - 1 - i] = obj
print(f'Перемешанный массив выглядит следующим образом: {array}')

# Вариант 2:
for i in range(arraySize // 2):
    obj = array[i+1]
    array[i+1] = array[arraySize - 1 - i]
    array[arraySize - 1 - i] = obj
print(f'Перемеанный массив вышлядит следующим образом: {array}')


# Могут быть и другие варианты