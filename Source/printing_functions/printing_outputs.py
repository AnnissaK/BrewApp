from Source.Classes.add_class_data import load_into_round_class
from Source.CSV_data_storage.csv_load_data import load_into_list
from Source.people_list.people_to_append import people
from Source.Classes.drink_and_people_class import Drink,Person
from Source.CSV_data_storage.save_csv import save_csv_items
from Source.data_bases.load_into_drinks import drinks
from Source.Classes.add_class_data import add_faves_class
from Source.printing_functions.print_table_items import print_table
from Source.Classes.round_class import Round
from Source.data_bases.round_list import round_variables
from Source.Classes.favourites_class import Favourites
from Source.data_bases.preference_list import favourites_list
from Source.data_bases.saving_databases import insert_into_favourites
from prettytable import PrettyTable
round_file = 'Source/CSV_data_storage/round.csv'
fave_dictionary = 'Source/CSV_data_storage/favourites_dictionary.csv'

def print_ID(list_data):
    people_ID = [person.ID for person in list_data]
    return people_ID      

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
    type_of_drink = [typedrink.type for typedrink in drinks ]
    return type_of_drink

def get_cost_of_drinks():
    cost_of_drinks =[costdrink.cost for costdrink in drinks]
    return cost_of_drinks


def print_previous_orders():
    orders_dict=[obj.orders for obj in round_variables]
    owners_list = [obj.owner for obj in round_variables]
    items =[]
    cost_list=[]
    for d in orders_dict:
        for key in d:
            cost_obj = [obj.cost for obj in drinks if obj.drink == d[key]]
            cost_list.extend(cost_obj)
            items.append((f'{key}\'s ordered {d[key]}'))
    for i,x,s in zip(owners_list,items,cost_list):
        print(f'{i.upper()}\'s ROUND : {x} and the cost of the drink was £{s}')
        
def favourites_menu():
    favourite=[obj.fave_dict for obj in favourites_list]
    #items =[]
    t = PrettyTable()
    t.title='Favourites'
    t.field_names = ['Name','Drink']
    for d in favourite:
        for key in d:
            #items.append((f'{key}\'s favourite drink is {d[key]}'))
            t.add_row([key,d[key]])
    print(t)

#need save csv
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
        input_drinks = input(str('Please write your favourite drink\n'))
    except ValueError:
        print('enter a string')
    if input_drinks not in print_drinks():
        print(' add a drink to the list by selecting 5')
    insert_into_favourites(input_name,input_drinks)

