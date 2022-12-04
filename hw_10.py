class SchoolItems:
    def __init__(self, name):
        self.name = name


class Maths(SchoolItems):
    def __init__(self, name, subject):
        SchoolItems.__init__(self, name)
        self.sudject = subject

class PhysicalCulture(SchoolItems):
    def __init__(self, name, element):
        SchoolItems.__init__(self, name)
        self.element = element

class Algebra(Maths):
    def __init__(self, name, num_1, subject = "умножение"):
        Maths.__init__(self, name, subject)
        self.num_1 = num_1


    def __mul__(self, other):
        return f"{self.num_1 * other}"

    def __str__(self):
        return f"Ответ получим : "

class Standard(PhysicalCulture):
    def __init__(self, name, element, approaches_1, approaches_2 ):
        PhysicalCulture.__init__(self, name, element)
        self.approaches_1 = approaches_1
        self.approaches_2 = approaches_2

    def __gt__(self, other):
        if self.approaches_1 > other.approaches_2:
            return True
        else:
            return False


    def __str__(self):
        return f"{self.element} сделал студент - {self.name}"




student_1 = Standard("Sasha", "pull-up", 30, 20)
student_2 = Standard("Sveta", "pull-up", 20, 20)
primer_1 = Algebra("primer_1", 10)
primer_2 = primer_1 * 12


print(primer_1)
print(primer_2)
print(student_1 > student_2)
print(student_1)