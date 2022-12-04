class Triangle:
    def __init__(self, name, side_a, side_b, side_c):
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def new_triangle(self):
        if self.side_a + self.side_b > self.side_c \
                and self.side_a + self.side_c > self.side_b \
                and self.side_b + self.side_c > self.side_a:
            print("Треугольник существует")
        else:
            print("Треугольник не существует")


triangle_1 = Triangle("triangle_1", 4, 5, 7)
triangle_1.new_triangle()

