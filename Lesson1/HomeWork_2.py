# Программа второго домашнего задания

seconds_input = int(input("Введите количество секунд, на которое поставить таймер: "))

seconds = seconds_input % 60
minutes = seconds_input // 60 % 60
hours = seconds_input // 3600

print(f"Таймер установлен на: {hours}ч.:{minutes}м.:{seconds}с.")  # Вывод значения таймера
