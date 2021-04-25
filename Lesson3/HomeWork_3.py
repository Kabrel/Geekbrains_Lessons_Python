# Программа третьего домашнего задания

"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""

user_input_1 = int(input("Число 1 = "))
user_input_2 = int(input("Число 2 = "))
user_input_3 = int(input("Число 3 = "))


def my_func(*inputs):
    inputs_list = []
    num_sum = 0
    for i in inputs:
        inputs_list.append(i)
    for args in range(2):
        max_num = max(inputs_list)
        num_sum += max_num
        inputs_list.remove(max_num)
    return num_sum


print(my_func(user_input_1, user_input_2, user_input_3))
