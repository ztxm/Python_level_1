"""
1)	Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

while True:
    try:
        script_name, work_time, salary_per_hour, bonus = argv
    except ValueError:
        print("Ошбика: все значения должны быть заполнены")
        break

    print(f"выработка в часах: {work_time}")
    print(f"ставка в час: {salary_per_hour}")
    print(f"премия: {bonus}")

    try:
        salary = (int(work_time) * int(salary_per_hour)) + int(bonus)
        print(f"Заработная плата сотрудника: {salary}")
        break
    except ValueError:
        print("Ошбика: значения должны быть цифровыми")
        break


