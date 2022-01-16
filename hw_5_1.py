"""
Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""
from random import randint

data_s_list = []


def my_random():
    data_list = []
    data_s = {}
    for _ in range(10):
        data = randint(0, 100)
        data_list.append(data)
        data_s = set(data_list)
        data_s_list = list(data_s)
        data_s_list.sort(reverse=True)
    print(data_s_list)
    return data_s_list


a = my_random()

print(a)
