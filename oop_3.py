from random import randint
from time import sleep

class User:

    def __init__(self, name, income):
        self.name = name
        self.__income = income
        self.__bill = 0
        self.__work_days = 0

    def get_income(self):
        self.__bill += self.__income

    def __grade_income(self):
        self.__income += 10000
        print('Повышение')
        self.__work_days = 0
    def go_to_work(self):
        self.__work_days += 1
        print('Идем на работу')

        if randint(0, 30) < self.__work_days:
            self.__grade_income()

    def get_bill(self):
        return self.__bill

ivan = User('Иван', 30000)
while True:
    ivan.go_to_work()
    print(ivan.get_bill())
    sleep(0.3)