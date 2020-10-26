# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class road_info(Road):  # weight_m - масса , thickness - толщина
    def __init__(self, _length, _width, weight_m, thickness):
        super().__init__(_length, _width)
        self.weight_m = weight_m
        self.thickness = thickness

    def get_r_p(self):
        print("Масса асфальта, необходимого для покрытия всего дорожного полотна равна: ")
        return self._length * self._width * self.weight_m * self.thickness / 1000


r1 = road_info(20, 5000, 25, 5)
print(r1.get_r_p())
