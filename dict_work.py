""" Работа со словарями
https://webdevblog.ru/kak-perebrat-slovar-v-python/
"""
##### a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

""" Получение КЛЮЧЕЙ
Создаем пустой список для дальнейшего заполнения его ключами
Достаем ключи из словаря и заполняем список
Кстати,  методы append(), extend() и insert() хорошо описаны здесь
https://andreyex.ru/programmirovanie/python/kak-dobavit-elementy-v-spisok-v-python-dobavit-rasshirit-i-vstavit/
"""
# key_list = []
# for key in a_dict:
#     key_list.append(key)
#     print(key)
# print(key_list)
# print(type(key_list))
# print(key_list[0])

""" Как достать ключи и значения
"""
# key_list = []
# value_list = []
# for key in a_dict:
#     print(key, ':', a_dict[key])
#     key_list.append(key)
#     value_list.append(a_dict[key])
# print(key_list)
# print(value_list)

""" Использование метода .items(), который возвращает новый вид элементов словаря
"""
# for item in a_dict.items():
#     print(item)
# print(type(item))

""" Метод keys() и values()
кстати
dict = {'Name': 'AndreyEx', 'Age': 187}
print ("Значение : %s" %  dict.keys())

dict = {'Sex': 'мужчина', 'Age': 18, 'Name': 'Андрей'}
print ("Значение : ",  list(dict.values()))
"""
# keys = a_dict.keys()
# print(keys)
# print(type(keys))
# print('_______________')
# keys_tuple = []
# for key in a_dict.keys():
#     print(key)
#     # print(key, ':', a_dict[key])
#     keys_tuple.append(key)
# print(keys_tuple)
# print(type(keys_tuple))
#
# print('_______________')
#
# value_tuple = []
# for value in a_dict.values():
#     print(value)
#     # print(key, ':', a_dict[key])
#     value_tuple.append(value)
# print(value_tuple)
# print(type(value_tuple))

""" Методы keys() и values() поддерживают тесты членства
(in) (membership tests (in)), 
что является важной функцией, если надо узнать, 
есть ли определенный элемент в словаре или нет:
"""
# print('pet' in a_dict.keys())

""" Изменение значений
"""
# prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for key, value in prices.items():
#     prices[key] = round(value * 0.9, 2)  # Apply a 10% discount
#     if key == 'apple':
#         prices[key] = round(value * 0.5, 2)
# print(prices)

""" УДАЛЕНИЕ ключа (очевидно, удаляется и значение)
"""
# prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for key in list(prices.keys()):  # Use a list instead of a view
#     if key == 'orange':
#         del prices[key]  # Delete a key from prices
# print(prices)

""" Почему нельзя напряму, например так (при ее выполнении выдается ошибка):
for key in prices.keys():
    if key == 'orange':
        del prices[key]
Потому что, это итерируемый объект (iterable), который 
возвращает элементы по одному в процессе выполнения процедуры
(выполнения последовательных инструкций, 
которая повторяется определенное количество раз или до выполнения указанного условия)
взятия элементов чего-то по очереди.
И если мы удалим элемент из очереди, то нарушим порядок выполнения процедуры - Error
"""

""" ПРЕВРАЩЕНИЕ ключей в значение
"""
# a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# new_dict = {}
# for key, value in a_dict.items():
#     new_dict[value] = key
# print(new_dict)
""" Превращение ключей в значение с использованием генератора (comprehensions) словарей
"""
# a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# new_dict = {value: key for key, value in a_dict.items()}
# print(new_dict)

""" ФИЛЬТРАЦИЯ
"""
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# new_dict = {}  # Create a new empty dictionary
# for key, value in a_dict.items():
#     if value <= 2:
#         new_dict[key] = value
# print(new_dict)
## C использованием генератора (comprehensions) словарей (вместо 4-х строк одна)
# a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# new_dict = {k: v for k, v in a_dict.items() if v <= 2}
# print(new_dict)

