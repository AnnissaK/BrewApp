#people list empty and drinks in function
#person.name is like the name of objec could be anthing you iteratig through objects when do person.name for person in people
from table import print_table
import sys
import csv
from csv import reader
from csv import writer

APP_NAME = 'Brew App'
MENU = f'''Welcome to {APP_NAME} v0.1!
Please, select an option by entering a number:
[1] Get all people
[2] Get all drinks
[3] Exit 
[4] Add person
[5] Add drink
[6] Round of drinks
[7] Choose favourites
'''
file_people_list = 'person.txt'
file_drink_list = 'drink_list.txt'
fave_dictionary = 'favourites_dictionary.csv'
round_class = 'round.csv'
people = []
drinks=[]
favourites_dict = {}

# def load_favourites():
#     with open(fave_dictionary,'r') as csvfile:
#         csv_reader = csv.reader(csvfile)
#         for row in csv_reader:
#             name,drink = row
#             favourites_dict[name]=drink
#             return favourites_dict


# def save_dictionary_items(name,drink):
#     with open(favourites_dict,'a+',newline ='') as csvfile:
#         csv_writer = writer(csvfile)
#         csv_writer.writerow([name,drink])


def start():
    load_people()
    loading_drinks()
    load_round_data_into_class()


def menu_option():
    print(MENU)
    answer = (int(input('what is your option?: \n')))
    output(int(answer))

def return_to_input():
    escape = int(input('press one to return to input command\n'))
    try:
        if escape == 1:
            menu_option()
        else:
            print('please press one \n')
    except ValueError:
        print('An integer please\n')

class Person():
     def __init__(self,name):
         self.name = name

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


class Favourites(Person):                               #try loading files into it - try csv for favourites and appending to class
    def __init__(self,name):
        self.fave_dict = {}
    
    def add_to_favourites(self,name,drink):
        self.fave_dict[name]=drink

    def print_favourites(self):
        items = []
        for name,drink in self.fave_dict.items():
            items.append(f'{name} favourite drink is {drink}')
        print_table('favourites',items)
    
def load_round_data_into_class():
    with open('round.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            R1 = Round(row[0])
            R1.add_order(row[1],row[2])
            R1.add_order(row[1],row[2])
            R1.return_items()

def save_round(ordername,name,drink):
    with open(favourites_dict,'a+',newline ='') as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow([ordername,name,drink])


def data_from_file(path):
    with open(path,'r') as f:
        data = []
        my_file = f.readlines()
        for i in my_file:
            data.append(i.strip())
        return data

def get_drinks_list():
    drinks_data_list= data_from_file(file_drink_list)
    return drinks_data_list


def load_people():
    with open(file_people_list,'r') as f:
        my_file = f.readlines()
        for i in my_file:
            people.append(Person(i.strip()))
        people_names = [person.name for person in people]
        return people_names

    
def loading_drinks():
    for drink in get_drinks_list():
        drinks.append(drink)


def save_items(path,data):
    with open(path,'a+')as f:
        if data not in f.read():
            f.write(f'{data}\n')  #where save drinks and people files


def add_name():
    user_input_name = input(str('add name you want:\n'))
    if user_input_name not in load_people():
        save_items(file_people_list,user_input_name)
    else:
        print('name already on the database')                        
        
def add_drinks():
    user_input_drinks = input(str('add the drink you want:\n'))
    if user_input_drinks not in drinks:
        save_items(file_drink_list,user_input_drinks)
    else:
        print('drink already on database')


def round_of_drinks():
    print()
    input_round = input(str('who will be buying the round of drinks?\n'))
    round1 = Round(input_round)
    input_name = input('name of people you are buying for seprated by spaces?\n')
    input_list_name= input_name.split() 
    input_drink = input('enter the corresponding drinks that the people would like to order\n')
    input_list_drink = input_drink.split()
    for name,drink in zip(input_list_name,input_list_drink):
        round1.add_order(name,drink)
        round1.return_items()
        save_round(input_round,name,drink)

        
def favourites_prompts():
    print(load_people())
    input_name = input('pick a name from the list of people\n')
    name = input_name
    if name not in load_people():
        print('add name to list by selecting option 4')
    input_drinks = input('pick favourite drink from the list of drinks\n')
    drink = input_drinks
    if drink not in drinks:
        print(' add drink to list by selecting 5')
    favourites = Favourites(input_name)
    favourites.add_to_favourites(name,drink)
    favourites.print_favourites()
    favourites_dict[input_name]=input_drinks
    print(f'this is the favourites menu') 
    print(favourites_dict)

def output(answer):
    while True:
        if answer == 1:
            print_table('People',load_people())
            return_to_input()
        elif answer ==2:
            get_drinks_list()
            loading_drinks()
            print_table('Drinks',drinks)
            return_to_input()
        elif answer == 3:
            exit()
        elif answer == 4:
            add_name()
            return_to_input()
        elif answer == 5:
            add_drinks()
            return_to_input()
        elif answer ==6:
            round_of_drinks()
            return_to_input()
        elif answer ==7:
            favourites_prompts()
            return_to_input()

if __name__ == "__main__":
    start()
    menu_option()
   














# def call_people():
#     person = input('enter your name?\n')
#     name_of_person = Person(person)
#     return str(name_of_person)
    
    


      







# def add_to_people():
#     person = input('enter your name?\n')
#     name_of_person = Person(person)
    
#     with open("file_people.txt","a+") as f_people:
#         if person not in getname():
#             f_people.write(person +"\n")
#             getname().append(person)
#         else:
#             print('name already on the system')




# # def getname():
# #      if os.path.exists("people_list.txt"):
# #          append_write = "a+"
# #      else: