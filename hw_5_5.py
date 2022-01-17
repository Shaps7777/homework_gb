"""
Использование ф-ции map, где она применяет к каждому агументу свою созданную функцию
"""
def miles_to_kilometers(num_miles):
    """ Converts miles to the kilometers """
    return num_miles * 1.6


mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print(kilometer_distances)

# Аналогично с применением ф-ции lambda
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))

print(kilometer_distances)