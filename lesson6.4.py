# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте
# в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина поехала! {self.name}")

    def stop(self):
        print(f"Машина остановилась {self.name}")

    def turn(self):
        print(f"Машина повернула {self.name}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.show_speed = 60
        if self.speed > self.show_speed:
            print(
                f"Ваша скорость: {self.speed} км/ч <<Внимание! Ваша скорость привышена!>> \n {self.name} - {self.color}"
                f": Разрешенная скорость {self.show_speed} км/ч")
        else:
            print(f"Ваша скорость: {self.speed}, Модель: {self.name}, Цвет: {self.color} ")

class SportCar(Car):
    def __init__(self, speed, color, name, show_speed, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.show_speed = show_speed
        print(f"Ваша скорость: {self.speed}, Модель: {self.name}, Цвет: {self.color} ")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.show_speed = 40
        if self.speed > self.show_speed:
            print(
                f"Ваша скорость: {self.speed} км/ч <<Внимание! Ваша скорость привышена!>> \n {self.name} - {self.color}"
                f": Разрешенная скорость {self.show_speed} км/ч ")
        else:
            print(f"Ваша скорость: {self.speed}, Модель: {self.name}, Цвет: {self.color} ")


class PoliceCar(Car):
    def __init__(self, speed, color, name, show_speed, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.show_speed = show_speed
        print(f"Ваша скорость: {self.speed}, Модель: {self.name}, Цвет: {self.color} ")


avto_1 = TownCar(100, "White", "Toyota Rav4", True)
avto_1.go()
avto_1.stop()
avto_1.turn()

avto_2 = TownCar(50, "Black", "Niva 4x4", True)
avto_2.go()
avto_2.stop()
avto_2.turn()

avto_3 = WorkCar(120, "Red", "Honda Accord", True)
avto_3.go()
avto_3.stop()
avto_3.turn()

avto_4 = PoliceCar(250, "Black Mamba", "Bat Mobile", True)
avto_4.go()

avto_5 = SportCar(220, "Blue", "Ferrari", True)
avto_5.turn()