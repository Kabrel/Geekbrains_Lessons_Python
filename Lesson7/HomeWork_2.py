# -*- coding: utf8 -*-
# Программа второго домашнего задания

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:

    def __init__(self, name, types, size=0, height=0):
        self.name = name
        self.size = size
        self.height = height
        self.type = types
        self.fabric = 0

    @property
    def count_fabric(self):
        if self.type == "coat":
            self.fabric = round(self.size / 6.5 + 0.5, 1)
            return self.fabric
        elif self.type == "suit":
            self.fabric = round(self.height * 2 + 0.3, 1)
            return self.fabric
        else:
            return None, "Тип одежды неизвестен"

    def sum_fabric(self):
        return coat.count_fabric + suit.count_fabric


coat = Clothes("Кашемир", "coat", size=42)
suit = Clothes("тройка", "suit", height=170)

print(coat.count_fabric, suit.count_fabric)
print(coat.sum_fabric())
