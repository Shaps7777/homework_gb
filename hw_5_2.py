"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор (компрехеншн, т.е. создание одного
списка, словаря, пр. из другого одной строкой).
"""
new_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(new_list)

"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Элементы вывести в порядке их следования в исходном списке. 
Использовать компрехеншн.
"""
from random import randint
from time import perf_counter

# Вариант 1. Пробегаем посписку и записываем только те значения
# которые встречаются 1 раз (my_list.count(el) == 1)
my_list = [randint(-10, 10) for _ in range(20000)]
start = perf_counter()
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Начальный список: {my_list}\nСписок без повтора: {uniq_list}')
print(f'Время выполнения операции: {perf_counter() - start}')

# Вариант 2. Делаем через множества.Вначале цикл: если элемента в check нет -
# записываем туда и в uniq. Как только значение 2-й раз встречается,
# перескакиваем в else и изымаем из uniq записанное туда ранее повторившееся значение
start = perf_counter()
check = set()
uniq = set()
# Если делать упорядоченный список, то
# uniq = []
for el in my_list:
    if el not in check:
        check.add(el)
        uniq.add(el)
        # И тогда
        # uniq.append(el)
    else:
        if el in uniq:
            uniq.remove(el)

print(f'Список без повтора: {uniq}')
print(f'Время выполнения операции: {perf_counter() - start}')
