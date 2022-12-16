class User:
    def __init__(self, name: str, surname: str, age: int, gender: str, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.profession = profession



    def new_brith_year(self):
        britn_year = 2022 - self.age
        return britn_year

    def get_email(self):
        email = self.name + '.' + self.surname + '@gmail.com'
        return email

    def policeman(self):
        profession = self.profession
        return profession

    def doctor(self):
        profession = self.profession
        return profession


    def teacher(self):
        profession = self.profession
        return profession



person = User(name='Peter', surname="Siyu", age= 20, gender='Male', profession="Policeman")
person_2 = User(name='Sasha', surname="Ptyshkina", age= 43, gender='Female', profession="Doctor")
person_3 = User(name='Sasha', surname="Ivanov", age= 32, gender='Male', profession="Teacher")
print(person.policeman(), person.new_brith_year(), person.get_email())
print(person_2.doctor(), person_2.new_brith_year(), person_2.get_email())
print(person_3.teacher(), person_3.new_brith_year(), person_3.get_email())