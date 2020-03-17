"""
3)	Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def check_digit(self):
        return True if self.isdigit() else False

number_list = []
print('Для выхода из программы введите "stop"')

while True:
    n = input("Введите целое число для добавления в список: ")
    if n.lower().find("stop") >= 0:
        break
    try:
        print(f"Вы ввели: {n}")
        if OwnError.check_digit(n) == False:
            raise OwnError("Ошибка, вводимые данные должны быть цифровыми")
        number_list.append(n)
    except OwnError as err:
        print(err)

print(f"Созданный список: {number_list}")
