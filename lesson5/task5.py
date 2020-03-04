"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import sys
from random import randint

try:
    new_file = open("new file 5.txt", "w", encoding="utf-8")
    my_list = [el for el in [randint(1, 10) for i in range(5)]]
    new_file.writelines(" ".join(str(el) for el in my_list))
    new_file.close()

    my_file = open("new file 5.txt", "r", encoding="utf-8")
    line = my_file.readline().split(" ")
    print(f"Сумма: {sum([int(el) for el in line])}")

except OSError:
    print(f'Не возможно открыть файл {new_file.name}')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    my_file.close()



#проверка
print("В файл было записано: ")
my_f = open("new file 5.txt", "r", encoding="utf-8")
content = my_f.read()
print(content)
