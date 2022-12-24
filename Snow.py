
class Snow:
    def __init__(self, quantity_snowflakes):
        self.quantity = int(quantity_snowflakes)

    def __add__(self, n):
        return self.quantity + n

    def __sub__(self, n):
        return self.quantity - n

    def __mul__(self, n):
        return self.quantity * n

    def __truediv__(self, n):
        return self.quantity // n

    def makeSnow(self, quantity_of_snowflakes):
        quantity_of_row = self.quantity // quantity_of_snowflakes
        for i in range(quantity_of_row):
            print("*" * quantity_of_snowflakes)
        print(self.quantity % quantity_of_snowflakes * '*')

squantity_1 = Snow(14)
print(squantity_1.makeSnow(3))


