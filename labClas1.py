
class panda():

    def __init__(self,race,weight,height,area):
        self.race = race
        self.weight = weight
        self.height = height
        self.area = area
    
    def get_panda_height(self):
        print(f"height in cm: {self.height}")

    def display_panda_info(self):
        print(f"panda's race: {self.race}, weight: {self.weight}KG, area of living: {self.area}")
    

panda1 = panda("japanese",150,190,"japan")
panda2 = panda("korean",155,192,"south korea") 
panda3 = panda("american",157,194,"united states")
panda4 = panda("chinese",159,195,"china")

print(panda1.area)
print(panda4.area)
print()
panda1.get_panda_height()
panda2.get_panda_height()
panda3.get_panda_height()
panda4.get_panda_height()
print()
panda1.display_panda_info()
panda2.display_panda_info()
panda3.display_panda_info()
panda4.display_panda_info()