import os

# Удаление файла (минуя корзину, т.е. "безвозвратно")
# os.remove('auto.png')
# Удаление директории
# os.rmdir('...')
# Переименование файла
# os.rename('data.txt', 'data_0.txt')
# Переименование файла
# print(os.listdir())

# Интересно
# Можно написать к-ду напрямую в Терминале
# os.system('dir')
# Но так как операционные системы различны, то не все так просто
# import platform
# user_komp = platform.platform()
# print(user_komp)
# if 'win' in user_komp: # Здесь почему то 'win' не определяется
#     os.system('dir')
# elif 'mac' in user_komp or 'Linux' in user_komp:
#     os.system('ls')

# Проверка наличия файлов
from os.path import isfile

# print(isfile('data.txt'))
# print(isfile('data_100.txt'))

# Смотрим, что внутри рабочей директории
for el in os.listdir():
    print(el)
print('_________')
for el in os.listdir():
    if isfile(el) and not el.startswith('.'):
        print(el)
        # можно и удалить
        # os.remove(el)