
class Rentangle:
    def __init__(self, name, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        self.name = name


    def get_square(self):
        return f"{self.side_a * self.side_b}"


    def get_perimetr(self):
        return f"{2 * (self.side_a + self.side_b)}"


    def __str__(self):
        return f"{self.name}: {'perimetr'}: {rentangle_1.get_perimetr()}, {'square'}: {rentangle_1.get_square()}"


rentangle_1 = Rentangle('rentangle', side_a=4, side_b=10)



