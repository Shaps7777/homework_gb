# f = lambda a, b: a + b


# Что эквивалентно
# def f(a, b):
#    return a + b


# , т. е. в lambda передаются аргументы, далее ":",
# выражение, результат которого возвращается (return)
# print(f(10, 5))

# Вспомним функцию reduce
# from functools import reduce

data = [10, 20, 30, 40]
# Ее можно заменить на lambda
# def func(a, b):
#     return a+b
# print(reduce(lambda a, b: a + b, data))


# Вспомним функцию map
data = list(map(lambda x: int(x) ** 2, data))
print(data)
