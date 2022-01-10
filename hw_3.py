def show_menu():
    """
    Меню
    """
    print('_____Menu_____')
    print('1.Input date\n2. Output date\n3. Out')
    print('______________')


def choice_menu():
    """
     Запрашивает у пользователя выбор п. меню
     """
    while True:
        choice = input('You choice: ')
        if choice in ('1', '2', '3'):
            return choice
        print('Введите корректные данные')


def create_new_item(config):
    """
    Запрашивает у пользователя ввод данных и
    возвращает их в виде СЛОВАРЯ, где ключ -
    слово из config (т.е. Название товара, Цена, К-во),
    а значение - введенные пользователем данные.
    """
    entry = {}
    for field in config:
        entry[field] = input(f'Введите {field}: ')
    return entry


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
    config = ('Название товара', 'Цена', 'К-во')
    while True:
        show_menu()
        choice = choice_menu()
        if choice == '1':
            database.append(create_new_item(config))
            # Результатом этой операции будет
            # передача в функцию create_new_item
            # КОРТЕЖ config, а функция возвратит
            # СЛОВАРЬ, который добавится в СПИСОК
            # datebase (в словаре field
            # являются ключами полей ("Название товара",
            # "Цена", "К-во")
        elif choice == '2':
            show_database(database)
        elif choice == '3':
            break

main()
