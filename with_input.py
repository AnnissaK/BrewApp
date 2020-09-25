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
[4] Enter your name and choose your favourite drink'''
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
        print("Exception occured: {}".format(e))
            
    

def output(answer):
    while (len(sys.argv)>=1):
        if answer == 1:
            print_table('People',people)
            return_to_input()
        elif answer ==2:
            print_table('Drinks','drinks')
            return_to_input()
        elif answer ==3:
            exit()
        elif answer ==4:
            option_4_input()
            return_to_input()
            


input_command()





   
    

    
    




