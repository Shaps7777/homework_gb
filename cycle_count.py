from itertools import cycle, count

# Это генератор последовательности целых числе
for i in count():
    if i == 20:
        break
    print(i)

# Эта функция выводит данные циклично
el = 0
for i in cycle(['a', 'b', 'c']):
    if el == 20:
        break
    print(i)
    el += 1
