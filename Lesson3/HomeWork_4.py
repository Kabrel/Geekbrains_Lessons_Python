# Программа четвертого домашнего задания

"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
"""

input_x = float(input("Введите действительное положительное число х: "))
input_y = int(input("Введите целое отрицательное число y: "))


def my_func(x, y):
    """Решение с помощью встроенной функции."""
    return x ** y


print(my_func(input_x, input_y))


def my_func_2(x, y):
    """ Решение с помощью цикла."""
    x_exp = x
    while y < -1:
        x_exp *= x
        y += 1
    result = 1/x_exp
    return result


print(my_func_2(input_x, input_y))
