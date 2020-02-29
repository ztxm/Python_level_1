"""
2)	Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
 элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().
"""

#my_list = ["текст", 123, 5.67, None, True, False, {'123', 'dsfs'}, [1, 2, 3], ('a1','a2','a3')]
#my_list = ["текст", 123, 5.67, None, True, False, {'123', 'dsfs'}, [1, 2, 3]]
#my_list = ["текст"]
my_list = input("Введите несколько значений через пробел: ").split()
print(f"вы ввели: {my_list}")

new_list = []
i = 0
list_len = 0
is_odd = 0
pair = 1
for el in my_list: list_len += 1

if list_len > 1:
    if list_len % 2 != 0:
        is_odd += 1
        list_len -= 1

    #if  list_len > 3:
    while i <= list_len - 2:
        c = i % 2
        if i == 0:
            new_list.append(my_list[i + 1])
            new_list.append(my_list[i])
        if c == 1:
            new_list.append(my_list[i + 2])
            new_list.append(my_list[i + 1])
            pair += 1
        i += 1
    if is_odd > 0:
        new_list.append(my_list[pair * 2])

    #print(pair)
    print(f"новый список: {new_list}")
else:
    print("Ошибка: введите хотябы два значения")


"""
Грамотное решение:
while i + 1 < len(my_list):
    if i % 2 == 0:
        my_list.insert(i, my_list.pop(i + 1))
    i += 1
print(f"новый список: {new_list}")
"""
