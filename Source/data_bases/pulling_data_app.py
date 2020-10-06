from Source.Classes.drink_and_people_class import Drink,Person
from Source.Classes.round_class import Round
import pymysql

def connection_f():
    connection = pymysql.connect(
    host="localhost",
    port=33066,
    user="root",
    passwd="password",
    database="BrewApp"
	)
    return connection

# Drinks_title = 0
# Drinks_type_title=1
# Drinks_cost = 2

def get_data_base(table,Y):
    data_list =[]
    cursor = connection_f().cursor()
    cursor.execute(f'SELECT * FROM {table}')
    while True:
        data_info = cursor.fetchone()
        if not data_info:
            break
        data_list.append(Y(data_info[0],data_info[1],data_info[2]))
        #insert cost into class-call the function in drinks class-for adding new drinks
    connection_f().commit()
    cursor.close()
    connection_f().close()
    return data_list


def get_data_base_people(table,Y):
    data_list =[]
    cursor = connection_f().cursor()
    cursor.execute(f'SELECT * FROM {table}')
    while True:
        data_info = cursor.fetchone()
        if not data_info:
            break
        data_list.append(Y(data_info[0],data_info[1]))
        #insert cost into class-call the function in drinks class-for adding new drinks
    connection_f().commit()
    cursor.close()
    connection_f().close()
    return data_list

def get_data_round(table,Y):
    data_list =[]
    cursor = connection_f().cursor()
    cursor.execute(f'SELECT * FROM {table}')
    while True:
        data_info = cursor.fetchone()
        if not data_info:
            break
        r1 =(Y(data_info[0]))
        r1.add_order(data_info[1],data_info[2])
        data_list.append(r1)
        #insert cost into class-call the function in drinks class-for adding new drinks
    connection_f().commit()
    cursor.close()
    connection_f().close()
    return data_list








# def get_data_base_multiple(Y,table,*argv):
#     data_list =[]
#     cursor = connection_f().cursor()
#     cursor.execute(f'SELECT * FROM {table}')
#     while True:
#         data_info = cursor.fetchone()
#         if not data_info:
#             break
#         list_index=[]
#         for arg in argv:
#             #arg+=1
#             list_index.append(arg)
#             data_list.append(Y(data_info[list_index[arg]],data_info[list_index[arg]]))
#             if arg == (len(list_index)-1):
#                 break 
#     connection_f().commit()
#     cursor.close()
#     connection_f().close()
#     print(data_list)
#     for i in data_list:
#         print(i.age)
    
# get_data_base_multiple( Person,'person',0, 1)

 



    
