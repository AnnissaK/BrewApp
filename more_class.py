import sys
import os

class Person():
    def __init__(self,name):
        name_person = input(str(''))
        self.name = name_person
    
    def print_name(self):
        print(f'{self.name} is stored in the database')
    
    def get_user_input():
        while 1:
            name = input('enter you name:\n')
            return self(name)

    def getname(self):
        if os.path.exists('people_list.txt'):
            append_write = "a+"
        else:
            append_write ="w"
        with open('people_list.txt',append_write) as f:
            if self.name not in f.read():
                f.write(f'{self.name}+\n')
                people =[]
                for i in f.readlines():
                    people.append(i.strip())
                print(print_table('people',people)
    

                

    

# class Drink():
#     def __init__(self,drink):
#         self.drink = drink
        
#     def getDrink(self):
#             chosen_drink = input('enter chosen drink:\n')
#             chosen_drink = self.drink
#             print(f'{chosen_drink} is stored on reccord')
    

                
     
UNP = [1,2,3,4] #unique number people
UND = [1,2,3,4] #unique number drinks
dict_people = dict(zip(open_f_people('file_people.txt'),UNP))
dict_drinks = dict(zip(open_drink('file_drink.txt'),UND))


APP_NAME = 'Brew App'
MENU = f'''Welcome to {APP_NAME} v0.1!
Please, select an option by entering a number:
[1] Get all people
[2] Get all drinks
[3] Exit 
[4] Select a unique number corresponding to your name and drink of choice,this is added to the favourites dictionary
[5] add your name and drink of choice to the favourites list and overall people and drinks list'''

def input_command():
    print(MENU)
    answer = (int(input('what is your option?: \n')))
    output(int(answer))


def return_to_input():
    escape = int(input('press one to return to input command\n'))
    try:
        if escape == 1:
            input_command()
        else:
            print('please press one \n')
    except ValueError:
        print('An integer please\n')

def print_table(title,data):
    width = width_table(title,data)
    print_header(title,width)
    for item in data:
        print(f'| {item}')
    seperator(width)
    
def print_header(title,width):
    seperator(width)
    print(f'| {title.upper()}')
    seperator(width)

def seperator(width):
    print(f"+ {'='* width}")

def width_table(title,data):
    longest =len(title)
    for item in data:
        if len(item)> longest:
            longest = len(item)
    return longest

def fave_dict_load_file(name, drink):
    if os.path.exists('fave_dictionary.txt'):
        append_write = 'a'
    else:
        append_write = 'w'
    with open('fave_dictionary.txt',append_write) as f:
        f.write(f"{name.rstrip('').lstrip('')}\n{drink.rstrip('').lstrip('')}\n")
        name_list =[]
        fave_drink =[]
        name_list.append(name)
        fave_drink.append(drink)
        fave_dict = (dict(zip(name_list,fave_drink)))
        print('this is your favourites entry')
        print(fave_dict)
    
def add_to_people_and_drinks(name,drink):
    with open("file_people.txt","a+") as f_people:
        if name not in f_people.read():
            f_people.write(name+"\n")
    with open("file_drink.txt","a+") as f_drink:
        if drink not in f_drink.read():
            f_drink.write(drink +"\n")

#use a+ to read and wrie files
        
def option_4_input():
    print(dict_people)
    unique_number_of_person = int(input('Please select the number corresponding to your name as shown above: \n'))
    try:
        for key,value in dict_people.items():
            if unique_number_of_person == value:
                key_value_people = key
                print(dict_people)
            else:
                print('if your name is not on the list you can add your name by selecting 5 on main menu')
                return_to_input()
        unique_number_drinks = int(input('Please select the number corresponding to your drink of choice from list above: \n'))
        for key,value in dict_drinks.items():
            if unique_number_drinks == value:
                key_value_drinks = key
                print(dict_drinks)
                print(f"'{key_value_people} \'s drink of choice is '{key_value_drinks}'")
            else:
                print('if your favourite drink is not on the list you can add your desired drink by selecting 5 on main menu')
                return_to_input()
        fave_dict_load_file(key_value_people, key_value_drinks)
        
    except Exception as e:
        print(f"Exception occured'{e}'")

#function will take 2 dictionary inpust and add a key value being the name and the corresponding value
#based on the values being numbers ranging from 1 to as many keys there are
#assuming fist inpt = name and second input = favourite drink
#sorted(x.keys())[-1] returns alphabetical order but list is ordered in terms of value       

def add_dic (x,y):
    append = input('Enter your name and your favourite drink you want to be added to the system:\n')
    name = append.split(',')[0]
    drink = append.split(',')[1]
    fave_dict_load_file(name, drink)
    add_to_people_and_drinks(name, drink)
    if name not in dict_people.keys():
        last_element = list(x.keys())[-1]
        value_element = x[last_element]
        x[name]=(int(value_element)+1)
        name_command = input(str((f"are you happy for '{name}' to be added to the people list?")))
        if (name_command == 'yes'):
            print(x)
        elif (name_command == 'no'):
            del x[name]
            print(x)
    else:
        print('name already in system')
        option_4_input()
    #for drink
    if drink not in dict_drinks.keys():
        last_element=list(y.keys())[-1]
        value_element = y[last_element]
        y[drink]=(int(value_element)+1)
        drink_command = input(str((f"are you happy for '{drink}' to be added to the drinks list?")))
        if drink_command =='yes':
            print(y)
        elif drink_command =='no':
            del y[drink]
            print(y)
    else:
        print('drink is already on the list')
        option_4_input()
    
def output(answer):
    while (len(sys.argv)>=1):
        try:
            if answer == 1:
                P1 = Person.get_user_input()
                P1.print_name()
                return_to_input()
            elif answer ==2:
                print_table('Drinks',open_drink('file_drink.txt'))
                return_to_input()
            elif answer ==3:
                exit()
            elif answer ==4:
                option_4_input()
                return_to_input()
            elif answer ==5:
                add_dic(dict_people,dict_drinks)
                return_to_input()
        except ValueError as e:
            print(f"ValueError occured'{e}'" )

input_command()
