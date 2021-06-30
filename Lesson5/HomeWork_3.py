# Программа третьего домашнего задания

"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 2 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def get_salary():
    with open("homework_3.txt") as salary_data:
        workers_salary = []
        low_price_workers = []
        for line in salary_data.readlines():
            line = line.strip().split("|")
            print(f"Сотрудник {line[0].strip()} c зарплатой {line[1]}")
            workers_salary.append(line)
        for worker, salary in workers_salary:
            if int(float(salary)) < 2000:
                low_price_workers.append(worker.strip())
        all_salary = [int(float(salary[1].strip())) for salary in workers_salary]
        print("Средний доход сотрудников:", round(sum(all_salary) / len(workers_salary)))
        print(f"Список сотрудников с окладом менее 2 тыс.: {str(low_price_workers)[1:-1]}")


get_salary()
