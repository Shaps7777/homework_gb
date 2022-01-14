# person = {'name': 'Max', 'phones': [967, 916]}
# with open('person.dat', 'wb') as f:
#     name = person['name']
#     f.write(f'{name}\n'.encode('utf-8'))
#     phones = person['phones']
#     for phone in phones:
#         f.write(f'{phone}\n'.encode('utf-8'))
# print('Персона зарегистрирована')
with open('person.dat', 'rb') as f:
    result = f.readlines()
person = {}
person['name'] = result[0].decode('utf-8').replace('\n', '')
phones = []
for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))
person['phones'] = phones
print(person)
