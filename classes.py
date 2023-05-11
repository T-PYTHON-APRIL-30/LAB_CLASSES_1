class Panda :
    def __init__(self, age:int, weight:float, height:float,color:str):
        self.age = age
        self.weight = weight
        self.height = height
        self.color = color

    def meth1 (self):
        return f"This panda is {self.age} years old, it's color is {self.color},"

    def meth2 (self):
        return f"it's weight is {self.weight} KG, and {self.height} height meter"

panda1 = Panda(12,130,1.3,"white and black")
panda2 = Panda(18,180,1.9,"black and white")
panda3 = Panda(21,188,2,"white")
panda4 = Panda(7,100,0.8,"black")

print (f"this is the first panda's age {panda1.age}\n'this is the second panda's age {panda2.age}\n'this is the third panda's age {panda3.age}\n'this is the fourth panda's age {panda4.age}")

print(panda1.meth1(),panda1.meth2())
print(panda2.meth1(),panda2.meth2())
print(panda3.meth1(),panda3.meth2())
print(panda4.meth1(),panda4.meth2())