# -*- coding: utf8 -*-
# Программа третьего домашнего задания

"""
Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    @property
    def full_name(self):
        return f"{self.surname} {self.name}"

    @property
    def total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


director = Position("Alex", "Main", "director", 100000, 25000)

print(director.full_name)
print(director.total_income)
