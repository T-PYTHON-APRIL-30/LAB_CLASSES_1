'''LAB_CLASSES_1
Using what you learned about classes , create a class to represent a Panda. The class should have the following:
4 Attributes
2 Methods
Create 4 instances of the class Panda , print 1 attribute value, and call the two methods on each instance.
'''

class Panda:
    def __init__(self,Type:str,size:str,weight:float,height:float):
        self.Type=Type
        self.size=size
        self.weight=weight
        self.height=height
    def PandaInfo(self):
        return f"the panda type{self.Type},the panda size{self.size}and it is weight is :{self.weight},It is height{self.height}"
    def PandaLife(self):
        panda_life="for along time it was believed that the panda bear was a member of the raccoon family\n but genetic research revealed that the panda this wonderfully \nbeloved animal is actually abear and is a member of the urcid family.\n"
        return panda_life
        
panda1=Panda("giantPanda","Big",100,120)
panda2=Panda("redPanda","small",20,60)
panda3=Panda("BigPandaBear","VBig",160,150)
panda4=Panda("SmallPandaBear","Vsmall",15,40)

print(panda1.Type)
print(panda1.PandaInfo())
print(panda1.PandaLife())
print(panda2.Type)
print(panda2.PandaInfo())
print(panda2.PandaLife())
print(panda3.Type)
print(panda3.PandaInfo())
print(panda3.PandaLife())
print(panda4.Type)
print(panda4.PandaInfo())
print(panda4.PandaLife())




