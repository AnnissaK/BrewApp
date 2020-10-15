from Source.printing_functions.printing_outputs import print_people,print_drinks,print_previous_orders,favourites_menu,favourites_prompts,print_ID
from Source.printing_functions.print_table_items import print_table
from Source.handle_inputs.add_drinks_and_name import add_name,add_drinks
from Source.data_bases.round_list import round_variables
from Source.time_function.week_day import week_day
from Source.data_bases.saving_databases import insert_round_data
from Source.people_list.people_to_append import people
from Source.data_bases.load_into_drinks import drinks
from Source.handle_inputs.round_handle_functions import get_name_of_person,get_preferred_drinks,round_handle_user_input,round_handle_drinks
from Source.time_function.week_day import week_day
from prettytable import PrettyTable
#from Source.handle_inputs.preference_handle import get_preferred_drinks,get_drink_options,handle_regular_customer

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
extra_round_names =[]
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

def pretty_table(title,list_data):
    t= PrettyTable()
    t.field_names =['Index number',title]
    for i,x in enumerate (list_data):
        t.add_row([i,x.title()])
    print(t)

def print_people_out(Id_number,list_data):
    t = PrettyTable()
    t.title='People list'
    t.field_names =['Person ID','People names']
    for i,x in zip(Id_number,list_data):
        t.add_row([i,x])
    print(t)

def output(answer):
    while True:
        if answer == 1:
            print_people_out(print_ID(),print_people())
            return_to_input()
        elif answer ==2:
            pretty_table('Drinks',print_drinks())
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


def week_day_selection():
    input_owner =input('can you reconfirm whos buying the round \n')
    input_name = input('can you please re-confirm your name?\n')
    owner =handle_owner_confirmation(input_owner)
    orderee =handle_owner_confirmation(input_name)
    orders= [obj.orders for obj in round_variables if obj.weekday == week_day()]
    for i in orders:
        for key,value in i.items():
            if key ==orderee:
                print(value)
                choose_drink = input("Please confirm you want to re-order the drink above , type y for yes and n for no\n")
                drink_of_choice =handle_owner_confirmation(choose_drink)
                if drink_of_choice == 'n':
                    print('return to main menu and select your round manually')
                    return_to_input()
                elif drink_of_choice== 'y':
                    insert_round_data(owner,orderee,value)
                    return_to_input()
            else:
                print(f"You have no prior orders for this '{week_day()}' so you will be returned to the main menu")
                return_to_input() 
    
def handle_owner_confirmation(x):   
    return x



def handle_regular_customer(regular_customer):
    if regular_customer == 'y':
        week_day_selection()
    else:
        return_to_input()
    


def round_class_dictionary():
    owner_name =get_name_of_person(round_handle_user_input('round owner',print_people()),print_people())
    order_person = get_name_of_person(round_handle_user_input('owners orderees name',print_people()),print_people())
    round_handle_drinks()
    input_number=input('''You have 3 options:
    a)Select the number corresponding to the drink you want
    b)if you want your favourite drink select a number out of the range 
    c) see weekly preferences by entering 100 \n''')
    integer_input_number = int(input_number)
    if integer_input_number ==100:
        regular_customer =input('Are you a regular customer? If so, would you like to re-order what you ordered on this day last week. If yes type y if not type n \n?')
        handle_regular_customer(regular_customer)
    elif integer_input_number > len(print_drinks()):
        print('y')
        get_preferred_drinks()
    elif integer_input_number<= len(print_drinks()):
        output_in_drinks_list(integer_input_number)
        owner_age=[person.age for person in people if person.name == owner_name]
        order_person_age =[person.age for person in people if person.name ==order_person]
        drink_type =[drink.type for drink in drinks if drink.drink ==output_in_drinks_list(integer_input_number)]
        dict_order_owner = dict(zip(drink_type,owner_age))
        dict_order = dict(zip(drink_type,order_person_age))
        for (k1,v1),(k2,v2) in zip(dict_order_owner.items(),dict_order.items()):
                if k1== 'Alcoholic':
                    if int(v1) < 18:
                        print('it is illegal for you as the owner to buy the round because you are underage')
                    elif k2 =='Alcoholic':
                        if int(v2) < 18:
                            print('it is illegal to buy to an alcoholic drink even if the person buying your round is over 18')
                        else:
                            insert_round_data(owner_name,order_person,output_in_drinks_list(integer_input_number))
                else:
                    print('there is no age restrictions for your drink')
                    insert_round_data(owner_name,order_person,output_in_drinks_list(integer_input_number))
                


def output_in_drinks_list(x):
    index = x
    element_value =print_drinks()[index]
    return element_value


