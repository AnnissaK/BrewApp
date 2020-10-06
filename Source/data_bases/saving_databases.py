import pymysql
from Source.people_list.people_to_append import people
from Source.data_bases.load_into_drinks import drinks
from Source.data_bases.round_list import round_variables
from Source.Classes.round_class import Round
def handle_user_people(user_input):
    name_user = user_input.split()[0]
    age_user = user_input.split()[1]
    if name_user not in print_people():
        cursor = connection_f().cursor()
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
    user_drink_name = user_input_drinks.split()[0]
    user_type_drink = user_input_drinks.split()[1]
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
                cursor.execute(f"INSERT INTO Drinks(Drink,Drink_type,`Cost / £`) VALUES ('{i.drink}','{i.type}','{i.cost}')")
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
    r1 = Round(owner_name)
    r1.add_order(order_person,name_of_drink)
    round_variables.append(r1)
    for i in round_variables:
        if i ==round_variables[-1]:
            obj_orders =[obj.orders for obj in round_variables]
            owners_list = [obj.owner for obj in round_variables]
            for i in owners_list:
                for d in obj_orders:
                    for key in d:
                        cursor.execute(f"INSERT INTO Rounds(owner,name,drink) VALUES('{i}','{key}','{d[key]}')")
                        connection.commit()
    cursor.close()
    connection.close()