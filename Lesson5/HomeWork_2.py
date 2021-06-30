# Программа второго домашнего задания

"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
Используется файл из первого домашнего задания.
"""


def get_txt_info():
    try:
        with open("homework_1.txt") as data_file:
            lines_count = sum(line.count("\n") for line in data_file.read())
            print(f"Количество строк в тексте: {lines_count}")
            data_file.seek(0)
            for index, line in enumerate(data_file.readlines(), start=1):
                words_per_line_count = (index, len(line.split()))
                print(f"В строке {words_per_line_count[0]} количество слов: {words_per_line_count[1]}")
    except FileNotFoundError:
        print("Запустите первое домашнее задание, для создания файла.")


get_txt_info()
