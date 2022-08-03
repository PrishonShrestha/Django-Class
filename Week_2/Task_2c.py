
"""Create a class Employee, with attributes: name, emp_code, designation.
Generate 4 digit emp code (using static method)
Create a method to create an employee object and emp_code for it should be generated using the method: that you created in Q.3.a.
Create objects :
One directly by passing parameters to the class. 
Another by the method you created in Q.3.b.
"""

from random import randint


class Employee:
    def __init__(self, name, emp_code, designation):
        self.name = name
        self.emp_code = emp_code
        self.designation = designation

    @staticmethod
    def random_number():
        rand_num = randint(1000, 9999)
        return rand_num


    @classmethod
    def employee_class(cls, name, designation):
        # print("Name: ", name)
        # print("Emp code: ", emp_code)
        # print("Designation: ", designation)
        emp_code = cls.random_number()
        return cls(name, emp_code, designation)

    def display(self):
        print(self.name, self.emp_code, self.designation)
#emp_code = Employee.random_number()

Employee.employee_class("name", "abc").display()
#print(emp_code)