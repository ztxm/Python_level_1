"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""
import sys

try:
    my_file = open("new file 6.txt", "r", encoding="utf-8")
    my_dict = {}
    for line in my_file.readlines():
        m = line.split(":")
        i = 0
        str_num = ""
        numbers = []
        for s in m[1]:
            if s.isdigit():
                i += 1
                #str_num += f"{s}"
                str_num += str(s)
            elif i > 0:
                numbers.append(int(str_num))
                str_num = ""
                i = 0
            else:
                i = 0

        my_dict.update({m[0]: sum(numbers)})

    print(f"Словарь: {my_dict}")

except OSError:
    print(f'Не возможно открыть файл {my_file.name}')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    my_file.close()



#проверка
print("\nВ файл было записано: ")
my_f = open("new file 6.txt", "r", encoding="utf-8")
content = my_f.read()
print(content)
