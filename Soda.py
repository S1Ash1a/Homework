class Soda:
    def __init__(self, additive= None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print(f"Обычная газировка")

soda_1 = Soda("Pepsi")
soda_2 = Soda()
soda_3 = Soda("Orange")
soda_1.show_my_drink()
soda_2.show_my_drink()
soda_3.show_my_drink()
