"""
3)	Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""

import sys

my_data = []
list_salary = []
min_salary = []

try:
    my_file = open("my file 3.txt", "r", encoding="utf-8")
    for line in my_file.readlines():
        my_data = line.split()
        list_salary.append(float(my_data[1]))
        if list_salary[-1] <= 20000:
            min_salary.append(list_salary[-1])
            print(f"{my_data[0]} {list_salary[-1]:.2f}")
    print(f"Средняя величина дохода: {sum(min_salary) / len(min_salary):.2f}")
    print(f"Средняя величина дохода всех сотрудников: {sum(list_salary) / len(list_salary):.2f}")

except OSError:
    print(f"Не возможно открыть файл {my_file.name}")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    my_file.close()