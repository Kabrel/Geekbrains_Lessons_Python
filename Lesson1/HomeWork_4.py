# Программа четвертого домашнего задания

input_int = int(input("Введите целое положительное число: "))
result_num = 0


if input_int <= 0:  # Проверка на знание определения положительного числа
    print("Вы ввели неверное число")

else:
    while input_int > 10:  # Проверяем число по символьно
        current_num = input_int % 10
        input_int //= 10
        if current_num > result_num:  # Запоминаем самое большое число
            result_num = current_num
    print(f"Самое большое число {result_num}")
