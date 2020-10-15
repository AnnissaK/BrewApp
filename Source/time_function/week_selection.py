from Source.data_bases.round_list import round_variables
from Source.time_function.week_day import week_day
from Source.data_bases.saving_databases import insert_round_data


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
