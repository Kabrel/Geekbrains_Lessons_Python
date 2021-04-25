# Программа второго домашнего задания

"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""

user_name = input("Введите имя пользователя: ")
user_soname = input("Введите фамилию пользователя: ")
user_year = input("Введите год рождения пользователя: ")
user_city = input("Введите город пользователя: ")
user_email = input("Введите e-mail пользователя: ")
user_tel = input("Введите телефон пользователя")


def get_user_data(name, soname, year, city, email, tel):
    """Функция вывода данных пользователя."""
    return [name, soname, year, city, email, tel]


print(get_user_data(name=user_name, soname=user_soname, year=user_year, city=user_city, email=user_email, tel=user_tel))
