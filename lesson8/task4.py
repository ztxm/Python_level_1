"""
4)	Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5)	Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6)	Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.

"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def check_digit(self):
        if type(self) == int:
            return True
        else:
            return True if self.isdigit() else False

class Warehouse():
    count_on_wh = 0 #Кол-во товаров на складе

    def __init__(self, name, art, price, quantity, on_warehouse=False):
        self.name = name
        self.art = art
        self.price = price
        self.quantity = quantity
        self.on_warehouse = on_warehouse
        self.params = []

    def __str__(self):
        return f"Создан товар: {self.name}, Арт. {self.art}, Цена: {self.price} руб., Кол-во: {self.quantity}"

    def add_in_wh(self, num=1):
        try:
            if OwnError.check_digit(num) == False:
                raise OwnError("Ошибка, вводимые данные должны быть цифровыми, товар не добавлен на склад")
        except OwnError as err:
            return print(err)
        Warehouse.count_on_wh += num
        self.on_warehouse = True
        return print(f"Товар: \"{self.name}\" добавлен на склад - {num} шт.")

    def sending(self, num=1):
        try:
            if OwnError.check_digit(num) == False:
                raise OwnError("Ошибка, вводимые данные должны быть цифровыми")
        except OwnError as err:
            return print(err)
        if Warehouse.count_on_wh < 1:
            return print(f"Ошибка: На складе нет товаров")
        if self.quantity < num:
            return print(f"Ошибка: нельзя отправить больше товаров чем есть = {self.quantity}")
        else:
            Warehouse.count_on_wh -= num
            self.quantity -=num
            self.on_warehouse = False
            return print(f"Товар: \"{self.name}\" отправлен со склада - {num} шт.")

    def add_params(self, list_params):
        for el in list_params:
            self.params.append(el)

    @staticmethod
    def info_count():
        return Warehouse.count_on_wh

class Orgtechnique(Warehouse):
    def my_list(self):
        return self.options

class Printer(Orgtechnique):
    def __init__(self, *options):
        self.options = list(options)

class Scanner(Orgtechnique):
    def __init__(self, *options):
        self.options = list(options)

class Xerox(Orgtechnique):
    def __init__(self, *options):
        self.options = list(options)

t_1 = Warehouse("Принтер", 140500, 10000, 4)
print(t_1)
t_1.add_in_wh(4)

t_2 = Warehouse("Сканер", 120898, 4000, 2)
print(t_2)
t_2.add_in_wh(t_2.quantity)

p = Printer("Тип печати: черно-белая", "Максимальный формат: А4", "Максимальная нагрузка: 15000 страниц")
print(f"Параметры Класса Printer: \n{p.my_list()}")
t_1.add_params(p.my_list())
print(f"Передали параметры объекту с принтерами: \n{t_1.params}")
print()
print(f"Всего товаров на складе: {Warehouse.info_count()}")

