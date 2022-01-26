"""
json - это  формат данных записанный определенным образом
(это не словарь!) для передачи даннных в интернете
Это стандарт. И если я обпащаюсь к данным сайта, то
получаю даные либо в формате html, либо в формате json
"""

import json

# Чтение данных из файла

# with open('data.json', 'r') as f:
#     data = json.load(f)
# print(type(data))
# print(data)
# print(f"Имя - {data['name']}, возраст - {data['age']}")

# Запись данных в формат json

data_2 = {
    'name': 'tv',
    'price': 50000,
    'contrast': '4000'
}
with open('data_2.json', 'w') as f:
    json.dump(data_2, f)
"""
Пример преобразования данных (без использования формата json)
Возьмем данные из другого файла (json_module_2.txt)
Которые структурированы, но имеют другой формат
и преобразуем их в формат словаря
"""

# with open('json_module_2.txt', 'r') as f:
#     data = f.read()
#     key_value = data.split('---')  # Разделяем по символу ---
#     print(key_value)  # Получаем список
#     data = {}  # Создаем пустой словарь

"""
    Проходим по списку и разносим данные на 
    ключ и значение  - key, value = elem.split('!!!')
    по разделителю и формируем словарь, присваивая 
    определенному ключу значение

"""
#     for elem in key_value:
#         key, value = elem.split('!!!')
#         print(key, value)
#         data[key] = value
#
# print(data)
