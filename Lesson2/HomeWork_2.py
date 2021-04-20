# Программа второго домашнего задания

"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = []
list_elem_count = int(input("Введите кол-во элементов: "))

while list_elem_count > 0:
    my_list.append(str(input(f"Введите значение для списка. Осталось: {list_elem_count}. ")))
    list_elem_count -= 1

print(my_list)

for index in range(0, len(my_list)-1, 2):
    print(index)
    my_list[index], my_list[index+1] = my_list[index+1], my_list[index]

print(my_list)
