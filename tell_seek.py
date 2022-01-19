# tell определяет позицию курсора
# seek переносит ее
# with open('data.txt', 'r') as f:
    # print(f.tell())
    # print(f.read())
    # print(f.tell())
    # print('_______')
    # f.seek(12)
    # print(f.tell())
    # print(f.read())
    # print(f.tell())
    #
# Опции
with open('data.txt', 'r') as f:
    print(len(f.read()), f.tell())

"""
Есть одна проблема. Если в текстовом файле русский текст, то
каждый символ занимает 2 байта, тогда как в латинице один. 
Тогда метод seek, перемещающий позицию по байту,
может попасть на середину символа и программа вылетает 
"""