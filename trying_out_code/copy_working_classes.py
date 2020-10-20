#have to go back to file and put curser on next line or throws error
import unittest
from unittest import mock
from unittest.mock import patch
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
file_people_list = 'person.csv'
file_drink_list = 'drinks.csv'
fave_dictionary = 'favourites_dictionary.csv'
round_file = 'round.csv'
people = []
drinks=[]
#fave_menu = {}

def start():
    load_people()
    load_drinks()
    
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


def load_into_list(filename,header):
    data_list =[]
    with open(filename,'r') as csvfile:
        csv_dict_reader = DictReader(csvfile)
        for row in csv_dict_reader:
            data_list.append(row[header])
        return data_list

def add_faves_class():
    favourites1=[]
    for i,s in zip(load_into_list(fave_dictionary,'name'),load_into_list(fave_dictionary,'favourites')):
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



def save_csv_items(path,name,drink):
    with open(path,'a+') as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow([name,drink])

def load_into_round_class():
    order_requests=[]
    for i,name,drink in zip(load_into_list(round_file,'owner'),load_into_list(round_file,'name'),load_into_list(round_file,'drink')):
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
        
#at start
def load_drinks():
    for i,s in zip(load_into_list(file_drink_list,'Drinks'),load_into_list(file_drink_list,'Drink_type')):
        drinks.append(classes.Drink(i,s))

#at start
def load_people():
    for i,s in zip(load_into_list(file_people_list,'name'),load_into_list(file_people_list,'age')):
        people.append(classes.Person(i,s))
    
        
def print_people():
    people_names = [person.name for person in people]
    return people_names

def get_age_of_person():
    person_age = [person.age for person in people]
    return person_age

  
def print_drinks():
    drinks_name = [drink_name.drink for drink_name in drinks]
    return drinks_name

def get_type_of_drink():
    type_of_drink = [typedrink.type for typedrink in drinks]
    return type_of_drink


# def save_items(path,data):
#     with open(path,'a+')as f:
#         if data not in f.read():
#             f.write(f'{data}\n')  #where save drinks and people files


def add_name():
    try:
        user_input = input(str('add your name and age to the database separated by a space in the respective order:\n'))
    except (TypeError,ValueError) as e:
        print(f'{e}')
    name_user = user_input.split()[0]
    age_user = user_input.split()[1]
    if name_user not in print_people():
        save_csv_items(file_people_list,name_user,age_user)
        load_people()
        #people.append(classes.Person(name_user,age_user))
    else:
        print('name already on the database')                        
        
def add_drinks():
    try:
        user_input_drinks = input(str('add the drink you want followed by a space with Non_Alcoholic or Alcoholic:\n'))
    except(TypeError,ValueError) as e:
        print(f'{e}')
    user_drink = user_input_drinks.split()[0]
    user_type_drink =user_input_drinks.split()[1]
    if user_drink not in drinks:
        save_csv_items(file_drink_list,user_drink,user_type_drink)
        load_drinks()
    else:
        print('drink already on database')


def round_handle_user_input(list_data,element):
    for i,x in enumerate (list_data):
        print(i,x)
    input_number = input(f'Select the number corresponding to the {element} you want from the list \n')
    index = int(input_number)
    element_value =list_data[index]
    return element_value

def round_class_dictionary():
    owner_name =round_handle_user_input(print_people(),'round owner')
    order_person = round_handle_user_input(print_people(),'owners orderees name')
    name_of_drink =round_handle_user_input(print_drinks(),'drink')
    owner_age=[person.age for person in people if person.name == owner_name]
    order_person_age =[person.age for person in people if person.name ==order_person]
    drink_type =[element.type for element in drinks if element.drink == name_of_drink]
    dict_order_owner = dict(zip(drink_type,owner_age))
    dict_order = dict(zip(drink_type,order_person_age))
    for (k1,v1),(k2,v2) in zip(dict_order_owner.items(),dict_order.items()):
            if k1== 'Alcoholic':
                if int(v1) <=18:
                    print('it is ilegal for you as the owner to buy the round because you are underage')
                else:
                    print('you as the owner are old enough to buy an Alcoholic drink')
                    save_round(owner_name,order_person,name_of_drink)
                if k2 =='Alcoholic':
                    if int(v2) <=18:
                        print('it is ilegal to buy to an alcoholic drink even if the person buying your round is over 18')
                    else:
                        print('You are old enough to have a alcoholic drink')
                        save_round(owner_name,order_person,name_of_drink)
            else:
                print('there is no age restrictions for your drink')
                save_round(owner_name,order_person,name_of_drink)

def favourites_prompts():
    print(print_people())
    try:
        input_name = input(str('pick a name from the list of people\n'))
        [person.age for person in people if person.name==input_name]
    except ValueError:
        print('enter a string')
    if input_name not in print_people():
        print('add name to list by selecting option 4')
    try:
        print(print_drinks())
        input_drinks = input(str('pick favourite drink from the list of drinks\n'))
    except ValueError:
        print('enter a string')
    if input_drinks not in print_drinks():
        print(' add a drink to the list by selecting 5')
    save_csv_items(fave_dictionary,input_name,input_drinks)
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
            print_table('Drinks',print_drinks())
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
            round_class_dictionary()
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
