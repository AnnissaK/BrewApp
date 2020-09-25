import sys
args = sys.argv
#unique_numbers_people = { person :'1' for person in people } only if assigning only one number


GET_PEOPLE = 'get-people'
GET_DRINK = 'get-drink'
people =['hubba','bubba','jam','wam']
drinks = ['vodka','champagne','sprite','crack']
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
[4] Enter your name and choose your favourite drink
[5] add your name and favourite drink to the list'''
#fix doesnt return to input because calls option- try making no input function and defining input command

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

def option_4_input():
    print(dict_people)
    name_person = int(input('Please select the number corresponding to your name as shown above: \n'))
    try:
        for key,value in dict_people.items():
            if name_person == value:
                key_value_people = key
                print(dict_drinks)
                fave_drink = int(input('Please select the number corresponding to your favourite drink from list above: \n'))
                for key,value in dict_drinks.items():
                    if fave_drink == value:
                        key_value_drinks = key
                        print(f"'{key_value_people} \'s favourite drink is '{key_value_drinks}'")
    
    except Exception as e:
        print(f"Exception occured'{e}'")

#people_dict[name]= (int(value_element)+1)
#print(people_dict)
#function will take a dictionary input and add a key value being the name and the corresponding value
#based on the values being numbers ranging from 1 to as many keys there are
#assuming fist inpt = name and second input = favourite drink
#sorted(x.keys())[-1] returns alphabetical order but list is ordered in terms of value


    



def add_dic (x,y):
    append = input('Enter your name and the drink you want to be added to the system:\n')
    name = append.split(',')[0]
    drink = append.split(',')[1]
    last_element = list(x.keys())[-1]
    value_element = x[last_element]
    x[name]=(int(value_element)+1)
    people.append(name)
    print(x)
    #for drink
    last_element=list(y.keys())[-1]
    value_element = y[last_element]
    y[drink]=(int(value_element)+1)
    drinks.append(drink)
    print(y)


def output(answer):
    while (len(sys.argv)>=1):
        try:
            if answer == 1:
                print_table('People',people)
                return_to_input()
            elif answer ==2:
                print_table('Drinks',drinks)
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





   
    

    
    




