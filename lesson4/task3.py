"""
3)	Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
from random import randint

print([el for el in [randint(20, 239) for i in range(100)] if el % 20 == 0 or el % 21 == 0])