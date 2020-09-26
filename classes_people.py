class Person():
     def __init__(self,name):
         self.name = name
drinks =[]
people =[]
# people=[]
# name =['bil','bob','susan']

# for i in name:
#     people.append(Person(name))
# print([person.name for person in people])

# def hello():
#     input1 = input('entehr')
#     input2 = input('enen')
#     input3 = input('engjt')
#     return input1,input2,input3
# hello()[0]

# def round_handle_user_input(list_data,element):
#     for i,x in enumerate (list_data):
#         print(i,x)
#     input_number = input(f'Select the number corresponding to the {element} you want from the list \n')
#     return input_number
    
# def get_name_of_person(name,list_data):
#     index = int(name)
#     element_value =list_data[index]
#     return element_value

# def handle_round_input():
#     owner_name =get_name_of_person(round_handle_user_input(print_people(),'round owner'),print_people())
#     order_person = get_name_of_person(round_handle_user_input(print_people(),'owners orderees name'),print_people())
#     name_of_drink =get_name_of_person(round_handle_user_input(print_drinks(),'drink'),print_drinks())
#     return owner_name,order_person,name_of_drink

def load_people():
    for i,s in zip(load_into_list(file_people_list,'name'),load_into_list(file_people_list,'age')):
        people.append(Person(i,s))
    
        
def print_people():
    people_names = [person.name for person in people]
    return people_names

def get_age_of_person():
    person_age = [person.age for person in people]
    return person_age

  
def print_drinks():
    drinks_name = [drink_name.drink for drink_name in drinks]
    return drinks_name

def get_type_of_drink():
    type_of_drink = [typedrink.type for typedrink in drinks]
    return type_of_drink




def load_into_round_class(x,y,z):
    order_requests=[]
    for owner,name,drink in zip(x,y,z):
        R1=Round(owner)
        R1.add_order(name,drink)
        order_requests.append(R1)
    return order_requests



def round_handle_user_input(list_data,element):
    for i,x in enumerate (list_data):
        print(i,x)
    input_number = input(f'Select the number corresponding to the {element} you want from the list \n')
    return input_number
    
def get_name_of_person(name,list_data):
    index = int(name)
    element_value =list_data[index]
    return element_value

def handle_round_input():
    owner_name =get_name_of_person(round_handle_user_input(print_people(),'round owner'),print_people())
    order_person = get_name_of_person(round_handle_user_input(print_people(),'owners orderees name'),print_people())
    name_of_drink =get_name_of_person(round_handle_user_input(print_drinks(),'drink'),print_drinks())
    return owner_name,order_person,name_of_drink
    
print(handle_round_input())