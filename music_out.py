import json
import pickle

# Открываем файл (json)
with open('m_group.json', 'r', encoding='utf-8') as f:
    resalt = json.load(f)
print(resalt)
print(type(resalt))

# Открываем файл (pickle, чтение байт)
with open('m_group.pickle', 'rb') as f:
    resalt = pickle.load(f)
print(resalt)
print(type(resalt))
