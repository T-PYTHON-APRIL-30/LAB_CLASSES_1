'''

Using what you learned about classes , create a class to represent a Panda. The class should have the following:
4 Attributes
2 Methods
Create 4 instances of the class Panda , print 1 attribute value, and call the two methods on each instance.

'''


class Panda:
    # Attributes
    def __init__(self, name, age, weight, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender

    # Methods
    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

panda1 = Panda("Panda1", 5, 200, "Male")
panda2 = Panda("Panda2", 7, 220, "Female")
panda3 = Panda("Panda3", 3, 180, "Male")
panda4 = Panda("Panda4", 4, 190, "Female")

pandas = [panda1, panda2, panda3, panda4]

for panda in pandas:
    print(f"Name: {panda.name}")
    print(panda.eat())
    print(panda.sleep())
    print('---')

