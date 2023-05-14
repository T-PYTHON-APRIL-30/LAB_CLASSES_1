class Panda:
    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Creating instances of the Panda class
panda1 = Panda("Foo", 5, "Male", 150)
panda2 = Panda("Pan", 3, "Female", 120)
panda3 = Panda("Lee", 2, "Male", 100)
panda4 = Panda("Ling", 4, "Female", 130)

# Accessing an attribute value
print(f"{panda1.name} weighs {panda1.weight} kg.")

# Calling methods on each instance
panda1.eat("bamboo")
panda1.sleep()

panda2.eat("leaves")
panda2.sleep()

panda3.eat("fruits")
panda3.sleep()

panda4.eat("shoots")
panda4.sleep()
