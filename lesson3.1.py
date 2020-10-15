# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_1(n_1, n_2):
    try:
        sub = n_1 / n_2

    except ZeroDivisionError:
        return "Error делить на 0 нельзя!"
    except ValueError:
        return "Error!", "Ошибка числа"
    return sub


print(my_1(n_1=int(input("enter n_1: ")), n_2=int(input("enter n_2: "))))
