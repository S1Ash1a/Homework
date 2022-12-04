
class Triangle:
    def __init__(self, array):
        self.array = array

    def new_triangle(self):
        a = self.array[0]
        b = self.array[1]
        c = self.array[2]

        if a + b > c \
                and a + c > b \
                and b + c > a:
            print("Треугольник существует")
        else:
            print("Треугольник не существует")


triangle_1 = Triangle([3, 4, 5])
triangle_1.new_triangle()