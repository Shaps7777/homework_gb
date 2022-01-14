# is_has_name = True
# name = 'Max' if is_has_name else 'Empty'
# print(name)

# is_russian = True
# print('Привет' if is_russian else 'Hello')

# Перевод букв слова в различные регистры
# Прямой метод
# word = 'слово'
# result = []
# for i in range(len(word)):
#     if i%2 != 0:
#         letter = word[i].lower()
#     else:
#         letter = word[i].upper()
#     result.append(letter)
# result = ''.join(result)
# print(result)

# С помощью тернального оператора
# word = 'Термальный оператор'
# result = []
# for i in range(len(word)):
#     # или
#     # letter = word[i].lower() if i%2 != 0 else word[i].upper()
#     # или
#     letter = word[i]
#     letter = letter.lower() if i % 2 != 0 else letter.upper()
#
#     result.append(letter)
# result = ''.join(result)
# print(result)

# Проверка пароля
password = input('Введите пароль')
print('Доступ разрешен' if password == 'secret' else 'Вход запрещен')
