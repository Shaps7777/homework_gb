"""
Реализовать функцию int_func(), принимающую слова
 из маленьких ЛАТИНСКИХ (фокус здесь) букв и возвращающую его же,
 но с прописной первой буквой.
 Например, print(int_func(‘text’)) -> Text.
"""


def func_word(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
 #   return word.title() if not set(word).difference(latin_char) else False
    if set(word).difference(latin_char):
        print('Введите символы в латинице!')
    else:
        return word.title()
""" Здесь перечисляются все латинские буквы, 
которые сравниваются со всеми введенными буквами в переменной word.
Эта переменная word рассматривается как множество (set), которое
обладает свойством содержать символы без повторения. Если разница есть - 
(например, введены цифры или символы на кирилице), то difference возвращает 
True. Но нам эта True нежна когда разницы нет, поэтому применен 
оператор if NOT, соответсвенно, если разницы нет, тогда исполняется
процедура  return word.title()
"""

word = input('Введите слова в латинской раскладке разделенные пробелом: ').split()
for w in word:
    resalt = func_word(w)
    if resalt:
        print(func_word(w), ' ')
