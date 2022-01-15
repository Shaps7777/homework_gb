# Функция reduce - встроенная функция высшего порядка
from functools import reduce

def func(a, b):
    return a+b

data = [10, 20, 30, 40]

print(reduce(func, data))