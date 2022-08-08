#Overriding
class Bird:
    def __init__(self, name):
        self.name = name
        self.does_fly = True

class Ostrich(Bird):
    # def __init__(self, name) -> None:
    #     super(Ostrich, self).__init__(name)

    def get_type(self):
        self.does_fly = False
        return print(f"{self.does_fly}: {self.name} cannot fly")

class Parrot(Bird):
    # def __init__(self, name) -> None:
    #     super(Parrot, self).__init__(name)
    def get_type(self):
        self.does_fly = True
        return print(f"{self.does_fly}: {self.name} can fly")

a = Parrot("Parrot")
b = Ostrich("Ostrich")
print(a.get_type())
print(b.get_type())
     

        

