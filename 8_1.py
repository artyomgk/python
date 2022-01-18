# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Data:
    data = []

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set(cls, data1):
        Data.data = input(f"Введи дату в формате день-месяц-год: ").split('-')
        d = int(Data.data[0])
        m = int(Data.data[1])
        y = int(Data.data[2])
        return cls(d, m, y)

    # Валидация месяца
    @staticmethod
    def validation_month(obj):
        if 0 < obj.month < 12:
            print("Месяц принят")
        else:
            print("Неправильный ввод месяца")

    # Валидация дня
    @staticmethod
    def validation_day(obj):
        # Создаем списки месяцев с одинаковыми числами в 2022 году
        list1 = [1, 3, 5, 7, 8, 10, 12]
        list2 = [4, 6, 9, 11]
        list3 = [2]
        # Проверка первого списка месяцев
        for mon in list1:
            if obj.month == mon:
                if 1 <= obj.day <= 31:
                    print("Число принято")
                else:
                    print("Такого числа нет")
        # Проверка второго списка месяцев
        for mon in list2:
            if obj.month == mon:
                if 1 <= obj.day <= 30:
                    print("Число принято")
                else:
                    print("Такого числа нет")
        # Проверка третьего списка месяцев
        for mon in list3:
            if obj.month == mon:
                if 1 <= obj.day <= 28:
                    print("Число принято")
                else:
                    print("Такого числа нет")

    # Валидация года
    @staticmethod
    def validation_year(obj):
        if 0 <= obj.year <= 2022:
            print("Год принят")
        else:
            print("В будущее не стоит смотреть")


x = Data.set(Data.data)
Data.validation_day(x), Data.validation_month(x), Data.validation_year(x)
