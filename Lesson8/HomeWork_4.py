# -*- coding: utf8 -*-
# Программа четвертого домашнего задания

"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:

    def __init__(self, count):
        self.count = count


class OfficeEquipment:

    def __init__(self, model):
        self.model = model


class Printer(OfficeEquipment):

    def __init__(self, print_type, model):
        super().__init__(model)
        self.print_type = print_type


class Scanner(OfficeEquipment):

    def __init__(self, scan_format, model):
        super().__init__(model)
        self.scan_format = scan_format


class Xerox(OfficeEquipment):

    def __init__(self, speed, model):
        super().__init__(model)
        self.speed = speed


printer = Printer("laser", "HP LaserJet 1505")
scanner = Scanner("A4", "HP Scan 854")
xerox = Xerox(450, "HP xerox 547")

print(printer.model)