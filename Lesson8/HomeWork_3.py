# -*- coding: utf8 -*-
# Программа третьего домашнего задания

"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class TypeCustomError(Exception):

    def __init__(self, txt):
        self.txt = txt


def get_list():
    result = []
    while True:
        data = input("Введите число. Для окончания ввода введите \"end\"")
        value = check_types(data)
        if type(value) is int:
            result.append(value)
        elif value == "end":
            return result


def check_types(data):
    try:
        if data.isdigit():
            return int(data)
        elif data == "end":
            return data
        else:
            raise TypeCustomError("Вводите только цифры или \"end\" для завершения программы")
    except TypeCustomError as err:
        print(err)


print(get_list())
