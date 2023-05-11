"""# LAB_CLASSES_1


## Using what you learned about classes , create a class to represent a Panda. The class should have the following:
- 4 Attributes
- 2 Methods


### Create 4 instances of the class Panda , print 1 attribute value,  and call the two methods on each instance. 
"""
class Panda:
    def __init__(self,name :str,age:int ,weghit:int ,favorit_food:str):
        self.name=name
        self.age=age
        self.weghit=weghit
        self.favorit_food=favorit_food

    def eat(self,food):
        return f"{self.name} like to eat {food}."
    
    def sleep(self):
        return f"{self.name} is sleeping now."
    
panda1=Panda('PP1',10,50,'Banana')
panda2=Panda('PP2',15,90,'Mango')
panda3=Panda('PP3',12,80,'Grapes')
panda4=Panda('PP4',18,100,'Watermelon')

print(panda4.weghit)
print(" ")
print(panda1.eat(panda1.favorit_food))
print(panda1.sleep())
print(" ")
print(panda2.eat(panda2.favorit_food))
print(panda2.sleep())
print(" ")
print(panda3.eat(panda3.favorit_food))
print(panda3.sleep())
print(" ")
print(panda4.eat(panda4.favorit_food))
print(panda4.sleep())
