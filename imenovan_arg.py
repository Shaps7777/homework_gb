"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
"""


def menu():  # Меню выбора
    print('_____Выберите действие_____')
    print('1. Ввод данных\n2. Вывод данных\n3. Выход')
    print('___________________________')


def choice_menu():  # Запрос выбора
    while True:
        choice = input('Ваш выбор: ')
        if choice in ('1', '2', '3'):
            return choice
        print('Некорректный ввод. Введите одну из цифр - 1, 2 или 3')


# В функцию отправляются поименованные по ключу значения, возвращается СЛОВАРЬ (?)
def create_new_item(Name, Surname, Year_of_birth, City, email, pfone_num):
    return f"Name - {Name}, Surname - {Surname}, Year_of_birth - {Year_of_birth}," \
           f"City - {City}, email - {email}, Pfone_num - {pfone_num}"


# def create_new_item(**kwargs):
#     return ' '.join(kwargs. values())


def show_database(database):
    """
    Выводит заполненную базу данных - database, которая
    представляет собой СПИСОК, элементами которого
    являются пары СЛОВАРЯ код:значение, созданные
    в процессе выполнения функции create_new_item
    """
    for entry in database:
        print(entry)


def main():
    database = []
    while True:
        menu()
        choice = choice_menu()
        if choice == '1':
            params = {
                'Name': input('Введите имя - '),
                'Surname': input('Фамилию - '),
                'Year_of_birth': input('Год рождения - '),
                'City': input('Город проживания - '),
                'email': input('эл. почту - '),
                'pfone_num': input('Номер телефона')
            }
            database.append(create_new_item(**params))
        elif choice == '2':
            show_database(database)
        elif choice == '3':
            break


main()
