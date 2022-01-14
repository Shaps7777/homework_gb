s = 'abc' # аналогично для l = [1, 2, 3], d = {1:'a'} и т.д.
# Классический способ
# if len(s) != 0:
# Так лучше, используя байтовые выражения
if s:
    print('Not empty')
else:
    print('Empty')

l = [1, 2, 3]
d = {1:'a'}
if l and d:
    print('Not empty')
else:
    print('Empty')
