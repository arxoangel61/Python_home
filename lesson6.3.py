# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и
# ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, _wage=None, _bonus=None):
        self.name = name
        self.surname = surname
        self.position = position
        # self.income = income
        self._income = _wage + _bonus


class Position(Worker):
    def get_full_name(self):
        print(f"Данные сотрудника {self.name} {self.surname} Должность {self.position}")

    def get_total_income(self):
        print(f"Доход сотрудника {self.name} {self.surname} равен {self._income} \n")


a1 = Position("Vladimir", "Mikhaylov", "IT worker", _wage=70000, _bonus=10000)
a1.get_full_name()
a1.get_total_income()

a2 = Position("Ekatirina", "Mikhaylova", "Manager", _wage=27000, _bonus=5000)
a2.get_full_name()
a2.get_total_income()

a3 = Position("Nikita", "Samsonov", "Gamer", _wage=0, _bonus=25000)
a3.get_full_name()
a3.get_total_income()
