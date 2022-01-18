# Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title="Запуск отрисовки"):
        self.title = title

    def draw(self):
        print({self.title})


# Создание дочерних классов: Pen (ручка), Pencil (карандаш), Handle (маркер)
class Pen(Stationery):
    def draw(self):
        print(f"Начало отрисовки с помощью {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Начало отрисовки с помощью {self.title}")


class Marker(Stationery):
    def draw(self):
        print(f"Начало отрисовки с помощью {self.title}")


stat = Stationery()
pen = Pen("ручки")
pencil = Pencil("карандаша")
marker = Marker("маркера")

list1 = [stat, pen, pencil, marker]
# Проверка метода для каждого экземпляра
for i in list1:
    i.draw()
