"""
1)	Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
https://r12a.github.io/app-conversion/
"""
import sys

try:
    my_file = open("test1.txt", "w")
    my_list = []
    print("Напишите текст, чтобы выйти оставьте пустую строку и нажмитие Enter: ")

    while True:
        string = input()
        my_list.append(f'{string.replace(chr(10), chr(92) + chr(110))}\n')
        if not string:
            my_file.writelines(my_list[:-1])
            print("Данные были сохранены в файле test1.txt")
            break

except OSError:
    print(f'Не возможно открыть файл {my_file.name}')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    my_file.close()

#проверка
print("В файл было записано: ")
my_f = open("test1.txt", "r")
content = my_f.read()
print(content)
my_f.close()
