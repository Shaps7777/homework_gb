""" Это функция высшего порядка
Здесь функция call_func принимает в качестве аргументов
функцию func - call_func(func), которую сама вызывает.
Получается, что вызвав call_func мы получаем кортеж или
 требование передачи 2-х аргументов (?) в
виде return f(10, 5), и эти 2 аргумента передаются в
func, которая с ними работает и возвращает результат
"""


def func(a, b):
    return a + b


def call_func(f):
    return f(10, 5)


print(call_func(func))

# Встроенные функции высшего порядка


data = ['1', '2', '3', '4']
# Функция map (применяет к каждому элементу float, int, и т.д.)
int_data = list(map(float, data))
print(int_data)

# Функция map, реализованная вручную
def my_map(func, data):
    resalt = []
    for el in data:
        resalt.append(func(el))
    return resalt


print(my_map(int, data))
