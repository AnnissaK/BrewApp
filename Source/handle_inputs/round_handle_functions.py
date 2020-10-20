from Source.printing_functions.printing_outputs import print_people,print_drinks,get_cost_of_drinks
from Source.people_list.people_to_append import people
from Source.data_bases.load_into_drinks import drinks
from Source.data_bases.saving_databases import insert_round_data
from Source.time_function.week_selection import week_day_selection
from Source.data_bases.round_list import round_variables 
from Source.data_bases.preference_list import favourites_list
from prettytable import PrettyTable
#from Source.main_part.menu import return_to_input
def age_restriction_for_preferences(age_of_person,age_of_owner,input_name,input_owner,drink):
    input_type = input('for you as the owner, is your favourite drink Alcoholic, enter y for yes and n for no?')
    if input_type=='y':
        integer_age_person = int("".join(map(str, age_of_person)))
        if integer_age_person<18:
            print('The person being bought for is not old enough to order their favourite drink')
        integer_age_owner = int("".join(map(str,age_of_owner)))
        if integer_age_owner <=18:
            print(' The owner of the roud is not old enough to get the person their ordering for their favourite drink')
        else: 
            print(f'you can buy your favourite drink ,{drink}')
            insert_round_data(input_owner,input_name,drink)
    elif input_type =='n':
        print('There are no age restrictions on soft drinks')
        insert_round_data(input_owner,input_name,drink)

def get_preferred_drinks():
    print(print_people())
    input_owner = input('choose a name referring to the owner buying the round \n')
    input_name = input('Please enter the name of person you are buying for \n')
    if input_name not in (print_people()):
        print('your name is not on the system please add your name by returning to the main menu')
    else:
        preference_round(input_owner,input_name)




def get_name_of_person(name,list_data):
        index = int(name)
        element_value =list_data[index]
        return element_value

def preference_round(input_owner,input_name):
    favourite=[obj.fave_dict for obj in favourites_list]
    for d in favourite:
        for key in d:
            if key == input_name:
                age_of_person =[person.age for person in people if person.name == input_name]
                age_of_owner =[person.age for person in people if person.name == input_owner]
                drink = d[key]
                age_restriction_for_preferences(age_of_person,age_of_owner,input_name,input_owner,drink)  
    
                


def round_handle_user_input(element,list_data):
    t= PrettyTable()
    t.field_names =['Index number','Name']
    for i,x in enumerate (list_data):
        #t =PrettyTable(['Index number','Name'])
        t.add_row([i,x])
    print(t)
    input_number = input(f'Select the number corresponding to the {element} you want from the list \n')
    return input_number

def round_handle_drinks():
    t = PrettyTable()
    t.field_names =['Index number','Drink','Cost in £']
    for i, (x,s) in enumerate(zip(print_drinks(),get_cost_of_drinks())):
        t.add_row([i,x,s])
    print(t)
    #get_drink_options()

