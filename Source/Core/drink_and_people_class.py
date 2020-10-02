class Person():
     def __init__(self,name,age):
         self.name = name
         self.age = age


class Drink():
    def __init__(self,drink,type,cost):
        self.drink = drink
        self.type = type
        self.cost = cost
    
    def cost_function(self):
        if self.type =='Alcoholic':
            self.cost == "6.50"
        else:
            self.cost == "2.50"
        