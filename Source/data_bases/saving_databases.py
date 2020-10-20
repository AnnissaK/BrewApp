import pymysql
from Source.people_list.people_to_append import people
from Source.data_bases.load_into_drinks import drinks
from Source.data_bases.round_list import round_variables
from Source.Classes.round_class import Round
from Source.Classes.favourites_class import Favourites
from Source.data_bases.preference_list import favourites_list
from Source.time_function.week_day import week_day
from Source.Classes.drink_and_people_class import Drink,Person

def handle_user_people(user_input):
    name_user = user_input.split()[0]
    age_user = user_input.split()[1]
    people_object = Person(name_user,age_user)
    people.append(people_object)
    if people_object in people:
        connection = pymysql.connect(
        host="localhost",
        port=33066,
        user="root",
        passwd="password",
        database="BrewApp"
    )
    cursor = connection.cursor()
    for i in people:
        if i == people[-1]:
            cursor.execute(f"INSERT INTO person(name,age) VALUES ('{i.name}','{i.age}')")
            connection.commit()
    cursor.close()
    connection.close()

def handle_user_drinks(user_input_drinks):
    try:
        user_drink_name = user_input_drinks.split()[0]
        user_type_drink = user_input_drinks.split()[1]
    except(IndexError) as e:
        print(f'{e}')
    drink_add_object = Drink(user_drink_name,user_type_drink)
    drinks.append(drink_add_object)
    if drink_add_object in drinks:
        connection = pymysql.connect(
            host="localhost",
            port=33066,
            user="root",
            passwd="password",
            database="BrewApp"
        )
        cursor = connection.cursor()
        for i in drinks:
            if i == drinks[-1]:
                cursor.execute(f"INSERT INTO Drinks_data(Drink_names,Drink_type,`Cost/£`) VALUES ('{i.drink}','{i.type}','{i.cost}')")
                connection.commit()
        cursor.close()
        connection.close()

def insert_round_data(owner_name,order_person,name_of_drink):
    connection = pymysql.connect(
            host="localhost",
            port=33066,
            user="root",
            passwd="password",
            database="BrewApp"
        )
    cursor= connection.cursor()
    r1 = Round(owner_name,week_day())
    r1.add_order(order_person,name_of_drink)
    round_variables.append(r1)
    # obj_orders =[obj.orders for obj in round_variables]
    # owners_list = [obj.owner for obj in round_variables]
    for i in round_variables:
        if i ==round_variables[-1]:
            owner_name = i.owner
            order_weekday = i.weekday
            order_dicts = i.orders
            for key,value in order_dicts.items():               
                cursor.execute(f"INSERT INTO Rounds(owner,name1,drink1,week_day) VALUES('{owner_name}','{key}','{value}','{order_weekday}')")
                connection.commit()
    cursor.close()
    connection.close()
    

    






def insert_into_favourites(input_name,input_drinks):
    connection = pymysql.connect(
        host="localhost",
        port=33066,
        user="root",
        passwd="password",
        database="BrewApp"
    )
    cursor= connection.cursor()
    F1 = Favourites(input_name)
    F1.add_to_favourites(input_name,input_drinks)
    favourites_list.append(F1)
    #obj_orders =[obj.fave_dict for obj in favourites_list]
    for i in favourites_list:
        if i == favourites_list[-1]:
            fave_dictionary = i.fave_dict
            for key,value in fave_dictionary.items():
                cursor.execute(f"INSERT INTO Favourites(name,favourites) VALUES('{key}','{value}')")
                connection.commit()
    cursor.close()
    connection.close()

