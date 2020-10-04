import sys
import os

people = []
drinks = []
people_path = 'people_list.txt'
drinks_path = 'drinks_list.txt'
favourite_dict = 'fave_dictionary.txt'

class Person():
    def __init__(self,name):
        self.name = name  
    
class Drink_type(Person):
    def __init__(self,name,drink_type):
        super.__init__(name)
        self.drink_type = drink_type

class Alcoholic_drink_age(Drink_type):
    def __init__(self,name,drink_type,age):
        super.__init__(self,name,drink_type)
        self.age = age 
    
    def getAge(self):
        if self.age >= 18:
            string_age = str(self.age)
            print(f'you are {string_age}, therefore you can order a drink')
        else:
            print(f'you are not old enough to order an alcoholic drink')

class Drink_of_alcohol(Alcoholic_drink_age):
    def __init__(self,name,age,alcohol_drink):
            super().__init__(self,name,age)
            self.alcohol_drink = alcohol_drink
        
    def get_drink(self):
        print(f'Your chosen alcoholic drink is {self.alcohol_drink}')

class Soft_drink(Drink_type):
    def __init__(self,name,drink_type,soft_drink):
        super().__init__(self,name,drink_type)
        self.soft_drink = soft_drink

    def get_soft_drink(self):
        print(f'Your chosen soft drink is {self.soft_drink} ')


def data_from_file(path):
    data = []
    with open('path','r') as f:
        my_file = f.readlines()
        for i in my_file:
            data.append(i.strip())  #put space

def get_people_list(file_people):
    for name in data_from_file(file_people):
        people.append(Person(name))

    
      
def prompts_for_add_name():
    name_of_person = input(str('please enter your name you want to add:\n'))
    name_person = Person(name_of_person)
    return name_person
    
def add_name():
    if name_person not in people:
        people.append(name_person)
        with open 
    
    type_of_drink = input(str('Please type alcoholic or non alcoholic in reference to the drink you want to order'))
    Alcohol_or_not = Drink_type(name_person,type_of_drink)
    if Alcohol_or_not == 'alcoholic':
        age_of_person =input(int(f'You are buying an alcoholic drink,How old are you\n?'))
        call_alcoholic_age_class = Alcoholic_drink_age(name_person,Alcohol_or_not,age_of_person)
        call_alcoholic_age_class.getAge()
        name_drink = input(str('what drink do you desire\n'))
        call_alcohol_class = Drink_of_alcohol(name_person,age_of_person,name_drink)
        call_alcohol_class.get_drink
    elif Alcohol_or_not =='non alcoholic':
        soft_drink  = input(str('what soft drink to you want to order'))
        call_soft_drink_class = Soft_drink(name_person,type_of_drink,soft_drink)
        call_soft_drink_class.get_soft_drink()               
     
UNP = [1,2,3,4] #unique number people
UND = [1,2,3,4] #unique number drinks
dict_people = dict(zip(people,UNP))
dict_drinks = dict(zip(drinks,UND))


APP_NAME = 'Brew App'
MENU = f'''Welcome to {APP_NAME} v0.1!
Please, select an option by entering a number:
[1] Get all people
[2] Get all drinks
[3] Exit 
[4] Select a unique number corresponding to your name and drink of choice,this is added to the favourites dictionary
[5] add your name and drink of choice to the favourites list and overall people and drinks list
'''

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
    if os.path.exists(favourite_dict):
        append_write = 'a'
    else:
        append_write = 'w'
    with open(favourite_dict,append_write) as f:
        f.write(f"{name.rstrip('').lstrip('')}\n{drink.rstrip('').lstrip('')}\n")
        name_list =[]
        fave_drink =[]
        name_list.append(name)
        fave_drink.append(drink)
        fave_dict = (dict(zip(name_list,fave_drink)))
        print('this is your favourites entry')
        print(fave_dict)
    
def add_to_people_and_drinks(name,drink):
    with open(people_path,"a+") as f_people:
        if name not in f_people.read():
            f_people.write(name+"\n")
    with open(drinks_path,"a+") as f_drink:
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
                print_table('People',open_f_people('people_list.txt'))
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





   
    

    
    





    
    
