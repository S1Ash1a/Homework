
class Triangle:
    def __init__(self, array):
        self.array = array

    def new_triangle(self, a, b, c):
        if a + b > c \
                and a + c > b \
                and b + c > a:
            print("Треугольник существует")
        else:
            print("Треугольник не существует")


triangle_1 = Triangle("a, b, c")
triangle_1.new_triangle(a=3, b=2, c=4)