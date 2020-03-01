"""
5)	Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
"""

def find_q(num_list, symbol="Q"): #функция возвращает первую позицию найденного элемента Q
    i = 0
    for el in num_list:
        #print(el.find(symbol))
        if el.find(symbol) >= 0:
           return i
        i += 1
    return -1

def sum_from_list(text_list): #функция счиает сумму из текстового списка
    new_list = []
    for el in text_list:
        new_list.append(int(el))
    return sum(new_list)

def sum_and_del_q(num_list, index_q): #функция удаляющая спец символ для выхода и отдающая сумму
    new_list = []

    i = 0
    while i < index_q:
        new_list.append(num_list[i])
        i += 1
    return sum_from_list(new_list)

all_sum = 0
pos = -1
while True:
    list_numbers = input('Введите введите целые числа через пробел, для выхода из программы добавьте "q", для продолжения "enter": ').upper().split()
    pos = find_q(list_numbers)
    if pos >= 0:
        all_sum = all_sum + sum_and_del_q(list_numbers, pos)
        break
    else:
        all_sum = all_sum + sum_from_list(list_numbers)

print(f"Сумма введеных значений = {all_sum}")
