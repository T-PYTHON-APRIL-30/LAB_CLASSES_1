class panda():
    def __init__(self,age:int,weight:float,region:str,height:float):

        self.age=age
        self.weight=weight
        self.region=region
        self.height=height
    def panda_region(self):

        if self.region=="africa":
            print("most of pandas in south of africa")
        elif self.region=="asia":
            print(" most of pandas in wast of china")
        else: 
            print("nost of pandas lives in jungle")
    def dispaly(self):
        print(f"this panda is {self.age} years old, his weight is {self.weight} kg\
and his height is {self.height} m.he lives in {self.region}.")


panda1=panda(3,60,"africa",0.80)
panda2=panda(5,90.5,"asia",1.70)
panda3=panda(1,20,"africa",0.70)
panda4=panda(4,80,"america",0.80)

panda1.panda_region()
panda1.dispaly()

panda2.panda_region()
panda2.dispaly()

panda3.panda_region()
panda3.dispaly()

panda4.panda_region()
panda4.dispaly()
