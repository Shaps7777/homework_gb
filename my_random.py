from random import randint, randrange, random, choice

# random генерирует дробные числа от 0 до 1, НЕ ВКЛЮЧАЯ 1
# print(random())

# randint генерирует целые числа в указанном д-не, ВКЛЮЧАЯ крайние числа
# print(randint(0, 5))

# randrange генерирует целые числа в д-не до 10 (НЕ ВКЛЮЧАЯ 10)
# print(randrange(10))
# randrange генерирует целые числа в д-не от -5 до 10 (НЕ ВКЛЮЧАЯ 10)
# print(randrange(-5, 10))
# randrange генерирует в д-не с шагом
# print(randrange(-5, 10, 2))

# choice выбирает элемент из списка случайным образом
a = [10,'Hello', 333.23]
print(choice(a))