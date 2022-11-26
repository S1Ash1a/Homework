'''Напишите программу с классом Car. Создайте конструктор (__init__) класса Car.
Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
Напишите три метода для этого класса. Первый — запуск автомобиля,
при его вызове выводится сообщение «Автомобиль заведен».
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
Третий - магический метод str  для вывода атрибутов экземпляра в виде строки.'''

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def sayHi(self):
        print("Автомобиль заведен " + self.type)

    def stop(self):
        print("Автомобиль заглушен")

    def __str__(self):
        return f"{self.color}, {self.type}, {self.year}"


my_car = Car(color="Black", type="Audi", year="1990")
my_car.sayHi()
my_car.stop()
print(my_car)
