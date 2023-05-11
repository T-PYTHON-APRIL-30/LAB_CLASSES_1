'''Using what you learned about classes , create a class to represent a Panda. The class should have the following:
4 Attributes
2 Methods
Create 4 instances of the class Panda , print 1 attribute value, and call the two methods on each instance.'''

class Panda:
    def __init__(self, number: int, age: int, weight: float, height: float):
        self.number = number
        self.age = age
        self.weight = weight
        self.height = height
    

    def panda_info(self):
        return print(f"Panda no. {self.number}, age: {self.age} years, weight: {self.weight} Kg, height: {self.height} cm")


    def panda_food(self):
        return print(f"Panda no. {self.number}, eats: 80-100 Kg of Bamboo.")


panda1 = Panda(1478, 10, 113, 150)
panda2 = Panda(3698, 8, 100, 165)
panda3 = Panda(2589, 15, 120, 180)
panda4 = Panda(2587, 4, 90, 120)

print(panda1)

panda1.panda_info()
panda2.panda_info()
panda3.panda_info()
panda4.panda_info()

print("\n")

panda1.panda_food()
panda2.panda_food()
panda3.panda_food()
panda4.panda_food()