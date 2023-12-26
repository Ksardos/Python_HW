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
class Autobus(Transport):

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def __str__(self):
        return "Марка: " + self.name + " Макс. скорость: " + str(self.max_speed) + " Пробег: " + str(
            self.mileage) + " Вместимость: " + str(self.capacity)

    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


autobus = Autobus("Renault Logan", 180, 12)
print(autobus.seating_capacity())
