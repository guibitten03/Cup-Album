# from utilities import StringBuilder
from importlib.resources import Package
from Entity import Entity


class Pessoa(Entity):

    idClass=0


    def __init__(self, name, money):
        self.id = Pessoa.idClass
        Pessoa.idClass += 1
        self.name = name
        # self.album = Album()
        self.count_packages = 0
        self.not_stickeds = list()
        self.money = money
    
    def openPackages(self,n : int):
        self.not_stickeds += Package().open()

      


    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_money(self):
        return self.money
    def get_count_packages(self):
        return self.count_packages
    def get_not_stickeds(self):
        return self.not_stickeds
    
    def set_name(self,name : str):
        self.name = name
    def set_money(self,money : float):
        self.money = money
    def set_count_packages(self,count_packages : int):
        self.count_packages = count_packages
    def set_not_stickeds(self,not_stickeds : list):
        self.not_stickeds = not_stickeds


    
    def __str__(self):
        return "Id: {},Name: {},Money: {},Packages: {},Not stickseds: {}".format(
            self.id,self.name,self.money,self.count_packages,self.not_stickeds)