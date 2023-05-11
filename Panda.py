class bears:

    def __init__(self,wight:int,hight:int,species:str,type:str):

        self.wight = wight
        self.hight = hight
        self.species = species
        self.type = type

    def Types_of_bear(self):
        return f"bear wight {self.wight} kg ,and thier hight usually {self.hight}, and I species  {self.species} of bears, and his type is {self.type}"

panda = bears (60,1.9,"bears","danager animals")

print(panda.Types_of_bear())

