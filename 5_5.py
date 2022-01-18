# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

with open("test.txt", "w", encoding="utf-8") as f_obj:
    list1 = [randint(1, 10) for _ in range(10)]
    f_obj.write(" ".join(map(str, list1)))

print(f'Сумма случайного набора чисел - {sum(list1)}')
