# LAB_CLASSES_1

class Panda:
    def __init__(self, color:str, weight:float,age:int,size:float):
        self.color=color
        self.weight=weight
        self.age=age
        self.size=size
    def density(self):
        density=self.weight/self.size #this equation is not real don't try at home 
        return round(density,2)
    def tag(self):
        return(f"This panda is taged it's weight: {self.weight} and it is {self.age} year old")

#these are not the real numbers of actual pandas xD
panda1=Panda("black and white",200,20,154.9)
panda2=Panda("black and white",150,10,112.4)
panda3=Panda("black and white",150,15,90.5)
panda4=Panda("pink",20,1,100)

#print 1 attribute value and calling the two methods on each instance.
print("the age of this panda is: ",panda1.age)
print(panda1.tag())
print("the density of this panda is: ", panda1.density())

print("the age of this panda is: ",panda2.age)
print(panda2.tag())
print("the density of this panda is: ", panda2.density())

print("the age of this panda is: ",panda3.age)
print(panda3.tag())
print("the density of this panda is: ", panda3.density())

print("the age of this panda is: ",panda4.age)
print(panda4.tag())
print("the density of this panda is: ", panda4.density())
