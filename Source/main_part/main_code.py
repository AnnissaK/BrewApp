#have to go back to file and put curser on next line or throws error
#generic function
import csv
import sys
from csv import DictReader, reader, writer
import pymysql
from prettytable import PrettyTable
from Source.Classes.add_class_data import (add_faves_class,load_into_round_class, load_people)
from Source.Classes.drink_and_people_class import Drink, Person
from Source.Classes.favourites_class import Favourites
from Source.Classes.handle_classes import (round_handle_drinks,round_handle_user_input)
from Source.Classes.round_class import Round
from Source.CSV_data_storage.csv_load_data import load_into_list
from Source.CSV_data_storage.save_csv import save_csv_items, save_round
from Source.handle_inputs.preference_handle import age_restriction_for_preferences
from Source.people_list.people_to_append import people
from Source.printing_functions.print_table_items import print_table
from Source.printing_functions.printing_outputs import (favourites_menu,get_age_of_person,get_cost_of_drinks,get_type_of_drink,print_drinks,print_people,print_previous_orders)
from Source.data_bases.load_into_drinks import drinks                                                   
from Source.data_bases.pulling_data_app import connection_f
from Source.data_bases.round_list import round_variables
from Source.data_bases.saving_databases import handle_user_people,handle_user_drinks,insert_round_data

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
file_people_list = 'Source/CSV_data_storage/person.csv'
file_drink_list = 'Source/CSV_data_storage/drinks.csv'
#people = []
#fave_dictionary='Source/CSV_data_storage/favourites_dictionary.csv'
#drinks=[]
#fave_menu = {}

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


def add_name():
    try:
        user_input = input(str('add your name and age to the database separated by a space in the respective order:\n'))
    except (TypeError,ValueError) as e:
        print(f'{e}')
    handle_user_people(user_input)
    
    
                      
        
def add_drinks():
    try:
        user_input_drinks = input(str('add the drink you want followed by a space with Non_Alcoholic or Alcoholic:\n'))
    except(TypeError,ValueError) as e:
        print(f'{e}')
    handle_user_drinks(user_input_drinks)
            
    

def get_name_of_person(name,list_data):
    try:
        index = int(name)
        element_value =list_data[index]
        return element_value
    except IndexError:
        get_preferred_drinks()

    

def get_preferred_drinks():
    print(print_people())
    input_owner = input('choose a name referring to the owner buying the round \n')
    input_name = input('Please enter the name of person you are buying for \n')
    if input_name not in (print_people()):
        print('your name is not on the system please add your name by returning to the main menu')
    preference_round(input_owner,input_name)
        

def preference_round(input_owner,input_name):
    favourite=[obj.fave_dict for obj in (add_faves_class(load_into_list(fave_dictionary,'name'),load_into_list(fave_dictionary,'favourites')))]
    for d in favourite:
        for key in d:
            if key == input_name:
                age_of_person_name =[person.age for person in people if person.name == input_name]
                age_of_owner =[person.age for person in people if person.name == input_owner]
                drink = d[key]
    age_restriction_for_preferences(age_of_person_name,age_of_owner,input_name,input_owner,drink)


def round_class_dictionary():
    owner_name =get_name_of_person(round_handle_user_input(print_people(),'round owner'),print_people())
    order_person = get_name_of_person(round_handle_user_input(print_people(),'owners orderees name'),print_people())
    name_of_drink =get_name_of_person(round_handle_drinks(),print_drinks())
    owner_age=[person.age for person in people if person.name == owner_name]
    order_person_age =[person.age for person in people if person.name ==order_person]
    drink_type =[element.type for element in drinks if element.drink == name_of_drink]
    dict_order_owner = dict(zip(drink_type,owner_age))
    dict_order = dict(zip(drink_type,order_person_age))
    for (k1,v1),(k2,v2) in zip(dict_order_owner.items(),dict_order.items()):
            if k1== 'Alcoholic':
                if int(v1) <=18:
                    print('it is illegal for you as the owner to buy the round because you are underage')
            if k2 =='Alcoholic':
                if int(v2) <=18:
                    print('it is illegal to buy to an alcoholic drink even if the person buying your round is over 18')
            else:
                print('there is no age restrictions for your drink')
                insert_round_data(owner_name,order_person,name_of_drink)



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
    # start()
    menu_option()
