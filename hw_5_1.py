"""
Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""
from random import randint

data_list = []


def my_random():
    for _ in range(10):
        data = randint(0, 100)
        data_list.append(data)
        data_list.sort(reverse=True)


my_random()
print(data_list)
