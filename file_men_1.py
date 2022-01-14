import os
import shutil
import datetime
import random


# Функция создания файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# Функция создания директории
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая директория уже существует')


# Функция копирования файла или директории
def copy_file_or_dir(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая директория (файл) уже существует')
    else:
        shutil.copy(name, new_name)


# Функция удаления файла или директории
def delete_file_or_dir(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# Расширение функционала (вывод всех файлов и директорий)
def get_list_f_dir():
    print(os.listdir())


# Вывод только директорий
def get_list_dir(folder_only=False):
    result = os.listdir()
    if folder_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# Запись информации по работе менеджера файлов
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_dir(name):
    os.chdir(name)
    print(os.getcwd())


def game_namber():
    input('Задумайте число от 1 до 100, компьютер будет угадывать, после нажмите Enter')
    count = 0
    min_namber = 1
    max_namber = 100
    result = None
    while result != '=':
        namber = random.randint(min_namber, max_namber)
        print('Это ', namber, '?')
        count += 1
        result = input('А у вас "=", меньше "<" или больше ">":    ')
        if result == '>':
            min_namber = namber + 1
        elif result == '<':
            max_namber = namber - 1
    print(f'Угадано c {count} попытки')

# Следующая строка кода нужна для того, чтобы при импорте нашей функции
# в другой скрипт, этот код не выполнялся (т.к. ниже процедуры проверки работы выше созданных функций)
# if __name__ == '__main__':
    # create_file('text.dat', 'some text')
    # create_folder('new_f')
    # get_list_f_dir()
    # get_list_dir(True)
    # delete_file_or_dir('text.dat')
    # copy_file_or_dir('new_f', 'new_f2')
    # copy_file_or_dir('text.dat', 'new_text.dat')
    # save_info('abc')
    # game_namber()
