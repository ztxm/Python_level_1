"""
1)	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Data():
    def __init__(self, param=0):
        self.param = param

    @staticmethod
    def check_digit(num):
        return True if num.isdigit() else False

    @staticmethod
    def check(num, dmy):
        num = int(num)
        if dmy == 0:
            if 0 < num <= 31:
                return num
            else:
                print(f"Ошибка: день должен быть от 1 до 31, а не {num} ")
                return 0
        elif dmy == 1:
            if 0 < num <= 12:
                return num
            else:
                print(f"Ошибка: месяц должен быть от 1 до 12, а не {num}")
                return 0
        elif dmy == 2:
            if 0 < num:
                return num
            else:
                print(f"Ошибка: {num} год должен быть больше 0")
                return 0
        else:
            return print(f"Не верный формат данных")

    @classmethod
    def get_data_2(cls, x):
        list_int = []
        [list_int.append(cls.check(el, i)) for i, el in enumerate(x.split("-")) if cls.check_digit(el) == True]
        return list_int if len(list_int) == 3 \
            else print(f"Ошибка, дата не должна содержать текст")

my_date = Data()
print(my_date.get_data_2("15-03-2020"))

my_date_2 = Data("25-11-2019")
print(my_date.get_data_2("17-11-2019"))