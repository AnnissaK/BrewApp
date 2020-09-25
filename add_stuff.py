import csv
from unittest.mock import Mock,patch
from copy_working_classes import round_handle_user_input
from csv import reader
from csv import writer
from csv import DictReader
from table import print_table
import classes
from classes import Person
from classes import Favourites
import re


# file_people_list = 'person.csv'
# file_drink_list = 'drinks.csv'
# people =[]
# drinks =[]

# drink_age = ['22']
# drink_name =['Alcoholic']
# drink_owner=['Alcoholic']
# drink_age_owner =['13']

# dict_order_owner = dict(zip(drink_owner,drink_age_owner))
# dict_order = dict(zip(drink_name,drink_age))
# for (k1,v1),(k2,v2) in zip(dict_order_owner.items(),dict_order.items()):
#     if k1== 'Alcoholic':
#         if int(v1) <=18:
#             print('it is ilegal for you as the owner to buy the round because you are underage')
#     if k2 =='Alcoholic':
#         if int(v2) <=18:
#             print('it is ilegal to buy to an alcoholic drink even if the person buying your round is over 18')
#     else:
#         print('there is no age restrictions for your drink')



# class load_and_save_data_from_csv():
#     def __init__(self,filename):
#         self.filename = filename
#         self.data_list = []
        

#     def load_into_list(self,header):
#         with open(self.filename,'r') as csvfile:
#             csv_dict_reader = DictReader(csvfile)
#             for row in csv_dict_reader:
#                 self.data_list.append(row[header])
#             return self.data_list

# def load_into_round_csv():
#     r1 = load_and_save_data_from_csv('favourites_dictionary.csv')
#     r1.load_into_list('name')
#     print(r1.data_list)

# def load_into_list(filename,header):
#     data_list =[]
#     with open(filename,'r') as csvfile:
#         csv_dict_reader = DictReader(csvfile)
#         for row in csv_dict_reader:
#             data_list.append(row[header])
#         print(data_list)

# # load_into_list('drinks.csv','Drinks')
# def load_into_list(filename,header):
#     data_list =[]
#     with open(filename,'r') as csvfile:
#         csv_dict_reader = DictReader(csvfile)
#         for row in csv_dict_reader:
#             data_list.append(row[header])
#         return data_list

# def load_people():
#     for i,s in zip(load_into_list(file_people_list,'name'),load_into_list(file_people_list,'age')):
#         people.append(classes.Person(i,s))

# def favourites_prompts():
#     # print(print_people())
#     try:
#         input_name = input(str('pick a name from the list of people\n'))
#         age =[person.age for person in people if person.name==input_name]
#         print(age)
#     except ValueError:
#         print('enter a string')
#     #if input_name not in print_people():
#         # print('add name to list by selecting option 4')
#     try:
#         # print(print_drinks())
#         input_drinks = input(str('pick favourite drink from the list of drinks\n'))
#     except ValueError:
#         print('enter a string')
#     # if input_drinks not in print_drinks():
#         # print(' add a drink to the list by selecting 5')
# load_people()
# favourites_prompts()












# load_into_round_csv():
# file_people_list = 'person.csv'
# people =[]
# def load_into_list(filename,header):
#     data_list =[]
#     with open(filename,'r') as csvfile:
#         csv_dict_reader = DictReader(csvfile)
#         for row in csv_dict_reader:
#             data_list.append(row[header])
#         return data_list

# def load_people():
#     load_into_list(file_people_list,'name')
#     load_into_list(file_people_list,'age')
#     for i,s in zip(load_into_list(file_people_list,'name'),load_into_list(file_people_list,'age')):
#         people.append(classes.Person(i,s))


# load_people()
    

# def get_people_names():
#     person_names = [person.name for person in people]
#     print(person_names)

# def get_age_of_person():
#     person_age = [person.age for person in people]
#     print(person_age)


# def input1():
#     x=input('heknde yeah')
#     y=x.split()[0]
#     print(y)

