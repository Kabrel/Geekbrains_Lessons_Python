# Программа первого домашнего задания

"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, work_time, rate_hours, bonus = argv


def get_salary(hours, rate, bounty):
    salary = int(hours) * int(rate) + int(bounty)
    return salary


print(get_salary(work_time, rate_hours, bonus))
