from datetime import date

class ClassMethod():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} is {self.age} years old")

    @classmethod
    def classMethod(cls, name, birthYear):
        #age = date.today().year - birthYear
        #print(f"{name} is {age} years old")
        return cls(name, date.today().year - birthYear)

### Using normal method
normalMethod = ClassMethod('Prishon', 20)
normalMethod.display()

### Using class method
ClassMethod.classMethod("Prishon", 1900).display()

a= ClassMethod.classMethod("abc", 1998)
a.display()



        