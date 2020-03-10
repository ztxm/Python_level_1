"""
5)	Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""

class Stationery():
    def __init__(self, title="что-то"):
        self.title = title

    def draw(self):
        return print(f"Запуск отрисовки {self.title}")

class Pen(Stationery):
    """Ручка"""
    def draw(self):
        return print(f"Рисуем ручкой {self.title}")

class Pencil(Stationery):
    """Карандаш"""
    def draw(self):
        return print(f"Рисуем карандашем {self.title}")

class Handle(Stationery):
    """Маркер"""
    def draw(self):
        return print(f"Рисуем маркером {self.title}")


my_draw = Stationery()
my_draw.draw()
print()
pen = Pen("Макет")
pen.draw()
pic = Pencil("Картина")
pic.draw()
coloring = Handle("Раскраска")
coloring.draw()
