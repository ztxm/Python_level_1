"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

import sys

def no_symb(string): #функция удаления спец символов в строке
    symbols = [",", ".", chr(10)]
    for el in symbols:
        string = string.replace(el, "")
    return string


sum_lines = 0
sum_symbols = 0

try:
    my_file = open("my file 2.txt", "r", encoding="utf-8")
    for line in my_file.readlines():
        num_symb = len(no_symb(line).split())
        sum_symbols += num_symb
        sum_lines += 1
        print(f"{line.replace(chr(10), '')} --> слов: {num_symb}")
    print(f"\nВсего строк: {sum_lines}\nВсего слов: {sum_symbols}")

except OSError:
    print(f"Не возможно открыть файл {my_file.name}")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    my_file.close()