# Программа первого домашнего задания

"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def get_data():
    data_list = []
    while True:
        data = input("Введите данные: ")
        if not data:
            break
        else:
            data_list.append(data)
    return data_list


def make_txt():
    with open("homework_1.txt", 'a') as text_file:
        for line in get_data():
            text_file.write(line +"\n")


make_txt()
