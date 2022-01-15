def mosinka(*ammo):
    for bullet in ammo:
        yield bullet
        # yield 'перезарядка'
        print('перезарядка')


gan = mosinka('обычный патрон', 'бронебойный патрон')
for i in gan:
    print(i)
# print(next(gan))
# print(next(gan))
# print(next(gan))
# print(next(gan))



# print(gan)
# for boom in gan:
#     print(boom)
