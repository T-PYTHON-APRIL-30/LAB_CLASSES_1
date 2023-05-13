class Panda:


    def __init__(self,age:int,weight:int,eat:str,sleep:int):
        self.age = age
        self.weight = weight
        self.eat = eat
        self.sleep = sleep


    def life(self):
        return(f"Most of the pandas eat{self.eat} and weight always about of {self.weight} Kg")

    def life_cicle(self):
        return (f"the average age of pandas about {self.age} years and Sleeping for {self.sleep} between meals")
    


panda_1 = Panda(20,115,"Bamboo",4)
panda_2 = Panda(15,120,"Fish",3)
panda_3 = Panda(17,110,"plants",2)
panda_4 = Panda(18,105,"small animals",5)

print(panda_1.age)
print(panda_3.eat)

print("")

print(panda_1.life(), panda_1.life_cicle()) , print()

print(panda_2.life(), panda_2.life_cicle()) , print()

print(panda_3.life(), panda_3.life_cicle()) , print()

print(panda_4.life(), panda_4.life_cicle())
