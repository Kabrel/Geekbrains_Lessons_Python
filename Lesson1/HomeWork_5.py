# Программа пятого домашнего задания

proceeds = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))

# Проверка прибыльности компании
if proceeds > costs:
    print("Ваша фирма прибыльна")
    profitability = proceeds - costs
    workers_count = int(input("Введите количество сотрудников фирмы: "))
    workers_profitability = profitability / workers_count  # Расчет прибыльности каждого сотрудника
    print(f"Ценность одного сотрудника составляет: {workers_profitability}")
elif proceeds < costs:
    print("Ваша фирма убыточна")
else:
    print("Ваша фирма работает в 0")
