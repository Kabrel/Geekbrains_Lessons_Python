# -*- coding: utf8 -*-
# Программа второго домашнего задания

"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_weight(self, depth, weight):
        return f"{(self.__length * self.__width * depth * weight)//1000} Т"


main_road = Road(5000, 20)

print(main_road.calc_weight(5, 25))
