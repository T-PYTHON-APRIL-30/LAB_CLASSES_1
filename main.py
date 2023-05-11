'''
Using what you learned about classes , create a class to represent a Panda. The class should have the following:
4 Attributes
2 Methods
Create 4 instances of the class Panda , print 1 attribute value, and call the two methods on each instance.
'''
class Panda:
    def __init__(self, name:str, age:int, weight:float, height:float):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def panda_info (self):
        return (f"Panda Name: {self.name}, Panda Age: {self.age}, Panda Weight: {self.weight}, Panda Height: {self.height}")

    def panda_bmi(self):
        bmi = round(self.weight/self.height**2,2)
        return (f"Panda BMI: {bmi}\n")

panda1 = Panda("Rou Rou",7,90,1.2)
print(f"\nInformation about {panda1.name}")
print(panda1.panda_info())
print(panda1.panda_bmi())

panda2 = Panda("Su Lin",17,100, 1.5)
print(f"\nInformation about {panda2.name}")
print(panda2.panda_info())
print(panda2.panda_bmi())

panda3 = Panda("Tai Shan",17,104,1.6)
print(f"\nInformation about {panda3.name}")
print(panda3.panda_info())
print(panda3.panda_bmi())

panda4 = Panda("Tian Tian",25,113,1.8)
print(f"\nInformation about {panda4.name}")
print(panda4.panda_info())
print(panda4.panda_bmi())




