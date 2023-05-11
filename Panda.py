import datetime

class Panda :
    def __init__(self, birthday:str, name:str, weight:float, height:float) -> None:
        self.valid_date(birthday)
        self.birthday : str = birthday
        self.name : str = name
        self.weight : float = weight 
        self.__height : float = height

    def get_height(self):
        return self.__height 
    
    def set_height(self, height:float):
        self.__height = height

    def get_age(self):
        dateToday : str= str(datetime.date.today())
        dateToday  = dateToday.split("-")
        birthDay = self.birthday.split("-")
        return int(dateToday[0]) - int(birthDay[0])

    def valid_date(self, date:str):
        '''check format date as yyyy-mm-dd'''
        if type(date) != str:
            raise ValueError("the date should be string")
        if len(date) != len("yyyy-mm-dd") or not date[:4].isdigit() or not date[5:7].isdigit() or not date[8:].isdigit() :
            raise ValueError("the format date should be as yyyy-mm-dd. for instanse: 2000-02-05")
        
        return True
    def toString(self):
        print(f'my name is {self.name}, and my birthday id {self.birthday}, bye!! ')

pandas : list = []
pandas.append(Panda("2004-02-11", "popo", 110, 1.2))
pandas.append(Panda("2007-02-11", "pipo", 90, 1.1))
pandas.append(Panda("2009-02-11", "pipi", 200, 1.8))
pandas.append(Panda("2019-02-11", "popi", 135, 1.6))
for panda in pandas:
    panda.toString()
    print(panda.weight)
    print(f'l am {panda.get_age()} years old')

