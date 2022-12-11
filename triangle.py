
class Triangle:
    def __init__(self, name, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = name


    def get_perimetr(self):
        return f"{self.side_a + self.side_b + self.side_c}"


    def get_square(self):
        return f"{(self.side_a * self.side_b) / 2:.0f}"

    def __str__(self):
        return f"{self.name}: {'perimetr'}: {triangle_1.get_perimetr()}, {'square'}: {triangle_1.get_square()}"

triangle_1 = Triangle('triangle', side_a=3, side_b=4, side_c=5)



