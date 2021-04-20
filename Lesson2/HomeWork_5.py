# Программа пятого домашнего задания

"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]

new_element = int(input("Введите новый элемент рейтинга: "))

if new_element in my_list:
    position_index = my_list.index(new_element) + my_list.count(new_element)
    my_list.insert(position_index, new_element)
else:
    my_list.append(new_element)

print(my_list)
