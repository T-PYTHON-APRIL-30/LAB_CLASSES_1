# LAB_CLASSES_1


## Using what you learned about classes , create a class to represent a Panda.
#  The class should have the following:
# - 4 Attributes
# - 2 Methods
### Create 4 instances of the class Panda , print 1 attribute value,  
# and call the two methods on each instance. 

class Panda:
    def __init__(self,type:str,  height:float,weight:str,diet:str):
        self.type = type
        self.height = height
        self.weight = weight
        self.diet = diet

    def differentiates_discover_self(self):
        return f"the type of panda is {self.type} ,the Height & Weight: {self.height}, {self.weight} Ibs.the bist diet is {self.diet}"
    
# Instantiate the Panda object
panda1=Panda("giant panda", "2 to 3 feet", 150 ,"Bamboo")
panda2=Panda("red panda", "20 to 26 inches" , 7 , "Bamboo")

#reading an attribute
print(panda1.type)
print(panda2.type)

#calling a method
print(panda1.differentiates_discover_self())
print(panda2.differentiates_discover_self())