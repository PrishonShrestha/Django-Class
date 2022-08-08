'''In order to make burger a chef needs at least the following ingredients:
• meat: pork, ham, chicken
• lettuce leaves
• tomato slices
sauce: bbq or mayonnaise
cheese

Get values of chicken meat, lettuce leaves and tomato slices from user. And create a normal sized burger. Use of OOP in Python.'''

class Burger:
    def __init__(self, meat, lettuce, tomato, sauce, cheese) -> None:
        self.meat = meat
        self.lettuce = lettuce
        self.tomato = tomato
        self.sauce = sauce
        self.cheese = cheese

class MediumBurger(Burger):
    def __init__(self, meat, sauce,  lettuce='', tomato='', cheese='') -> None:
        super(MediumBurger, self).__init__(meat, lettuce, tomato, sauce, cheese)
        self.lettuce = "5 pieces"
        self.tomato = "5gm"
        self.cheese = "5gm"
    
    def ingredients(self):
        return print(f"Ingredients for Medium Size burger: \n Meat: {self.meat} \n Sauce: {self.sauce} \n Lettuce leaves: {self.lettuce} \n Tomato: {self.tomato} \n Cheese: {self.cheese}")

class LargeBurger(Burger):
    def __init__(self, meat,  sauce,  lettuce='', tomato='', cheese='') -> None:
        super(LargeBurger, self).__init__(meat, lettuce, tomato, sauce, cheese)
        self.lettuce = "8 pieces"
        self.tomato = "8gm"
        self.cheese = "8gm"

    def ingredients(self):
        return print(f"Ingredients for Large Size burger: \n Meat: {self.meat} \n Sauce: {self.sauce} \n Lettuce leaves: {self.lettuce} \n Tomato: {self.tomato} \n Cheese: {self.cheese}")

meat = input("Meat: ")
sauce = input("Sauce: ")
#burgerSize = input("Burger size (M/L): ")
m = MediumBurger(meat,sauce)
l = LargeBurger(meat, sauce)

m.ingredients()
l.ingredients()




# p = LargeBurger(meat,sauce)
# print(p.ingredients())
