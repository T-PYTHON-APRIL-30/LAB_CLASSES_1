class Panda:

    def __init__(self,environment:str, age:int, color:int, weight:float,height:int):
        self.environment = environment
        self.age = age 
        self.color = color
        self.weight = weight
        self.height = height

    def aboutPanda(self):
        return f"The average age of a panda is {self.age} years, and it often lives in the {self.environment} also its color is ( {self.color} ) and mostly its weight is {self.weight} kg."
    
    def pandasHeight(self):
        return f"The height of the panda is {self.height} cm"
        

generalPandasInfo = Panda("temperate forests",27,"black and white",100.0,150)
print("--- general Info ---")
print(generalPandasInfo.aboutPanda())
print("--- environment ---")
pandasEnvironment = generalPandasInfo.environment
print(f"The panda's often lives in the {pandasEnvironment}.")
print("--- age ---")
pandasAge = generalPandasInfo.age
print(f"The panda's average age is {pandasAge} years.")
print("--- color ---")
pandasColor = generalPandasInfo.color
print(f"The panda's colors are {pandasColor}.")
print("--- weight ---")
pandasWeight = generalPandasInfo.weight
print(f"The panda's average weight is {pandasWeight}kg.")
print("--- height ---")
userinput = int(input("What do you the average height of a panda? "))

if userinput == generalPandasInfo.height :
    print(f"Yes it's {generalPandasInfo.height}, you got it.")
else:
    print(f"Wrong guess, {generalPandasInfo.pandasHeight()}.")