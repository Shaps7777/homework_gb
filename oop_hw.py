""" 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния
(красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
# Для начала, что делает ниже в основной программе \r (возврат каретки). Пример использования
# # _________________________________________________________________________

# from time import sleep
#
# status = 0
# while status <= 10:
#     print(f'\r{status}%', end='')
#     sleep(0.5)
#     status += 1

# # _________________________________________________________________________
# import time
# import itertools
#
#
# class Traffic:
#     __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]
#
#     def running(self):
#         for light in itertools.cycle(self.__color):
#             print(f"\r\033[{light[1][1]}m\33[1m{light[0]}\33[0m", end="")
#             time.sleep(light[1][0])
# # https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
#
# trf = Traffic()
# trf.running()

""" 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого 
для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта 
где масса одного кв метра дороги, покрытого асфальтом, определяется по ф-ле 25 кг х толщины полотна в см. 
Берем фиксированную толщину - 5 см. 
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

# class Road:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def get_full_mass(self):
#         return f'{self.length} м X {self.width} м X 25 кг X 5 см  = {(self.length * self.width * 25 * 5)/1000} тонн'
#
# road_mass = Road(5000, 20)
# print(road_mass.get_full_mass())

""" 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным 
и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных 
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self.wage = wage
#         self._income = {'profit': wage, "bonus": bonus}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return f"{self.name} {self.surname}"
#
#     def get_full_profit(self):
#         return f'{sum(self._income.values())}'
#
#
# manager = Position("Tom", "Cruse", "CEO", 50000, 20000)
# print(manager.get_full_name(), manager.position, manager.get_full_profit())

""" 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
 свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, 
выведите результат. Выполните вызов методов и также покажите результат.
"""


# class Car:
#     def __init__(self, name, color, speed, is_police=False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         self.is_police = is_police
#         print(f"Новый авто: {self.name}, цвет - {self.color}, полицейская - {self.is_police}")
#
#     def go(self):
#         print(f'{self.name} поехала')
#
#     def stop(self):
#         print(f'{self.name} остановилась')
#
#     def turn(self):
#         print(f"{self.name} повернула {'налево' if direction == 0 else 'направо'}")
#
#     def show_speed(self):
#         print(f'{self.name} скорость авто - {self.speed}')
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         return f"{self.name}: скорость авто - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!" \
#             if self.speed > 40 else f"{self.name}: скорость авто: {self.speed}"
#
#
# class SportCar(Car):
#     def show_speed(self):
#         return f"{self.name}: скорость авто - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!" \
#             if self.speed > 100 else f"{self.name}: скорость авто: {self.speed}"
#
#
# class PoliceCar(Car):
#     def __init__(self, name, color, speed, is_police=True):
#         super().__init__(name, color, speed, is_police)
#
#
# polise_car = PoliceCar('ДПС', 'Белый', 80)
# # print(polise_car.show_speed())
# # polise_car.go()
# work_car = WorkCar('Рабочая', 'Серый', 50)
# print(work_car.show_speed())
# sport_car = SportCar('Спортивная', 'Красный', 90)
# print(sport_car.show_speed())

""" 5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса 
Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать 
переопределение метода draw. Для каждого из классов методы должен выводить 
уникальное сообщение. Создать экземпляры классов и проверить, 
что выведет описанный метод для каждого экземпляра.
"""