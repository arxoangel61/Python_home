# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
# желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __attr = ["Зеленый", "Желтый", "Красный", "Желтый"]

    def running(self):
        while True:
            print(f"{start._TrafficLight__attr[0]}")
            sleep(7)
            print(f"{start._TrafficLight__attr[1]}")
            sleep(2)
            print(f"{start._TrafficLight__attr[2]}")
            sleep(7)
            print(f"{start._TrafficLight__attr[3]}")
            sleep(2)


start = TrafficLight()
start.running()
print(start._TrafficLight__attr)
