#have to go back to file and put curser on next line or throws error
from table import print_table
import sys
import classes 
import csv
from csv import DictReader
from csv import writer
from csv import reader

APP_NAME = 'Brew App'
MENU = f'''Welcome to {APP_NAME} v0.1!
Please, select an option by entering a number:
[1] Get all people
[2] Get all drinks
[3] Exit 
[4] Add person
[5] Add drink
[6] View previous rounds
[7] order a round
[8] View favourites menu
[9] Choose favourites
'''
file_people_list = 'person.txt'
file_drink_list = 'drink_list.txt'
fave_dictionary = 'favourites_dictionary.csv'
round_file = 'round.csv'
people = []
drinks=[]
#fave_menu = {}

def start():
    load_people()
    loading_drinks()
    
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


def load_name_fave():
    with open(fave_dictionary,'r') as csvfile:
        name =[]
        csv_dict_reader = DictReader(csvfile)
        for row in csv_dict_reader:
            name.append(row['name'])
        return name
         
def load_drinks_fave():
    with open(fave_dictionary,'r') as csvfile:
        fave_drinks =[]
        csv_dict_reader=DictReader(csvfile)
        fave_drinks =[]
        for row in csv_dict_reader:
            fave_drinks.append(row['favourites'])
        return fave_drinks


def add_faves_class():
    favourites1=[]
    for i,s in zip(load_name_fave(),load_drinks_fave()):
        F1 =classes.Favourites(i)
        F1.add_to_favourites(i,s)
        favourites1.append(F1)
    return favourites1

def favourites_menu():
    favourite=[obj.fave_dict for obj in add_faves_class()]
    items =[]
    for d in favourite:
        for key in d:
            items.append((f'{key}\'s favourite drink is {d[key]}'))
    print_table('Favourites',items)



def save_dictionary_items(name,drink):
    with open(fave_dictionary,'a+') as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow([name,drink])


def load_csv_owner():
    with open('round.csv','r') as read_obj:
        owner_list = []
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            owner_list.append(row['owner'])
        return owner_list

def load_csv_name():
    with open('round.csv','r') as read_obj:
        name_list = []
        csv_dict_reader=DictReader(read_obj)
        for row in csv_dict_reader:
            name_list.append(row['name'])
        return name_list

def load_csv_drink():
    with open('round.csv','r') as read_obj:
        drink_list = []
        csv_dict_reader=DictReader(read_obj)
        for row in csv_dict_reader:
            drink_list.append(row['drink'])
        return drink_list


def load_into_round_class():
    order_requests=[]
    for i,name,drink in zip(load_csv_owner(),load_csv_name(),load_csv_drink()):
        R1=classes.Round(i)
        R1.add_order(name,drink)
        order_requests.append(R1)
    return order_requests

def print_previous_orders():
    orders_dict=[obj.orders for obj in load_into_round_class()]
    owners_list = [obj.owner for obj in load_into_round_class()]
    items =[]
    for d in orders_dict:
        for key in d:
            items.append((f'{key}\'s ordered {d[key]}'))
    for i,x in zip(owners_list,items):
        print(f'{i.upper()}\'s ROUND : {x}')
            
#order_names = [person.owner for person in order_request]
#order_menu = [request.orders for request in order_request]
#[order_names_unique.append(x) for x in order_names if x not in order_names_unique]


def save_round(ordername,name,drink):
    with open('round.csv','a+',newline ='') as csvfile:
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

#at start
def load_people():
    with open(file_people_list,'r') as f:
        my_file = f.readlines()
        for i in my_file:
            people.append(classes.Person(i.strip()))

def print_people():
    people_names = [person.name for person in people]
    return people_names

 #at start   
def loading_drinks():
    for drink in get_drinks_list():
        drinks.append(drink)


def save_items(path,data):
    with open(path,'a+')as f:
        if data not in f.read():
            f.write(f'{data}\n')  #where save drinks and people files



def add_name():
    user_input_name = input(str('add name you want:\n'))
    if user_input_name not in print_people():
        save_items(file_people_list,user_input_name)
        people.append(classes.Person(user_input_name))
    else:
        print('name already on the database')                        
        
def add_drinks():
    user_input_drinks = input(str('add the drink you want:\n'))
    if user_input_drinks not in drinks:
        save_items(file_drink_list,user_input_drinks)
        drinks. append(user_input_drinks)
    else:
        print('drink already on database')


def round_of_drinks():
    print(print_people())
    try:
        input_round = input(str('who will be buying the round of drinks, choose a name in the list please?\n'))
    except ValueError:
        print('enter a word please not an integer')
    try:
        input_name = input(str('name of people you are buying for seprated by spaces?\n'))
    except ValueError:
        print('enter a word please not an integer')
    input_list_name= input_name.split()
    print(drinks)
    try:
        input_drink = input(str('enter the corresponding drinks that the people would like to order from the list of drinks\n'))
    except ValueError:
        print('please enter a word please not an integer')
    input_list_drink = input_drink.split()
    for name,drink in zip(input_list_name,input_list_drink):
        save_round(input_round,name,drink)

def favourites_prompts():
    print(print_people())
    try:
        input_name = input(str('pick a name from the list of people\n'))
    except ValueError:
        print('enter a string')
    name = input_name
    if name not in print_people():
        print('add name to list by selecting option 4')
    try:
        print(drinks)
        input_drinks = input(str('pick favourite drink from the list of drinks\n'))
        drink = input_drinks
    except ValueError:
        print('enter a string')
    if drink not in drinks:
        print(' add drink to list by selecting 5')
    save_dictionary_items(name,drink)
    # favourites = classes.Favourites(input_name)
    # favourites.add_to_favourites(name,drink)
    # favourites.print_favourites()
    # favourites_dict[input_name]=input_drinks
    # print(favourites_dict)

def output(answer):
    while True:
        if answer == 1:
            print_table('People',print_people())
            return_to_input()
        elif answer ==2:
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
            print_previous_orders()
            return_to_input()
        elif answer ==7:
            round_of_drinks()
            return_to_input()
        elif answer ==8:
            favourites_menu()
            return_to_input()
        elif answer ==9:
            favourites_prompts()
            return_to_input()


if __name__ == "__main__":
    start()
    menu_option()
