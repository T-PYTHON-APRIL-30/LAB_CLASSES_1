# LAB_CLASSES_1


## Using what you learned about classes , create a class to represent a Panda.
#  The class should have the following:
# - 4 Attributes
# - 2 Methods
### Create 4 instances of the class Panda , print 1 attribute value,  
# and call the two methods on each instance. 

class Panda:
    def __init__(self,name:str,height:str,weight:float,diet:str):
        self.name = name
        self.height = height
        self.weight = weight
        self.diet = diet

    def pandas_attributes_self(self):
        return f"the name of panda is {self.name}.the bist diet is {self.diet}"
    def Height_and_Weight(self):
        return  f" the Height & Weight for panda {self.name} is : {self.height}, {self.weight} Ibs "  
# Instantiate the Panda object
panda1=Panda("Bai Yun", "2 to 3 feet", 150 ,"Bamboo")
panda2=Panda("Bao Bao", "20 to 26 inches" , 76 , "Bamboo")
panda3=Panda("Bei Bei","3 feet",103,"Bamboo")
panda4=Panda("Gao Gao","4 feet",97.3,"Bamboo")

#reading an attribute
print(panda1.name)
print(panda2.name)
print(panda3.name)
print(panda4.name)

#calling a method
print(panda1.pandas_attributes_self())
print(panda1.Height_and_Weight())
print(panda2.pandas_attributes_self())
print(panda2.Height_and_Weight())
print(panda3.pandas_attributes_self())
print(panda3.Height_and_Weight())
print(panda4.pandas_attributes_self())
print(panda4.Height_and_Weight())