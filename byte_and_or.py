# Оператор and. Он "ленивый", то есть, если первое выражение
# не выполняется (False), то программа идет дальше

import math

# if 1 > 2 and math.sqrt(-1):
#    print('Ошибки нет, т.к. первое условие ложно, программа идет дальше')
# if math.sqrt(-1) and 1 > 2:
#    print('Ошибка, т.к. первое условие невозможно выполнить')

# Если общее выражение содержит ложь, то использование оператора 'and'
# выдает первую встречающуюся ложь
# print([1] and 'qwerty' and {})
# Если общее выражение истинно, то использование оператора 'and'
# выдает последнюю истину
# print([1] and 'qwerty' and {1:'a'})

# Оператор or. Он тоже "ленивый", то есть, если первое выражение
# выполняется (True), то программа идет дальше
# Возвращает первый истинный элемент или последний ложный

# if 2 > 1 or math.sqrt(-1):
#     print('Ошибки нет, т.к. первое условие истино, программа идет дальше')
# Первая истина
# print(0 or [] or 5)
# Последняя ложь
# print(0 or [] or {})

# 'and' - извлечение квадратного корня и оставление тех, у которых он меньше 2

import math


numbers = [4, 1, 2, 3, -4, -6]

# Обычный способ
result = []
for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        if sqrt < 2:
            result.append(number)
print(result)

# Через ленивый 'and'
result = []
for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)
print(result)

# Через генератор
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)

# 'or' - добавление элемента в список

# Обычный способ
def add_to_list(input_list=None):
    if input_list is None:
        input_list = []
    input_list.append('c')
    return input_list

result = add_to_list(['a', 'b'])
print(result)
result = add_to_list()
print(result)

# Через 'or'
def add_to_list(input_list=None):
    input_list = input_list or []
    input_list.append('c')
    return input_list

result = add_to_list(['a', 'b'])
print(result)
result = add_to_list()
print(result)
