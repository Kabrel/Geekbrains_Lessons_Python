# -*- coding: utf8 -*-
# Программа пятого домашнего задания

"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random


def make_file():
    with open("homework_5.txt", "a") as new_file:
        for item in range(100):
            new_file.write(" ".join(str(random.randint(1, 100))))


def sum_data():
    with open("homework_5.txt") as data_file:
        num_list = [int(data) for data in data_file.read().split()]
        print(sum(num_list))


make_file()
sum_data()
