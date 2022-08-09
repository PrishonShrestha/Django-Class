#Method overriding

class Veg:
    def __init__(self, name) -> None:
        self.name = name

    def display(self):
        print(f"{self.name} is a vegitable")

class Fruits(Veg):
    def __init__(self, name) -> None:
        super(Fruits, self).__init__(name)
    def display(self):
        print(f"{self.name} is a fruit")

veg = Veg("Carrot")
veg.display()

fruits = Fruits("Mango")
fruits.display()