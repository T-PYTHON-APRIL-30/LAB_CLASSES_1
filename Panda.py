'''Using what you learned about classes , create a class to represent a Panda. The class should have the following:
4 Attributes
2 Methods
Create 4 instances of the class Panda , print 1 attribute value, and call the two methods on each instance.'''

class Panda:

    def __init__(self,name,food,country,age,color):
        self.name = name
        self.food = food
        self.country = country
        self.age = age
        self.__color = color
        

    
    def aboutAnimal(self):
        return f'I am a {self.name}, my age is {self.age} years old. Also I\'m a kind of bears which lives in {self.country}\n I have a unique color ({self.getColor()})..'
    
    def typeOfFood(self):
        return f'My favorite food is {self.food}..'
    
    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        if type(color) != str:
            raise ValueError("You must provide a valid color")
        
        self.__color = color



panda1 = Panda('Panda 1', 'Bamboo', 'China', 10, 'Black & White')
panda2 = Panda('Panda 2', 'Fish', 'China', 5, 'Black & White')
panda3 = Panda('Panda 3', 'Bamboo', 'China', 7, 'Black & White')
panda4 = Panda('Panda 4', 'leaves', 'China', 3, 'Black & White')

print(panda1.aboutAnimal())
print(panda1.typeOfFood())
#print 1 attribute value
print(panda1.getColor())
print()
print(panda2.aboutAnimal())
print(panda2.typeOfFood())
#print 1 attribute value
print(panda2.age)
print()
print(panda3.aboutAnimal())
print(panda3.typeOfFood())
#print 1 attribute value
print(panda3.food)
print()
print(panda4.aboutAnimal())
print(panda4.typeOfFood())
#print 1 attribute value
print(panda4.country)
print()







    
    

    
