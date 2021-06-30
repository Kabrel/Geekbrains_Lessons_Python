# -*- coding: utf8 -*-
# Программа седьмого домашнего задания

"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json


def get_data():
    try:
        with open("homework_7.txt") as data_file:
            yield from (data for data in data_file.readlines())
    except FileNotFoundError:
        print("Файл 'homework_7.txt' не найден")
        return


def count_profit():
    negative_profit_company_dict = {}
    positive_profit_company_dict = {}
    for company_data in get_data():
        profit_val = int(company_data.split()[2]) - int(company_data.split()[3])
        if profit_val > 0:
            positive_profit_company_dict.setdefault(company_data.split()[0], profit_val)
        else:
            negative_profit_company_dict.setdefault(company_data.split()[0], profit_val)
    company_data_dict = {}
    company_data_dict.update(negative_profit_company_dict)
    company_data_dict.update(positive_profit_company_dict)
    all_profit = [positive_profit_company_dict.get(profit) for profit in positive_profit_company_dict]
    average_profit = {"average_profit": round(sum(all_profit) / len(positive_profit_company_dict))}
    return [company_data_dict, average_profit]


def write_json():
    with open("homework_7_result", "a") as json_file:
        json.dump(count_profit(), json_file)


write_json()
