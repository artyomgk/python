# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(self, rows):
        return '\n'.join(['@' * rows for _ in range(self.num // rows)]) + '\n' + '@' * (self.num % rows)

    def __str__(self):
        return f"{self.num}"

    def __add__(self, other):
        print("Сумма - ")
        return Cell(self.num + other.num)

    def __sub__(self, other):
        print("Вычитание - ")
        return Cell(self.num - other.nums) if self.num - other.num > 0 else "Вычитание невозможно"

    def __mul__(self, other):
        print("Умножение - ")
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        print("Целочисленное деление - ")
        return Cell(self.num // other.num)


cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))