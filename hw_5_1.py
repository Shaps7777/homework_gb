"""
Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых размещены в обратном порядке.
"""
from random import randint


def my_random():
    data_list = []
    data_s_list = []
    for _ in range(10):
        data = randint(0, 100)
        data_list.append(data)
        data_s = set(data_list)
        data_s_list = list(data_s)
        data_s_list.sort(reverse=True)

    return data_s_list


a = my_random()

print(a)

# А теперь мы выводим только те значения, которые больше предыдущего.

my_list = [2, 4, 3, 67, 12, 34, 4, 8]
more_than = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_than)
