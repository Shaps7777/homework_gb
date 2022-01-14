# Фильтр данных. Оставляются только совпадающие значения
# fruits1 = ['apple', 'banana', 'orange', 'kiwi', 'pear']
# fruits2 = ['banana', 'kiwi', 'tangerine']
#
# # Классический способ
# result = []
# for fruit in fruits1:
#     if fruit in fruits2:
#         result.append(fruit)
# print(result)
# # С помощью генератора
# result = [fruit for fruit in fruits1 if fruit in fruits2]
# print(result)
#
# # *********************************************************************************
# # Фильтр: только положительные числа, кратные 3 не кратные 4
# nambers = [1, 5, -9, 10, 27, 8, 17, 45, 100, 11, -7, 12, -27]
# namber = [namber for namber in nambers if namber > 0 and namber %3 == 0 and namber %4 != 0]
# print(namber)

# # *********************************************************************************
# # на вход подается список, из него создается список кв. корней исходных элементов
# # при этом исходный список должен быть сохранен
# import math
#
# old_list = [1, -1, 2, -2, 4, 5, 6, 7, 8, 9]
#
# Классический способ
# def new_list(input_list):
# # Если список не копировать, то старый список также изменится
#     input_list = input_list.copy()
#
#     for i in range(len(input_list)):
#         namber = input_list[i]
#         if namber > 0:
#             input_list[i] = math.sqrt(namber)
#     return input_list
# result = new_list(old_list)
# print(result)
# print(old_list)

# С помощью генератора
# def new_list(input_list):
#     result = [math.sqrt(namber) for namber in input_list if namber > 0]
#     return result
# result = new_list(old_list)
# print(result)
# print(old_list)
# Но, в новом списке пропали отрицательные числа. Используем тернальный оператор
# def new_list(input_list):
#     result = [math.sqrt(namber) if namber > 0 else namber for namber in input_list]
#     return result
# result = new_list(old_list)
# print(result)
# print(old_list)
# # *********************************************************************************
# Ввод числа, если 13 - это плохо, выход, остальные в квадрат
def bad_namber(namber):
    if namber == 13:
        raise ValueError('Ой!')
    else:
        return namber ** 2

namber = int(input('Введите число от 1 до 100  '))
# Обработка исключений, в ином случае программа "вылетет" если будет задано число 13.
try:
    result = bad_namber(namber)
except ValueError:
    print('Неудачный выбор')
else:
    print('Результат в квадрате =', result)
