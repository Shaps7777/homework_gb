goods = []
features = {'name': '', 'price': '', 'namber': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'namber': [], 'unit': []}
num = 0

while True:
    if input('Для выхода нажмите q, для продолжения Enter:  ') == 'q':
        break
    num += 1
    for f in features.keys():
        prop = input(f'Введите значение для {f} -')
        features[f] = int(prop) if f in ('price', 'namber') else prop
        analytics[f].append(features[f])
    goods.append((num, features.copy()))
    print((f'\nСтруктура товаров\n{goods}'))
    print(f"\nАналитика\n{'*' * 10}")
    for key, value in analytics.items():
        print(f"{key[:25]:>10}:{value}")

