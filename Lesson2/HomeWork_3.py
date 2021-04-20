# Программа второго домашнего задания

"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# Решение через list

user_month = int(input("Введите месяц в виде целого числа: "))

calendar_list = ["зима", "весна", "лето", "осень"]

if 2 < user_month < 6:
    print(f"{user_month} относится к времени года: {calendar_list[1]}")
elif 5 < user_month < 9:
    print(f"{user_month} относится к времени года: {calendar_list[2]}")
elif 8 < user_month < 12:
    print(f"{user_month} относится к времени года: {calendar_list[3]}")
else:
    print(f"{user_month} относится к времени года: {calendar_list[0]}")

# Решение через dict

user_month = int(input("Введите месяц в виде целого числа: "))
calendar_dict = {"зима": [12, 1, 2],
                 "весна": [3, 4, 5],
                 "лето": [6, 7, 8],
                 "осень": [9, 10, 11]
                 }

for season_index, month_index in calendar_dict.items():
    if user_month in month_index:
        print(f"{user_month} относится к времени года: {season_index}")
