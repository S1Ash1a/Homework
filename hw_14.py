
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

    def __call__(self, new_quantity):
        return self.quantity == new_quantity

    def makeSnow(self, quantity_of_snowflakes):
        string_snowflakes = ""
        quantity_of_row = int(self.quantity) // quantity_of_snowflakes
        for i in range(quantity_of_row):
            string_snowflakes += ("*" * quantity_of_snowflakes)
            string_snowflakes += "\n"
        rest_of_snowflakes = (int(self.quantity) - quantity_of_row * quantity_of_snowflakes)
        string_snowflakes += "*" * rest_of_snowflakes
        return string_snowflakes

squantity_1 = Snow(200)
print(squantity_1.makeSnow(10))


