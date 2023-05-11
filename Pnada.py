class Panda:
    def __init__(self,name:str,live:str, age:int, height:float ,weight:float):
        self.name=name
        self.live = live
        self.age =age
        self.height= height
        self.weight=weight

    def pand_information(self):
        return f"{self.name} Panda is live in {self.live}, it is {self.age} years old, {self.height} meters and {self.weight} kg"
    
    def bmi(self, weight:float , height:float)->float:
        bmi= round(weight/height**2,2)
        return f"The BMI is: {bmi}"
    
Panda1 = Panda("Absi","Sichuan",3, 1.6, 95 )
Panda2= Panda("Dabdoob","Shaanxi",5 ,1.76, 105)
Panda3 = Panda("Kaabool", "Gansu provinces",2 , 1.5, 70)
Panda4=Panda("Eren","lowland areas", 6, 1.8, 115)

print(Panda1.pand_information())
print(Panda1.bmi(Panda1.weight,Panda1.height))
print("\n")
print(Panda2.pand_information())
print(Panda2.bmi(Panda2.weight,Panda2.height))