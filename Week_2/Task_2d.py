'''Create a TemperatureConverter class, where you need to convert between Kelvin , celsius and Fahrenheit . 
Eg: if degree is given in C, a method to convert C to K, and another to C to F.

Similarly, do for all three temperature measuring units. Hint: use static methods'''


class TemperatureConverter:
    def __init__(self, temp):
        self.temp = temp

    @staticmethod
    def from_C():
        k = temp + 273.15
        f = temp*(9/5) + 32
        return k,f

    @staticmethod
    def from_K():
        c = temp -273.15
        f = (temp-273.15)*(9/5) + 32
        return c,f

    @staticmethod
    def from_F():
        c = (temp-32)*(5/9)
        k = (temp-32)*(5/9)+273.15
        return c, k
        
    def temp_to_convert(self):
        
        if unit=='c':
            print("(k,f)", self.from_C())

        elif unit == 'f':
            print("(c,k)", self.from_F())

        elif unit == 'k':
            print("(c,f)", self.from_K())

        else:
            print("Invalid input")

#print(TemperatureConverter.from_C(200))
temp = int(input("Enter a temperature: "))
unit = str(input("Enter its unit: "))
a = TemperatureConverter(temp)
a.temp_to_convert()