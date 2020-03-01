"""
3)	Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

def my_func(v1, v2, v3):
    my_list_1 = [v1, v2, v3]
    my_list_1.pop(my_list_1.index(min(my_list_1)))
    return print(sum(my_list_1))

my_func(1, 2, 3)


