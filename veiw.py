from triangle import triangle_perimetr, triangle_square
from circle import circle_perimetr, circle_square
from rentangle import rentangle_perimetr, rentangle_square


def triangle_result():
    return {"triangle": {"square": triangle_square(2, 6), "perimetr": triangle_perimetr(2, 6 ,8)}}

def circle_result():
    return {"circle": {"square": circle_square(3), "perimetr": circle_perimetr(3)}}

def rentangle_result():
    return {"rentangle": {"square": rentangle_square(2, 4), "perimetr": rentangle_perimetr(2, 4)}}


print(triangle_result())
print(circle_result())
print(rentangle_result())
