# -*- coding: utf8 -*-
# Программа шестого домашнего задания

"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumbers:

    def __init__(self, number):
        self.expression = number.split()
        self.number_1 = self.expression[0]
        self.number_2 = self.expression[1] + self.expression[2][:-1]

    def __add__(self, other):
        return f"{int(self.number_1) + int(other.number_1)} + {int(self.number_2) + int(other.number_2)}i"

    def __mul__(self, other):
        return f"{(int(self.number_1) * int(other.number_1)) + abs(int(self.number_2) * int(other.number_2))} + " \
               f"{(int(self.number_1) * int(other.number_2)) + (int(self.number_2) * int(other.number_1))}i"


complex_1 = ComplexNumbers("2 + 3j")
complex_2 = ComplexNumbers("5 - 2j")

print(complex_1 + complex_2)
print(complex_1 * complex_2)
