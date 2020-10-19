# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [i for i in range(100, 1000) if i % 2 == 0]
#print(my_list)


def my_func(prev_i, i):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_i * i


print(reduce(my_func, my_list))

# print(reduce(lambda x,y: x * y, [i for i in range(100, 1000, 2)]))
