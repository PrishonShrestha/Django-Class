'''Create a class Point where initial x,y values are initialized with 0. 
Create objects of class Point with x and y values passed to it. 

Eg: point p1 with x=2 and y=3 should be created.
		
Create a method to Calculate distance between two points. 

Formula: res = sqrt((x2-x1)^2 + (y2-y1)^2), where x1 and x2 are x values of p1 and p2 points resp. , y1 and y2 are y values of p1 and p2 resp.

Represent the point objects with x, y values in the format: (x,y). Eg: (2,3).'''



from cmath import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x =x
        self.y = y


    def calc_distance(self, point):
        point.x, point.y

        res = sqrt((self.x-point.x)^2+(self.y-point.y)^2)
        print("Distance: ", res)
    
    def __str__(self):
        return f"Point(x,y): {self.x, self.y}"
        

p1 = Point(2, 3)
p2 = Point(4,5)

print(p1.calc_distance(p2))

print(p1.__str__())
print(p2.__str__())
