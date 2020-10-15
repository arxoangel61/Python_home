# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_func(**kwargs):
    return kwargs


a = my_func(name="Vladimir", lastname="Mikhailov", bitrday=1987, city="Rostov", email="forv1p10@gmail.com",
            phone=89281765616)

for key, value in a.items():
    print(f"{key} : {value}")
