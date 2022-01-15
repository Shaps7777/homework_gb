""" Пример комприхэншен, то есть создвание одного списка
(кортежа, словаря) из другого одной строкой.
"""

# data = [1, 2, 3, 4, 5, 6, 7]
# new_data = []


# Классическое исполнение
# for el in data:
#     if el % 2 == 0:
#         new_data.append(str(el ** 2))
# print(new_data)

# Комприхэншен, множества, кстати, также как словарь, в {} но без :
# new_data = [str(el ** 2) for el in data if el % 2 == 0]
# new_data = {str(el ** 2) for el in data if el % 2 == 0}
# new_data = {el: str(el ** 2) for el in data if el % 2 == 0}
# без if
new_data = {el ** 3 for el in range(5, 10)}

print(new_data)
