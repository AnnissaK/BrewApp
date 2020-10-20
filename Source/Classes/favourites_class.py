#from Source.printing_functions.printing_outputs import print_table
class Favourites():                              
    def __init__(self,name):
        self.name = name
        self.fave_dict = {}
    
    def add_to_favourites(self,name,drink):
        self.fave_dict[name]=drink

    def print_favourites(self):
        items = []
        for name,drink in self.fave_dict.items():
            items.append(f'{name} favourite drink is {drink}')
            print_table('favourites',items)
    