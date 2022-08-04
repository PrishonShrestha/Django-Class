#Inheritance

#Classwork: Do for Vehicle with parameters brand, model and num of wheels. 
#Inherit it to Car and Bike, override the num of wheels attribute for car and bike respectively. 

class Vehicle:
    def __init__(self, brand, model, no_of_people):
        self.brand = brand
        self.model = model
        self.no_of_people = no_of_people

    def vehicle_discription(self):
        print(f" Brand: {self.brand} \n Model: {self.model} \n Number of people: {self.no_of_people}")


class Car(Vehicle):
    #Override
    def __init__(self, brand, model, no_of_people, no_of_wheels=4):
        super(Car, self).__init__(brand, model, no_of_people)
        self.no_of_wheels = no_of_wheels

class Bike(Car):
    def bike_disc (self):
        self.no_of_wheels = 2

# vehicle = Vehicle("BMW", "abc", 32)
# vehicle.vehicle_discription()

car = Car('abc', 'bcd', 4)
print(car.vehicle_discription())
print("Number of wheels: ", car.no_of_wheels)

bike = Bike('a','b', 2)
bike.bike_disc()
print(bike.vehicle_discription())
print("Number of wheels: ", bike.no_of_wheels)
        