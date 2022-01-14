import json
import pickle


my_favorite_group = {'name':'LZ',
                     'tracks': ['Kashmir', 'The song remain the same'],
                     'albums': [{'name': 'LZ1', 'year': 1969},
                                {'name': 'LZ2', 'year': 1970}]}
print(my_favorite_group)

# Приводим словарь к формату json
j_group = json.dumps(my_favorite_group)
print('json')
print(j_group)
print(type(j_group))

# Приводим словарь к формату pickle (2 вариант)
print('pickle')
p_group = pickle.dumps(my_favorite_group)
print(p_group)
print(type(p_group))

# Открываем файл (json)
with open('m_group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favorite_group, f)
# Открываем файл (pickle, запись байтами)
with open('m_group.pickle', 'wb') as f:
    pickle.dump(my_favorite_group, f)
