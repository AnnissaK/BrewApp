#have to go back to file and put curser on next line or throws error
import sys
from prettytable import PrettyTable
from Source.Classes.drink_and_people_class import Person,Drink
from Source.Classes.favourites_class import Favourites
from Source.Classes.round_class import Round
from Source.printing_functions.printing_outputs import print_drinks,print_people,get_age_of_person,get_type_of_drink,get_cost_of_drinks,print_previous_orders,favourites_menu
from Source.data_bases.pulling_data_app import get_data_base
from Source.CSV_data_storage.csv_load_data import load_into_list
from Source.CSV_data_storage.save_csv import save_csv_items,save_round
from Source.Classes.add_class_data import add_faves_class,load_into_round_class,load_people
from Source.handle_inputs.preference_handle import age_restriction_for_preferences
from Source.people_list.people_to_append import people
from Source.printing_functions.print_table_items import print_table
from Source.Classes.handle_classes import round_handle_drinks,round_handle_user_input
import pymysql
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
file_people_list = 'Source/CSV_data_storage/person.csv'
file_drink_list = 'Source/CSV_data_storage/drinks.csv'
#people = []
#fave_dictionary='Source/CSV_data_storage/favourites_dictionary.csv'
#drinks=[]
#fave_menu = {}

def start():
    load_people(load_into_list(file_people_list,'name'),load_into_list(file_people_list,'age'))
    #load_drinks(load_into_list(file_drink_list,'Drinks'),load_into_list(file_drink_list,'Drink_type'),load_into_list(file_drink_list,'cost'))
    global drinks
    drinks=(get_data_base('Drinks',Drink))

def connection_f():
    connection = pymysql.connect(
    host="localhost",
    port=33066,
    user="root",
    passwd="password",
    database="BrewApp")
    return connection  



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
    name_user = user_input.split()[0]
    age_user = user_input.split()[1]
    if name_user not in print_people():
        save_csv_items(file_people_list,name_user,age_user)
        load_people(load_into_list(file_people_list,'name'),load_into_list(file_people_list,'age'))
    
    else:
        print('name already on the database')                        
        
def add_drinks():
    try:
        user_input_drinks = input(str('add the drink you want followed by a space with Non_Alcoholic or Alcoholic:\n'))
    except(TypeError,ValueError) as e:
        print(f'{e}')
    handle_user_drinks()

 #append to data_list   

#on exit
def handle_user_drinks():
    user_drink = user_input_drinks.split()[0]
    user_type_drink =user_input_drinks.split()[1]
    add_drink_object1 = Drink(user_drink,user_type_drink)
    drinks.append(add_drink_object1)
    cursor = connection_f().cursor()
	args = ("v","p","j")
	cursor.execute("INSERT INTO Drinks (Drink,Drink_type,`Cost / £`) VALUES ({%s},{%s},{%s})",args)
	connection_f().commit()
	cursor.close()
	connection_f().close()
    cursor = connection_f().cursor()
    #for drink_name in drinks:
    args =('k','k','k')
    cursor.execute("INSERT INTO Drinks (Drink,Drink_type,`Cost / £`) VALUES (%s,%s,%s)",args)
        # WHERE '{drink_name.drink}' NOT IN Drink")
    connection_f().commit()
    cursor.close()
    connection_f().close()
            
        
        # cursor = connection_f().cursor()
        # for i in drinks:
        #     cursor.execute(f"INSERT INTO Drinks (Drink,Drink_type,`Cost / £` ) VALUES ('{i.drink}','{i.type}','{i.cost}') \
        #     ON DUPLICATE KEY UPDATE Drink ='{i.drink}',Drink_type='{i.type}',`Cost / £`='{i.cost}'")
        #     connection_f().commit()
        # cursor.close()
        # connection_f().close()
    
    


# def update_data_base(table,class_name,**kwargs):
#     connection_f
#     cursor = connection_f.cursor()
#     for i in get_data_base('Drinks',Drink):
#         for arg in kwargs:
#             arguments = (class_name.kwargs)
#             cursor.execute(f'INSERT INTO {table} ({args},{args},SET VALUES{arg}={arguments} ON DUPLICATE KEY UPDATE {arg}={arguments}')
#     connection_f.commit()
#     cursor.close()
#     connection_f.close()

# update_data_base('Drinks',Drink,A=drink,B=type,C=cost)


        #args =(get_data_base(Drinks,'Drinks').drink,get_data_base(Drinks,'Drinks').type,'4.00')
        #cursor.execute(f'''INSERT INTO {table} ({column1},{column2},{column3}) VALUES ("{%s},{%s},{%s}") ON DUPLICATE KEY UPDATE {column1},{column2},{column3}="{%s},{%s},{%s}"''',args+args)
      
    #if user_drink not in drinks:
        #save_csv_items(file_drink_list,user_drink,user_type_drink)
        #load_drinks(load_into_list(file_drink_list,'Drinks'),load_into_list(file_drink_list,'Drink_type'),load_into_list(file_drink_list,'cost'))
    # else:
    #     print('drink already on database')

def get_name_of_person(name,list_data):
    try:
        index = int(name)
        element_value =list_data[index]
        return element_value
    except IndexError:
        get_preferred_drinks()

    

def get_preferred_drinks():
    print(print_people())
    input_owner = input('choose a name referring to the owner buying the round')
    input_name = input('Please enter the name of person you are buying for')
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
                save_round(owner_name,order_person,name_of_drink)


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
