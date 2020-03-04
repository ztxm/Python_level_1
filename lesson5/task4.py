"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

"""
import sys

my_data = []

def func_translate(string): #функция перевода
    words = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    for v in words.items():
        if string == v[0]:
            string = v[1]
    return string

try:
    my_file = open("my file 4.txt", "r", encoding="utf-8")
    for line in my_file.readlines():
        m = line.split()
        m[0] = func_translate(m[0])
        m = f'{" ".join(m)}\n'
        my_data.append(m)
        #print(m)

    new_file = open("new file 4.txt", "w", encoding="utf-8")
    new_file.writelines(my_data)

except OSError:
    print(f'Не возможно открыть файл {my_file.name}')
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    my_file.close()
    new_file.close()


#проверка
print("В файл было записано: ")
my_f = open("new file 4.txt", "r", encoding="utf-8")
content = my_f.read()
print(content)
my_f.close()
