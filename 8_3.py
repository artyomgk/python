# Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
# скрипт завершается, сформированный список с числами выводится на экран.

class Only_nums(Exception):
    def __init__(self, txt):
        self.txt = txt

    # Метод проверки вводного значения на число
    @staticmethod
    def is_digit(string):
        if string.isdigit():
            return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False

    # Определяем функцию
    def func_sum(*args):
        my_list = []
        while True:
            # Просьба пользователя ввести числа или выйти из программы
            list1 = input("Введи число. (Для выхода из программы введи stop): ").split()
            # Цикл обработки условий
            for num in list1:
                # Специальный символ для выхода из программы
                if num == 'stop':
                    print(f"Вот список твоих чисел - {my_list}")
                    return
                else:
                    try:
                        if not Only_nums.is_digit(num):
                            raise Only_nums("Введи число!")
                    except Only_nums as err:
                        print(err)
                    else:
                        my_list.append(num)


Only_nums.func_sum()
