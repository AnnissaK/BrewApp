#people list empty and drinks in function
#person.name is like the name of objec could be anthing you iteratig through objects when do person.name for person in people
from table import print_table
import sys
import classes 
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
people = []
drinks=[]
favourites_dict = {}

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
    print(print_people)
    try:
        input_round = input(str('who will be buying the round of drinks?\n'))
    except ValueError:
        print('enter a word please not an integer')
    round1 = classes.Round(input_round)
    try:
        input_name = input(str('name of people you are buying for seprated by spaces?\n'))
    except ValueError:
        print('enter a word please not an integer')
    input_list_name= input_name.split()
    print(drinks)
    try:
        input_drink = input(str('enter the corresponding drinks that the people would like to order\n'))
    except ValueError:
        print('please enter a word please not an integer')
    input_list_drink = input_drink.split()
    for name,drink in zip(input_list_name,input_list_drink):
        round1.add_order(name,drink)
        #round1.print_order()

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
    favourites = classes.Favourites(input_name)
    favourites.add_to_favourites(name,drink)
    favourites.print_favourites()
    favourites_dict[input_name]=input_drinks
    print(favourites_dict)

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
# #          append_write ="w+"
# #      with open("people_list.txt",append_write) as f:
# #          if call_people() not in f.read():
# #              f.write(f'{call_people()}+\n')       
        