# -*- coding: utf8 -*-
# Программа четвертого домашнего задания

"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, max_speed, color, name, is_police):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = 0
        self._max_speed = max_speed

    def go(self, speed):
        if speed >= self._max_speed:
            self.speed = self._max_speed
        else:
            self.speed = speed
        return f"{self.name} going on"

    def stop(self):
        self.speed = 0
        return f"{self.name} stopping"

    def show_speed(self):
        return f"Скрость {self.name} = {self.speed}"

    @property
    def parameters(self):
        return f"{self.name} in color {self.color} and max speed = {self._max_speed}"

    @staticmethod
    def turn(self, left, right):
        if left:
            return f"{self.name} turned left"
        elif right:
            return f"{self.name} turned right"


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 60:
            return f"{self.name} превышает на {self.speed - 60}"
        else:
            return f"Скрость {self.name} = {self.speed}"


class SportCar(Car):
    ...


class WorkCar(Car):

    def show_speed(self):
        if self.speed >= 40:
            return f"{self.name} превышает на {self.speed - 60}"
        else:
            return f"Скрость {self.name} = {self.speed}"


class PoliceCar(Car):
    ...


police_car = PoliceCar(240, "blue white", "police car 001", True)
worker_car = WorkCar(100, "yellow", "tractor 001", False)
sport_car = SportCar(320, "red", "sport car 001", False)
town_car = TownCar(210, "black", "town car 001", False)

print(police_car.parameters)
print(worker_car.parameters)
print(sport_car.parameters)
print(town_car.parameters)

print(worker_car.go(120))
print(town_car.go(50))
print(worker_car.show_speed())
print(town_car.show_speed())
