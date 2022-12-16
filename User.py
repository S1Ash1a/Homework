class User:
    def __init__(self, name: str, surname: str, age: int, gender: str, profession: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.email = name + '.' + surname + '@gmail.com'
        self.profession = profession
        self.brith_year = 2022 - self.age


    def Policeman():
        return User(name='Peter', surname="Siyu", age= 20, gender='Male', profession="Policeman")


    def Doctor():
        return User(name='Sasha', surname="Ptyshkina", age= 43, gender='Female', profession="Doctor")

    def Teacher():
        return User(name='Sasha', surname="Ivanov", age= 32, gender='Male', profession="Teacher")



    def __str__(self):
        return f"{self.profession}, {self.email}, {self.brith_year}"


person = User(name='Peter', surname="Siyu", age= 20, gender='Male', profession="policeman")
person_2 = User(name='Sasha', surname="Ptyshkina", age= 43, gender='Female', profession="policeman")
person_3 = User(name='Sasha', surname="Ivanov", age= 32, gender='Male', profession="policeman")
print(person)
print(person_2)
print(person_3)