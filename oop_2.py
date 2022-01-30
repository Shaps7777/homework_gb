class Auto:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    # *
    def __str__(self):
        return f'{self.name} with speed {self.speed}'

    # **
    def __add__(self, other):
        return Auto(self.name + other.name, self.speed + other.speed)

    # *** (отвечает за операцию взятия по индексу)
    def __getitem__(self, item):
        return item + ' а ты как думал?'

    # **** (срабатывет, когда мы атрибуту присваиваем какое то значение)
    def __setattr__(self, key, value):
        if key == 'speed' and value > 450:
            print('Скорость ограничена 450 км/ч')
            self.speed = 450
        else:
            self.__dict__[key] = value

    # ***** Оператор сравнения
    def __eq__(self, other):
        return self.speed == other.speed

# Что такое __dict__ это атрибут-словарь, в котором храняться все атрибуты объекта

ferrari = Auto('Феррари', 350)
uaz = Auto('Уаз', 180)
# zaz = Auto('Запорожец', 100)

# print(ferrari)               # См. *
# print(ferrari + uaz + zaz)   # См. **
# print(ferrari['ку-ку'])      # См. ***
ferrari.speed = 451            # См. **** (ferrari - это self, doors - это key, value - это 2)
print(ferrari.speed)
print(ferrari.__dict__)
ferrari.doors = 2  # Эквивалентная операция: ferrari.__dict__['doors'] = 2
print(ferrari.__dict__)
print(ferrari == uaz)           # См. *****

print(dir(ferrari))
