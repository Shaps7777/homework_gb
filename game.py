import random

input('Задумайте число от 1 до 100, компьютер будет угадывать, после нажмите Enter')
count = 0
min_namber = 1
max_namber = 100
result = None
while result != '=':
    namber = random.randint(min_namber, max_namber)
    print('Это ', namber, '?')
    count += 1
    result = input('если да, то введите = , если больше - > , если меньше - < ')
    if result == '>':
        min_namber = namber + 1
    elif result == '<':
        max_namber = namber - 1
print(f'Угадано c {count} попытки')
