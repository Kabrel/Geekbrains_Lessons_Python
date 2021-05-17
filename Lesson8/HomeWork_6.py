# -*- coding: utf8 -*-
# Программа шестого домашнего задания

"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class ValidData(Exception):

    def __init__(self, txt):
        self.txt = txt


class Warehouse:

    def __init__(self):
        self.storage = {"printer": {"model": "count"},
                        "scanner": {"model": "count"},
                        "xerox": {"model": "count"}
                        }

    def get_equipment(self, equipment, count):
        try:
            if type(count) is not int:
                raise ValidData("Enter count as Integer")
            else:
                for tech_type, values in self.storage.items():
                    if tech_type == equipment.tech_type:
                        for model, amount in values.copy().items():
                            if model == equipment.model:
                                values[model] = amount + count
                                print(f"Added {model}. Actual count: {values[model]}")
                            else:
                                values.update({equipment.model: count})
                                print(f"Added {equipment.model}. Actual count: {count}")
        except ValidData as err:
            print(err)

    def send_equipment(self, company, equipment, count):
        for tech_type, value in self.storage.items():
            if tech_type == equipment.tech_type:
                for model, amount in value.copy().items():
                    if equipment.model == model:
                        if amount >= count:
                            value[model] = amount - count
                            print(f"{model} send to {company}, available {value[model]}")
                        else:
                            print(f"{amount} amount of {model} not enough")


class OfficeEquipment:

    def __init__(self, tech_type, model):
        self.model = model
        self.tech_type = tech_type


class Printer(OfficeEquipment):

    def __init__(self, print_type, model, tech_type):
        super().__init__(tech_type, model)
        self.print_type = print_type


class Scanner(OfficeEquipment):

    def __init__(self, scan_format, model, tech_type):
        super().__init__(tech_type, model)
        self.scan_format = scan_format


class Xerox(OfficeEquipment):

    def __init__(self, speed, model, tech_type):
        super().__init__(tech_type, model)
        self.speed = speed


printer = Printer("laser", "HP LaserJet 1505", "printer")
scanner = Scanner("A4", "HP Scan 854", "scanner")
xerox = Xerox(450, "HP xerox 547", "xerox")

warehouse = Warehouse()

warehouse.get_equipment(printer, "15")
warehouse.send_equipment("Apple", printer, 16)
