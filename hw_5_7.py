"""
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
"""
# a_list = ["a", "b", "c", "d"]
#
# for iteration, item in enumerate(a_list):
#   print(iteration)

from itertools import count
from math import factorial


def fact_gen():
    for el in count(1):
        yield factorial(el)


gen = fact_gen()

x = 0

for i in gen:
    if x == 15:
        break
    else:
        x += 1
        print(f'Факториал {x} = {i}')
