"""
Какова логика. Создается базовый класс в котором прописываются атрибуты
которыми наделяются все объекты.
Далее создается дополнительный класс, который ссылается на базовый и тогда участники
этого дополнительного класса НАСЛЕДУЮТ все атрибуты базового класса.
В дополнительном же прописываются лишь те атрибуты, которые относятся
к объектам дополнительного класса.
"""
# class Auto:
#     auto_count = 0
#
#     # Класс определяет свои методы, например
#     # метод __init__ - это и констуктор и инициализатор
#     def __init__(self, name, color):
#         # атрибуты уровня объекта
#         self.name = name
#         self.color = color
#         self.start_engine()
#         Auto.auto_count +=1
#     # Еще один метод
#     def start_engine(self):
#         print(f'{self.name} - на конвейер')
#
# ferrari = Auto('Феррари', 'красный')
# print(ferrari.name, ferrari.color)
# print(f'Количество авто: {Auto.auto_count}')
# print(f'Количество авто: {ferrari.auto_count}')
#
# zaz = Auto('Запорожец', 'синий')
# print(zaz.name, zaz.color)
# print(f'Количество авто: {Auto.auto_count}')
# print(f'Количество авто: {zaz.auto_count}')
# print(f'Количество авто: {ferrari.auto_count}')

"""Пишем игру
"""
class Unit:
    # инициализация: имя, здоровье, угроза, броня персонажей игры
    def __init__(self, name, hp, dmg, armor):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.armor = armor

    # Создадим метод (атака и по конкретной target)
    def attack(self, target):
        target_dmg = self.dmg - target.armor
        if target_dmg > 0:
            print(f'{self.name} наносит урон {target.name}, в результате {target.name} теряет здоровье на: {target_dmg}')
            target.hp -= target_dmg
        else:
            print(f'{self.name} не пробивает броню {target.name}')

    def __add__(self, other):
        return (f'{self.name} обнимает {other.name}')

# Передаем значения атрибутам класса конкретного игрока
orche = Unit('Орк', 120, 25, 15)
elf = Unit('Эльф', 90, 20, 5)
# Атакуем
orche.attack(elf)
print(f'остается: {elf.hp}')

# А вот НАСЛЕДОВАНИЕ
class Dragon(Unit):
    def fly(self):
        print(f'{self.name} летит')
    def fire_breath(self):
        print(f'{self.name} дышит огнем')
    # А вот и полиморфизм, т. е. мы переопределяем для дракона функцию атаки
    def attack(self, target):
        print(f'{self.name} атакует огнем')
    def __init__(self, name, hp, dmg, armor, fly_speed = 20):
        Unit.__init__(self, name, hp, dmg, armor)
        self.fly_speed = fly_speed
""" Но вот захотелось добавить дракону новый атрибут - скорость полета. Что делать? 
Не переписывать же класс Unit. ?
 Выходим из положения следующим образом.
"""
gorynych = Dragon('Горыныч', 1000, 80, 100)
# Атакуем
gorynych.attack(orche)
print(f'остается: {orche.hp}')
gorynych.fly()
# Еще один класс "наследников", ведьма
class Witch(Unit):
    def fly(self):
        print(f'{self.name} летит на метле')
    def witchcraft(self):
        print(f'{self.name} колдует')
yaga = Witch('Баба Яга', 90, 20, 5)
yaga.fly()
yaga.witchcraft()

# Создаем класс гибрида дракона и ведьмы
class Dw(Witch, Dragon):
    def rid(self):
        print(f'{self.name} освобождает')
drwitch = Dw('Королева драконов', 120, 25, 14)

drwitch.fly()

army = [orche, elf, gorynych, drwitch, yaga]
for unit in army:
    unit.attack(elf)

""" Что такое переопределение метода/
напимер, мы хотим "провернуть" следующую операцию
print(elf+yaga). Программа выдаст ошибку. То есть, операции с классами не поддерживаю такой метод. 
Тогда мы поступаем так. В классе Unit прописываем
def __add__(self, other):
    return(f'{self.name} обнимает {other.name}'
То есть, мы переопределили как срабатывать оператору "+" в классе Unit и все заработало. 
"""
print(elf+yaga)
