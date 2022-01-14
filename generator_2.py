# Создать список из случайных чисел
import random
nambers = [random.randint(1, 100) for i in range(10)]
print(nambers)

# Создать список квадратов чисел
nambers = [1, 2, 3, -4]
nambers = [namber**2 for namber in nambers]
print(nambers)

# Фильтровать список по именам (выбор имен, начинающихся на А)
names = ['Руслан', 'Дмитрий', 'Алексей', 'Андрей']
names = [name for name in names if name.startswith('А')]
print(names)
