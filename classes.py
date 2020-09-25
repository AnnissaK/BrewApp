from table import print_table

class Person():
     def __init__(self,name,age):
         self.name = name
         self.age = age


class Drink():
    def __init__(self,drink,type):
        self.drink = drink
        self.type = type

    # def type_of_drink(self):
    #     if self.type == 'Alcohol':
    #         print('I need you to confirm that you are older then 18')
    #     else:
    #         print('you do not need ID to buy this drink')
        

class Round():
    def __init__(self,owner):
        self.owner = owner
        self.orders = {}
    
    def add_order(self,name,drink):
        self.orders[name]=drink


    def return_items(self):
        items = []
        for name,drink in self.orders.items():
            items.append(f'{name},{drink}')
        
        print_table(f"{self.owner}'s round",items)

class Favourites(Person):                              
    def __init__(self,name):
        self.fave_dict = {}
    
    def add_to_favourites(self,name,drink):
        self.fave_dict[name]=drink

    def print_favourites(self):
        items = []
        for name,drink in self.fave_dict.items():
            items.append(f'{name} favourite drink is {drink}')
            print_table('favourites',items)
    
