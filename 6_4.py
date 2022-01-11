# Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

from random import choice


class Car:
    direction = ["север", "запад", "юг", "восток"]

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"{color} автомобиль {name} полицеский? {is_police}")

    def go(self):
        print(f"{self.name} автомобиль поехал")

    def stop(self):
        print(f"{self.name} автомобиль остановился")

    def turn(self):
        print(f"{self.name} автомобиль повернул на {choice(self.direction)}")

    def speed_(self):
        return f"{self.name} автомобиль едет со скоростью {self.speed}"


class TownCar(Car):

    def speed_(self):
        return f"{self.name} скорость автомобиля - {self.speed}. Скорость превышена" if self.speed > 60 else super().speed_()


class WorkCar(Car):

    def speed_(self):
        return f"{self.name} скорость автомобиля - {self.speed}. Скорость превышена" if self.speed > 40 else super().speed_()

class SportCar(Car):
    """Спорткар"""


class PoliceCar(Car):
    """Полицейская машина"""

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)


police = PoliceCar('"Полицейская машина"', "черный", 80)
work = WorkCar("Рабочая машина", "синий", 40)
sport = SportCar("Спорткар", "красный", 150)
town = TownCar("Городская машина", "белый", 70)

list1 = [police, work, sport, town]

for i in list1:
    i.go()
    print(i.speed_())
    i.turn()
    i.stop()
    print()
