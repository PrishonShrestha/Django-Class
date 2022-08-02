'''
class Person:
    age = 32
    name = "Prishon"
    def get_name(self):
        print(f'My name is {self.name}')

'''
'''
class Person:
    def __init__(self,age, name="a"):
        self.age = age 
        self.name = name

    def get(self):
        print("Calling here: ", self.name, self.age)


    def __str__(self):
        return f"My name is {self.name}"

p = Person(age=20)
p2 = Person(100, "a")
#p.get_name()
print(p.age)
print(p2.name)

print(p.get())
print(Person.get(p2))
print(p2)'''

from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def obj_createwith_age_by_yr (cls, name, year):
        age = date.today().year -year
        print(age)
        return cls(name, age)

#person = Person("liza", 22)
p2 =Person.obj_createwith_age_by_yr("ABC", 1998)
