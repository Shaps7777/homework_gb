"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


# 1 вариант. Удаляем минимальный элемент
# и суммируем остальные
def my_f(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Enter only a namber!'


# 2 вариант. Сортируем
# и суммируем начиная со 2-го элемента
def my_f_2(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    return sum(sorted(my_list)[1:])


my_sum = my_f(1, 2, 3)
print(my_sum)
my_sum = my_f_2(1, 2, 3)
print(my_sum)
