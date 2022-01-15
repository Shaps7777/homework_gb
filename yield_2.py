"""
Демонстрация разницы операций над данными, представленными
в виде списка и формируемых генератором
"""

from sys import getsizeof
from time import perf_counter

data_list = [100_000_000 for _ in range(100_000_000)]


def data_gen():
    count = 0
    while count < 100_000_000:
        yield 100_000_000
        count += 1


# print(sum(data_list))
# print(sum(data_gen()))

print('Размер памяти под данные списка: ', getsizeof(data_list))
start = perf_counter()
print('Время суммирования данных в списке: ', sum(data_list), perf_counter() - start)

print('Размер памяти под данные генератора: ', getsizeof(data_gen()))
start = perf_counter()
print('Время суммирования генератором: ', sum(data_gen()), perf_counter() - start)

""" 
Что в итоге
Размер памяти под данные 
                 списка:   835 128 600 байт
              генератора:  104 байт
Время суммирования данных
                в списке:   1.9 c
        данных генератора:  7.85 c
"""

"""
Демонстрация того, что range это одноразовый генератор
"""
a = range(3)
b = a.__iter__()

for i in b:
    print(i)

for i in b:
    print(i)

# print(next(b))
# print(next(b))
