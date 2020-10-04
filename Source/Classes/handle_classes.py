from Source.printing_functions.printing_outputs import print_people,get_cost_of_drinks,print_drinks
from prettytable import PrettyTable

def round_handle_user_input(list_data,element):
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
    input_number = input('Select the number corresponding to the drink you want from the list,if your name is not on the list select a number outside the range given \n')
    return input_number