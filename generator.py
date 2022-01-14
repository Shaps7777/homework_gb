nambers = [1, 2, 3, 4, 5, -1, -2, -3]
result = []
# Из данного списка оставить только положительные числа

# Классический способ
for namber in nambers:
    if namber > 0:
        result.append(namber)
print(result)

# Через функцию filter
result = filter(lambda namber: namber > 0, nambers)
print(list(result))

# Через генератор (лучший из 3-х)
result = [namber for namber in nambers if namber > 0]
print(result)

# Генератор словарей (используется редко)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# Классический способ
result = {}
for pair in pairs:
    key = pair[0]
    val = pair[1]
    result[key] = val
print(result)

# Через генератор
result = {pair[0]:pair[1] for pair in pairs}
print(result)
