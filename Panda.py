class bears:

    def __init__(self,wight:int,hight:int,species:str,type:str):

        self.wight = wight
        self.hight = hight
        self.species = species
        self.type = type


class panda (bears):
    def __init__(self, wight: int, hight: int, species: str, type: str,made_of:str,avalible:str):
        super().__init__(wight, hight, species, type)
        self.made_of = made_of
        self.avaliable = avalible

    def Types_of_bear(self):
        return f"bear wight {self.wight} kg ,and thier hight usually {self.hight}, and I species  {self.species} of bears, and his type is {self.type}, and he  is {self.made_of}, and until know he is {self.avaliable} "

panda1 = panda(100,70,"panda","dangrous","live anamals","exisit")
panda2 = panda(90,80,"black bear","dangrous","live anamals","exisit")
panda3 = panda(80,90,"brown bear","dangrous","live anamals","exisit")
panda4 = panda(70,100,"green bear","dangrous","live anamals","exisit")


print(panda1.Types_of_bear())
print("--"*16)
print(panda2.Types_of_bear())
print("--"*16)
print(panda3.Types_of_bear())
print("--"*16)
print(panda4.Types_of_bear())


