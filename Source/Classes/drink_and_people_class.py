class Person():
     def __init__(self,name,age):
         self.name = name
         self.age = age


class Drink():
    def __init__(self,drink,type,cost=''):
        self.drink = drink
        self.type = type
        self.cost = cost
        if self.cost =='' and self.type =='Non_Alcoholic':
            self.cost = '2.50'
        else:
            self.cost ='6.50'


   