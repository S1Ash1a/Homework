

class Circle:
    __pi = 3.14
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def get_square(self):
        return f"{Circle.__pi * (self.radius ** 2) :.0f}"

    def get_perimetr(self):
        return f"{2 * Circle.__pi * self.radius :.0f}"

    def __str__(self):
        return f"{self.name}: {'perimetr'}: {circle_1.get_perimetr()}, {'square'}: {circle_1.get_square()}"


circle_1 = Circle('circle', radius=4)




