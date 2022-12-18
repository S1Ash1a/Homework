
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
    def country(city):
        if city == "BMW":
            return "Germani"
        elif city == "Vaz":
            return "Russia"
        elif city == "VolVO":
            return 'China'
        else:
            return f"City not made"

    def country_instance(self):
        if self.name == "BMW":
            return "Germani"
        elif self.name == "VAZ":
            return "Russia"
        elif self.name == "VOLVO":
            return 'China'
        else:
            return f"City not made"



    def usd_price(self):
        usd = self.price / 2.5
        return  usd

    def __str__(self):
        return f"name : {self.name}, Age : {self.age}, Milage : {self.__milage}, price : {self.price} руб,"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age








avto = Car(milage=20000, name='BMW', age=2010, price=15000)
avto_2 = Car(milage=10000, name='AUDI', age=2020, price=50000)
avto_3 = Car(milage=150000, name='VAZ', age=1995, price=5000)
avto_4 = Car(milage=100000, name='VOLVO', age=2000, price=30000)


print(avto == avto_2)
print(Car.get_count())

avto.milage = 50000
print(avto.milage, avto.__dict__)

print(avto, 'Цена в долларах :', avto.usd_price(), 'Maden in :', avto.country_instance())
print(avto_2, 'Цена в долларах :', avto_2.usd_price(), 'Maden in :', avto_2.country_instance())
print(avto_3, 'Цена в долларах :', avto_3.usd_price(), 'Maden in :', avto_3.country_instance())
print(avto_4, 'Цена в долларах :', avto_4.usd_price(), 'Maden in :', avto_4.country_instance())
