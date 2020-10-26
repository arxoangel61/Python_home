# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen
# (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw.  Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def draw(self, title):
        self.title = title
        print(f"Начала отрисовки: {self.title}")


class Pen(Stationery):
    def draw(self, title):
        super().draw(title)
        print(f"Класс 1 активирован : {self.title} < Процесс начат! \n")


class Pencil(Stationery):
    def draw(self, title):
        super().draw(title)
        print(f"Класс 2 активирован : {self.title} < Процесс начат! \n")


class Handle(Stationery):
    def draw(self, title):
        super().draw(title)
        print(f"Класс 3 активирован : {self.title} < Процесс начат! \n")


a1 = Pen()
a1.draw("Ручка")

a2 = Pencil()
a2.draw("Карандаш")

a3 = Handle()
a3.draw("Маркер")
