"""Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу."""


# Определяем функцию
def func_sum(*args):
    # Инициализируем переменную x
    x = 0
    while True:
        # Просьба пользователя ввести числа или выйти из программы
        list1 = input("Введи числа через пробел. (Для выхода из программы нажми q): ").split()
        # Цикл обработки условий
        for num in list1:
            # Специальный символ для выхода из программы в самом начале
            if num == 'q':
                return x
            else:
                try:
                    # Суммирование всех введенных значений
                    x += int(num)
                except ValueError:
                    # Вывод сообщения при неккоректном вводе значения
                    print("Введено некорректное входное значение. Вводить строго целые числа!")
        # Вывод результата
        print(f"Результат суммирования значений: {x}")


# Вызов функции
func_sum()
