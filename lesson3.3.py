# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(n_1, n_2, n_3):
    a = min(n_1, n_2, n_3)
    b = n_1 + n_2 + n_3
    b = b - a
    return b


print(my_func(10, 20, 30))


def my_func2(k_1, k_2, k_3):
    try:
        my_list = [k_1, k_2, k_3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return "Неправильное число"


print(my_func2(10, 20, 30))
