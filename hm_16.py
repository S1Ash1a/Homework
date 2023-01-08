class Cat:
    counter = False
    moor_counter = 0
    mewo_counter = 0
    
    def __init__(self, name: str):
        self.name = name

    def to_answer(self):
        if Cat.counter:
            Cat.moor_counter += 1
            Cat.counter = False
            return f'{self.name} moore'
        else:
            Cat.mewo_counter += 1
            Cat.counter = True
            return f'{self.name} mewo'

    @staticmethod
    def counter_moor():
        return Cat.moor_counter

    @staticmethod
    def counter_mewo():
        return Cat.mewo_counter


 
cat_1 = Cat('Barsik')
print(cat_1.to_answer())
print(cat_1.to_answer())
print(cat_1.to_answer())
print(cat_1.to_answer())

print(cat_1.counter_moor())
print(cat_1.counter_mewo())

