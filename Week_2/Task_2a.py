#Create a class Vehicle with attributes: color, brand, vehicle_type (car, bike, truck, etc.), number_of_wheels (make default=4), price. 
# #Then create its object, along with a method to access its brand, vehicle type and price.




class Vehicle:
    def __init__(self, color, brand, type, price, number_of_wheels=4 ):
        self.color = color
        self.brand = brand
        self.type = type
        self.number_of_wheels = number_of_wheels
        self.price = price

    def vehicle_details(self):
        print(f"Vehicle Color: {self.color}")
        print(f"Vehicle brand: {self.brand}")
        print(f"Vehicle type: {self.type}")
        print(f"Number of wheels on vehicle: {self.number_of_wheels}")
        print(f"Vehicle price: {self.price}")

v = Vehicle("red", "bmw", "car", "500k", 2)
print(Vehicle.vehicle_details(v))

#print(v.vehicle_details())