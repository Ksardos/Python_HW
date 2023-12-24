# -*- coding: cp1251 -*-

# Задание 1
class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def info(self):
        return f"Название автомобиля: {self.name}. Скорость: {self.max_speed}. Пробег: {self.mileage}"

    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


autobus = Transport('Renaul Logan', '180', '12')
print(autobus.info())

# Задание 2
Autobus = Transport('Renaul Logan', '180', '12')
print(Autobus.seating_capacity())
