# Программа пятого домашнего задания

"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def get_multiplication(element_1, element_2):
    return element_1 * element_2


data_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(get_multiplication, data_list))