# input1()

# first_column =[]
# second_column=[]
# third_column =[]


# class load_data_from_csv():
#     def __init__(self,filename):
#         self.data_list = []
#         self.value_list =[]
#         self.filename = filename
    
#     def load_into_list(self,filename):
#         with open(filename,'r') as csvfile:
#             csv_dict_reader = DictReader(csvfile)
#             for i in csv_dict_reader:
#                 self.data_list.append(i)
    
#     def deal_with_list(self):
#         for d in self.data_list:
#             for value in d.values():
#                 self.value_list.append(value)
    

# def call_class(filepath):
#     r1= load_data_from_csv(filepath)
#     r1.load_into_list(filepath)
#     r1.deal_with_list()
#     r1.value_list
#     return r1.value_list

# def get_favourites_column(filename):
#     first_column =[]
#     for i,x in enumerate (call_class(filename)):
#         if i % 3 ==0:
#             first_column.append(x)
#         elif i % 2 ==0:
#             second_column.append(x)
#         else:
#             third_column.append(x)
    

# get_favourites_column('favourites_dictionary.csv')
# print(first_column) 
# print(second_column)
# print(third_column)






    
    
# get_first_column()
                #for value in row.values():
                    #print(value)
            #         self.data_list.append(value)
            # print(self.data_list)
      
# r1=load_data_from_csv('favourites_dictionary.csv')
# r1.load_into_list('favourites_dictionary.csv')
# r1.deal_with_list()
# r1.value_list


# def specific_func_fave():
#     drink =[]
#     r1=load_and_save_data_from_csv('favourites_dictionary.csv')
#     r1.load_into_list()
#     for i,x in enumerate r1.data_list:
#         if index % 2 ==0:
#             drink.append(x)
#             print(x)

    
   
                #self.data_list.append(row['header'])
                   
    
            # for i in header:
            #     for row in csv_dict:
            #     print(row)
            #     print(header)
            #     self.data_list.append(row[str(header_string)])
            # return self.data_list






# round_file = 'round.csv'

# # def load_csv_data_owner(filename):
# #     with open(filename,'r') as csv_file:
# #         owner_name=[]
# #         csv_reader = csv.reader(csv_file)
# #         header = next(csv_file)
# #         if header != None:
# #             for row in csv_file:
# #                 owner_name.append(row['owner'])
# #         print(owner_name)

# def load_csv_owner():
#     with open('round.csv','r') as read_obj:
#         owner_list = []
#         csv_dict_reader = DictReader(read_obj)
#         for row in csv_dict_reader:
#             owner_list.append(row['owner'])
#         return owner_list

# def load_csv_name():
#     with open('round.csv','r') as read_obj:
#         name_list = []
#         csv_dict_reader=DictReader(read_obj)
#         for row in csv_dict_reader:
#             name_list.append(row['name'])
#         return name_list

# def load_csv_drink():
#     with open('round.csv','r') as read_obj:
#         drink_list = []
#         csv_dict_reader=DictReader(read_obj)
#         for row in csv_dict_reader:
#             drink_list.append(row['drink'])
#         return drink_list


# def load_into_round_class():
#     order_requests=[]
#     for i,name,drink in zip(load_csv_owner(),load_csv_name(),load_csv_drink()):
#         R1=classes.Round(i)
#         R1.add_order(name,drink)
#         order_requests.append(R1)
#     return order_requests


# load_into_round_class()   
#     for name,drink in zip(load_csv_name(),load_csv_drink()):
#         R1.add_order(name,drink)
#         order_requests.append(R1)
    # return order_requests


# def add_order_request():
#     # order_request=[]
#      for name,drink in zip(load_csv_name(),load_csv_drink()):
#     print(load_into_round_class())
#         # print(order_request)



    # for name, drink in zip(load_csv_name(),load_csv_drink()):
    #     R2=load_into_round_class().add_order(name,drink)
    #     order_request.append(R2)
    # print(order_request) 
                
        #     R1.add_order(name,drink)
        #     order_request.append(R1)
        #  return order_request    


