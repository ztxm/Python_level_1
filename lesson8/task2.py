"""
2)	Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.

"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

number_1 = input("Ведите первое число ")
number_2 = input("Ведите второе число ")

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
    if number_2 == 0:
        raise OwnError("Ошибка, делить на ноль нельзя")
    print(f"Результат = {number_1 / number_2}")
except ValueError:
    print("Ошибка, должны быть введены только числа")
except OwnError as err:
    print(err)
