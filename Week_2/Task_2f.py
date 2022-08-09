'''Create classes with inheritance as in the picture below. Add your own attributes to the classes.
6. A. Show Multiple Inheritance
6. B. Show Multilevel Inheritance'''



##### Multiple inheritance
class Family:
    def __init__(self, lastname, address) -> None:
        self.lastname = lastname
        self.address = address
    # def test():
    #     print("Family")

class Father(Family):
    def __init__(self, lastname, address) -> None:
        
        super(Father, self).__init__(lastname, address)
        print("I am father")

    def test():
        print("Father")

class Mother(Family):
    def __init__(self, lastname, address) -> None:
        super(Mother, self).__init__(lastname, address)
        print("I am mother")

    def test():
        print("Mother")
    
class Child(Father, Mother):
    def __init__(self, lastname, address) -> None:
        super(Child, self).__init__(lastname, address)
        print("I am child")

    def test():
        print("Child")

Child("name", "nepal")

print(Child.test())
print(Child.mro())


##### Multi-level Inheritance

class Grandpa:
    def __init__(self) -> None:
        print("Grandpa")

class Father1(Grandpa):
    def __init__(self) -> None:
        super().__init__()
        print("Father1")

class Child1(Father1):
    def __init__(self) -> None:
        super().__init__()
        print("Child1")

child1 = Child1()
print(child1)
print(Child1.mro())
    