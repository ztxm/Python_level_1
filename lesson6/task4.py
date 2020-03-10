"""
4)	Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""

class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} Машина поехала"

    def stop(self):
        return f"{self.name} Машина остановилась"

    def turn(self, direction):
        if direction == "left":
            return "повернула на лево"
        if direction == "right":
            return "повернула на право"

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Вы превысили скорость на {self.speed - 60}"
        return self.speed

class SportCar(Car):
    """dsf"""

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Вы превысили скорость на {self.speed - 40}"
        return self.speed

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


my_car = Car(60, "silver", "Mazda")
my_town_car = TownCar(45, "black", "Volvo")
my_sport_car = SportCar(100, "Red", "Ferrari")
my_work_car = WorkCar(50, "white", "Gaz")
my_police_car = PoliceCar(0, "white", "Ford")

print(f"{my_car.name} {my_car.color}")
print(f"{my_town_car.name} {my_town_car.color} {my_town_car.is_police}")
print(f"{my_sport_car.name} {my_sport_car.color} {my_sport_car.turn('left')}")
my_sport_car.speed = 150
print(my_sport_car.go())
print(f"{my_sport_car.name} Скрость: {my_sport_car.show_speed()} км/ч")
print(my_sport_car.stop())
my_town_car.speed = 80
print(f"\n{my_town_car.name} {my_town_car.show_speed()} км/ч")
my_work_car.speed = 70
print(f"{my_work_car.name} {my_work_car.show_speed()} км/ч")


