# -*- coding: utf8 -*-
# Программа первого домашнего задания

"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Data:
    data = "dd-mm-yyyy"

    def __init__(self, data_string):
        Data.data = data_string

    @classmethod
    def get_data(cls):
        day = int(cls.data[:2])
        month = int(cls.data[3:5])
        year = int(cls.data[6:])
        return cls.check_data(day, month, year)

    @staticmethod
    def check_data(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year < 9999:
                    return day, month, year
                else:
                    return day, month, "invalid year value"
            else:
                return day, "invalid month value"
        else:
            return "invalid day value"


date_1 = Data("02-05-2021")

print(Data.get_data())
