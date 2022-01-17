"""
Реализовать формирование списка, используя функцию range()
 и возможности генератора. В список должны войти
 четные числа от 100 до 1000 (включая границы).
 Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def my_list(el_1, el_2):
    return el_1 * el_2


uniq_list = [el for el in range(1, 9, 2)]
print(f'List\n{uniq_list}\nMultiplication_num\n{reduce(my_list, uniq_list)}')
# И с помощью lambda
print(reduce(lambda a, b: a * b, [x for x in range(1, 9, 2)]))