""" Расчеты
"""
# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# total_income = 0.00
# for value in incomes.values():
#     total_income += value  # Accumulate the values in total_income
# print(total_income)
# # C использованием генератора (comprehensions) словарей (вместо 3-х строк одна)
# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# total_income = sum([value for value in incomes.values()])
# print(total_income)
""" Если файл очень большой и надо экономить ПАМЯТЬ, то
можете использовать выражение-генератор (generator expression)
 вместо генератора списков. 
 Выражение-генератор — это выражение, которое возвращает итератор. 
 Это похоже на генератор списков, 
 но вместо квадратных скобок для его определения необходимо использовать круглые скобки:
"""
# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# total_income = sum(value for value in incomes.values())
# print(total_income)
# # """ Или еще проще"""
# total_income = sum(incomes.values())
# print(total_income)

"""УДАЛЕНИЕ выбранных элементов.
Есть словарь. Нужно создать новый с удаленными выбранными ключами. 
Объекты словаря похожи на sets (множества) и также поддерживают общие операции над множествами
(объединения, пересечения и различия /incomes.keys() - {'orange'}/.
"""
# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}
# print(non_citric)

""" Метод zip() - Функция zip() в Python создает итератор, 
который объединяет элементы из нескольких источников данных. 
Эта функция работает со списками, кортежами, множествами и словарями 
для создания списков или кортежей
"""
# print('______Вариант с формированием словаря_________')
# objects = ['blue', 'apple', 'dog']
# categories = ['color', 'fruit', 'pet']
# С использованием генератора (comprehensions)
# a_dict = {key: value for key, value in zip(categories, objects)}
# print(a_dict)
# print(type(a_dict))
#
# print('______Вариант с формированием списка_________')
# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
#
# zipped_values = zip(employee_names, employee_numbers)
# zipped_list = list(zipped_values)
# print(zipped_list)
# print(type(zipped_list))
# print('______Распаковка (zip со звездочкой)_________')
# employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
# employee_names, employee_numbers = zip(*employees_zipped)
#
# print(employee_names)
# print(employee_numbers)

""" СОРТИРОВКА словаря, МЕТОД sorted()
    по ключу
"""
# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# # с помощью генератора (comprehensions)
# sorted_income = {k: incomes[k] for k in sorted(incomes)}
# print(sorted_income)
# # или
# for key in sorted(incomes):
# или в обратном порядке
# for key in sorted(incomes, reverse=True):
#     print(key, ': ', incomes[key])

""" по значению
"""
# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
#
# def by_value(item):
#     return item[1]
#
# for k, v in sorted(incomes.items(), key=by_value):
#     print(k, ': ', v)
""" by_value() используется  для сортировки incomes по значению. 
Перебирается словарь в порядке сортировки, с использованием метода sorted(). 
Ключевая функция (by_value ()) сообщает sorted() отсортировать incomes.items() 
по второму элементу каждого элемента, то есть по значению (item [1]).
Как я это понял. Метод sorted() использует 2 аргумента - что сорировать (и здесь исходный словарь
но добавление items() видимо означает, что рассматриваются или не теряются значения словаря
т.е. мы работаем и с ключами, и с значениями) и по чему сортировать. И здесь встроенная (?) 
функция key, которая определяет, по чему сортировать. Т. к. она обращается к функции  by_value, 
а та использует item[1] (т. е. не [0]. что относится к ключам, а [1] - к значениям, 
то и сортировка производится по значению.
"""

""" Если ключи не нужны, то сортировку по значению можно сделать проще
"""
# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# for value in sorted(incomes.values()):
#     print(value)

"""Разрушительная итерация с помощью .popitem()
Иногда нужно перебрать словарь в Python и последовательно удалить его элементы. 
 .popitem() удалит и возвратит произвольную пару ключ-значение из словаря. 
 Когда вы вызываете .popitem() в пустом словаре, он вызывает ошибку KeyError.
"""
# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
#
# while True:
#     try:
#          print(f'Dictionary length: {len(a_dict)}')
#          item = a_dict.popitem()
#          # Do something with item here...
#          print(f'{item} removed')
#     except KeyError:
#          print('The dictionary has no item now...')
#          break

"""Ест еще ряд интересных методов работы со словарями, которые можно почитать здесь
https://webdevblog.ru/kak-perebrat-slovar-v-python/
"""