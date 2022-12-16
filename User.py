class User:
    def __init__(self, name: str, surname: str, age: int, gender: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender


    def new_brith_year(self):
        britn_year = 2022 - self.age
        return britn_year

    def get_email(self):
        email = self.name + '.' + self.surname + '@gmail.com'
        return email

    def policeman():
        profession = 'Policeman'
        return profession

    def doctor():
        profession = 'Doctor'
        return profession


    def teacher():
        profession = "Teacher"
        return profession



person = User(name='Peter', surname="Siyu", age= 20, gender='Male')
person_2 = User(name='Sasha', surname="Ptyshkina", age= 43, gender='Female')
person_3 = User(name='Sasha', surname="Ivanov", age= 32, gender='Male')
print(User.policeman(), person.new_brith_year(), person.get_email())
print(User.doctor(), person_2.new_brith_year(), person_2.get_email())
print(User.teacher(), person_3.new_brith_year(), person_3.get_email())