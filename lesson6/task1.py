"""
1)	Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
 — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

"""

import time
from itertools import cycle

class TrafficLight():
    def __init__(self, l_color="red"):
        self.__color = l_color

    def running(self):
        timing = {"red": [7, "Красный", "\x1b[6;30;41m"],
                  "yellow": [2, "Желтый", "\x1b[6;30;43m"],
                  "green": [7, "Зеленый", "\x1b[6;30;42m"],
                  "yellow2": [2, "Желтый", "\x1b[6;30;43m"]}

        #проверка
        err = 0
        past = 0
        my_list = []
        [my_list.append(el) for el in timing]
        my_list.append(my_list[0])
        for el in my_list:
            if (el == "red" or el == "green") and (past == "red" or past == "green"):
                print(f"Ошибка: Нарушен порядок: {el} -> {past}")
                err = 1
                break
            past = el

        t_cycle = cycle(timing.items())
        find = False
        while True:
            if err == 1:
                break
            it = iter(t_cycle)
            v = next(it)
            if v[0] == self.__color and find is False:
                find = True
            if find:
                print(f"\r{v[1][2]} {v[1][1]} \x1b[0m", end="")
                time.sleep(v[1][0])

s = TrafficLight("green")
s.running()
