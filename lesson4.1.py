# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

script_name, first_param, second_param, third_param = argv

print(argv)
print("Имя скрипта: ", script_name)
print("Выработка в часах: ", first_param)  # 9
print("Ставка в час: ", second_param)  # 150
print("Премия: ", third_param)  # 7000

a = int(first_param)
b = int(second_param)
c = int(third_param)
final = ((a * b) + c)
print("Ваша зарплата", final)
