
class Car:
    count = 0
    def __init__(self, milage, name, age, price):
        self.name = name
        self.age = age
        self.price = price
        self.__milage = milage
        Car.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @property
    def milage(self):
        return self.__milage

    @milage.setter
    def milage(self, milage):
        self.__milage = milage
        return milage

    @milage.deleter
    def milage(self):
        del self.__milage


    @staticmethod
    def get_country(brand):
        if brand in ["BMW", "AUDI", "MERCEDES"]:
            return "Germany"
        else:
            return "Unknown country"


    def usd_price(self):
        return  f"Price: {self.price} USD ~ {self.price * 2.5} BYN"

    def __str__(self):
        return f"name : {self.name}, Age : {self.age}, Milage : {self.__milage}, price : {self.price} руб,"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


avto = Car(milage=20000, name='BMW', age=2010, price=15000)
avto_2 = Car(milage=10000, name='VOLVO', age=2020, price=50000)

print(avto)
print(avto == avto_2)
print(Car.get_count())
print(avto.usd_price())
print(avto.get_country(avto.name))
print(avto.milage)
avto.milage = 50000
print(avto.milage)


class Chevrolet(Car):
    __get_count = 0

    def get_county(self):
        return "USA"

car_chevrole = Chevrolet(10000, "TAHO", 2021, 40000)


print(car_chevrole.get_county())
print(car_chevrole.get_count())
