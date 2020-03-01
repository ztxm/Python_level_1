"""
5)	Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
произведения всех элементов списка. Подсказка: использовать функцию reduce().

"""
from random import randint
from functools import reduce

my_list = [el for el in [randint(100, 1000) for i in range(10)] if el % 2 == 0]
print(my_list)

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

print(f"Сумма всех произведений списка равна = {reduce(my_func, my_list)}")
