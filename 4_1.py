# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv
script_name, time_work, rate_hour, bonus = argv

print("Выработка в часах: ", time_work)
print("Ставка в час:", rate_hour)
print("Премия: ", bonus)

salary = (float(time_work) * float(rate_hour)) + float(bonus)

print(f"Ваша зарплата: {salary}")
