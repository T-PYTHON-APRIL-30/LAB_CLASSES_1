'''Using what you learned about classes ,
 create a class to represent a Panda. 
 The class should have the following:
4 Attributes
2 Methods
Create 4 instances of the class Panda , 
print 1 attribute value, and call the two methods on each instance.'''
class Panda:
    def __init__(self, name:str,color:str, age:int, weight:int) -> None:
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
    
    def runningPanda(self):
        return f"its name: {self.name}, and it color {self.color} and  {self.age} years old, and it weigh {self.weight} kg"
    def colorpanda(self):
        return f"it's color {self.color}"
        
PandaOne = Panda("Panda1", "Black", 3, 30)
print(PandaOne.name)
print(PandaOne.colorpanda())
PandaTwo = Panda("Panda2", "white", 7, 44)
print(PandaTwo.color)
print(PandaTwo.colorpanda())
PandaThree = Panda("Panda3", "brown", 33, 66)
print(PandaThree.age)
print(PandaThree.colorpanda())
PandaFore = Panda("Panda4", "gray", 4, 76)
print(PandaFore.weight)
print(PandaFore.colorpanda())
