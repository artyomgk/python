# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class myZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data_1 = input("Введите числитель: ")
inp_data_2 = input("Введите знаменатель: ")

try:
    inp_data_1 = int(inp_data_1)
    inp_data_2 = int(inp_data_2)
    if inp_data_2 == 0:
        raise myZeroDivisionError("Деление на ноль запрещено!")
except ValueError:
    print("Вы ввели не число")
except myZeroDivisionError as err:
    print(err)
else:
    print(f"Результат деления равен: {inp_data_1 / inp_data_2}")
