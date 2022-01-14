# реализация менеджера как "скрипт с параметрами"
# Чтобы получить параметры скрипта мы должны импортировать модуль sys
# И переменная sys argv будет параметром скрипта
# Первый параметр скрипта будет ноль - текущий файл, второй - команда
import sys
from file_men_1 import create_file, create_folder, get_list_f_dir, get_list_dir, delete_file_or_dir, copy_file_or_dir, \
    save_info, change_dir, game_namber

save_info('Старт')
# Это команда: копировать, создать, удалить, пр.
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо ввести команду help')
else:
    # В зависимости от команды - действия
    if command == 'list_f_dir':
        get_list_f_dir()
    elif command == 'list_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Добавьте 2-й параметр - True')
        else:
            get_list_dir(name)
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Нет 2-го параметра: имени создаваемого файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Нет 2-го параметра: имени создаваемой директории')
        else:
            create_folder(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Недостаточно введено параметров')
        else:
            copy_file_or_dir(name, new_name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Нет 2-го параметра: имени удаляемого файла/директории')
        else:
            delete_file_or_dir(name)
    elif command == 'ch_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        else:
            change_dir(name)
    elif command == 'game':
        game_namber()

    elif command == 'help':
        print('\n Подсказка:\n list_f_dir - список файлов и директорий в текущей папке; \n',
              'list_dir + "True" - список директорий в текущей папке; \n',
              'create_file + "name" - создание нового файла с именем name;\n',
              'create_folder + "name" - создание новой папки с именем name;\n',
              'delete + "name" - удаление папки или файла с именем name;\n',
              'copy + "name" + "name_2" - копирование папки/файла с именем'
              ' name в создаваемую папку/файл с именени name_2.\n',
              'ch_dir - перейти в дочернюю директорию\n',
              'game - поиграть \n')

    save_info('Финиш')
