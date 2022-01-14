""" Пример комприхэншен, то есть создвание одного списка
(кортежа, словаря) из другого одной строкой.
"""
# Классическое исполнение
data = [1, 2, 3, 4, 5, 6, 7]
new_data = []
for el in data:
    if el % 2 == 0:
        new_data.append(str(el ** 2))
print(new_data)

# Комприхэншен
# new_data = [str(el ** 2) for el in data if el % 2 == 0]
new_data = {el: str(el ** 2) for el in data if el % 2 == 0}

print(new_data)
