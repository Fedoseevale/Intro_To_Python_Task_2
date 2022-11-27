# Задача 3
# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
import random

my_listSize = int(input('Введите размер списка: '))
my_list = []

for i in range(my_listSize):
    my_list.append(random.randint(0, 100))
print(f'Имеется список: {my_list}')

# Вариант 1:
for i in range(my_listSize // 2):
    obj = my_list[i]
    my_list[i] = my_list[my_listSize - 1 - i]
    my_list[my_listSize - 1 - i] = obj
print(f'Перемешанный список выглядит следующим образом: {my_list}')

# Вариант 2:
for i in range(my_listSize // 2):
    obj = my_list[i+1]
    my_list[i+1] = my_list[my_listSize - 1 - i]
    my_list[my_listSize - 1 - i] = obj
print(f'Перемешанный список выглядит следующим образом: {my_list}')

# Можно реализовать через метод:
def my_listChange(mylist: list):
    size = len(mylist)
    for i in range(size // 2):
        obj = mylist[i]
        mylist[i] = mylist[size - 1 - i]
        mylist[size - 1 - i] = obj
    return mylist

my_listNew = my_listChange(my_list)
print(f'Перемешанный список выглядит следующим образом: {my_listNew}')

# Могут быть реализованы и другие варианты