# def load_csv_orders_data():
#     with open(round_file,'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)
#         order_value = []
#         for row in csv_reader:
#             order_value.append(row[1])
#         print(order_value)
#             order_value.append(row)
#         return order_value

# def into_round_class():
#     for i in load_csv_owner_data():
#         R1 = classes.Round(i)
#     for i in load_csv_orders_data



# def get_round_list():
#     round_list = load_csv_data(round_file)
#     return round_list

        # orders.append(R1.orders)

# def print_previous_orders():
#     orders_dict=[obj.orders for obj in load_into_round_class()]
#     owners_list = [obj.owner for obj in load_into_round_class()]
#     items =[]
#     for d in orders_dict:
#         for key in d:
#             items.append((f'{key}\'s ordered {d[key]}'))
#     for i,x in zip(owners_list,items):
#         print(f'{i.upper()}\'s ROUND : {x}')
            

# print_previous_orders() 
   
   
   
   
    # order_names =[obj.owner for obj in load_into_round_class()]
    # order_reccord=[obj.orders for obj in load_into_round]
    # print(order_reccord)
    # items =[]
    # for i in order_names:
    #     for d in order_reccord:
    #         for key in d:
    #             items.append((f'{key } ordered {d[key]}'))
    #             print_table(i,items)
















# def load_name_fave():
#     with open(fave_dictionary,'r') as csvfile:
#         csv_reader = csv.reader(csvfile)
#         name =[]
#         for row in csv_reader:
#             name.append(row[0])
#         return name
            #name,drink = row
            # classes.Favourites(row[0])
            # f1.add_to_favourites(row[0],row[1])
            # #f1.print_favourites()
            # for key,value in f1.fave_dict.items():
            #     fave_menu[key]=value
# def load_drinks_fave():
#     with open(fave_dictionary,'r') as csvfile:
#         csv_reader = csv.reader(csvfile)
#         fave_drinks =[]
#         for row in csv_reader:
#             fave_drinks.append(row[1])
#         return fave_drinks


# def add_faves_class():
#     for i,s in zip(load_name_fave(),load_drinks_fave()):
#         F1 =classes.Favourites(i)
#         F1.add_to_favourites(i,s)
#         favourites1.append(F1)
#     return favourites1

# def favourites_menu():
#     favourite=[obj.fave_dict for obj in favourites1]
#     items =[]
#     for d in favourite:
#         for key in d:
#             items.append((f'{key}\'s favourite drink is {d[key]}'))
#     print_table('Favourites',items)
        
# add_faves_class()
# favourites_menu()        















# owners_round=[]
# round_file = 'round.csv'
# order_request=[]

# class Round():
#     def __init__(self,owner):
#         self.owner = owner
#         self.orders = {}
    
#     def add_order(self,name,drink):
#             self.orders[name]=drink


#     def return_items(self):
#         items = []
#         for name,drink in self.orders.items():
#             items.append(f'{name},{drink}')
        
#         print_table(f"{self.owner}'s round",items)

# def load_csv_data(filename):
#     with open(filename,'r') as csv_file:
#         raw_data = []
#         csv_reader = csv.reader(csv_file)
#         for row in csv_reader:
#             raw_data.append(row)
#         return raw_data


# def get_round_list():
#     round_list = load_csv_data(round_file)
#     return round_list

# def load_into_round_class():
#     for list in get_round_list():
#         R1=Round(list[0])
#         owners_round.append(R1)
#         R1.add_order(list[1],list[2])
#         order_request.append(R1)
#         #orders.append(R1.orders)

# def print_previous_orders():
#     order_names = [person.owner for person in owners_round]
#     order_menu = [request.orders for request in order_request]
#     for i in order_names:
#         for d in order_menu:
#             for key in d:
#                 output=(f'{key} {d[key]}')
#         print_table(i,output)
    
# load_into_round_class()
# print_previous_orders()


