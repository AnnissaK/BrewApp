#FOREGIN KEY TO ADD-PRIMARY KEY ID IN PERSON TABLE AS WELL


def get_data_round(table,Y):
    data_list =[]
    data_drink =[]
    data_person=[]
    cursor = connection_f().cursor()
    cursor.execute(f'SELECT * FROM {table}')
    while True:
        data_info = cursor.fetchone()
        if not data_info:
            break
        r1 =(Y(data_info[0],data_info[13]))
        data_list_info =list(data_info[1:13])
        for i in range(1,13):
            if i%2 == 0:
                data_drink.append(data_info[i])
            elif i%2 !=0:
                data_person.append(data_info[i])
        # print(data_drink)
        # print(data_person)
        #print(data_person)
            for i,x in zip(data_person,data_drink):
                r1.add_order(i,x)
        data_list.append(r1)
        #insert cost into class-call the function in drinks class-for adding new drinks
    connection_f().commit()
    cursor.close()
    connection_f().close()
    for i in data_list:
        print(i.orders)


def enter_number_of_rounds(input_number_people):
    enter_name_of_people = input(f"Enter the ID corresponding to the person you are buying a drink for this should run '{input_number_people}' times , each time enter one name at a time\n")
    return enter_name_of_people

def enter_number_of_drinks(input_number_people):
    enter_name_of_people = input(f"Enter the number corresponding to the drinks you are buying for each person this should run '{input_number_people}' times , each time enter one drink at a time\n")
    return enter_name_of_drink

def input_round():
    input_number_people = input('how many people do you wish to buy for\n?')
    if int(input_number_people) > 6:
        print('Due to covid restrictions one of you should go home')
    elif int(input_number_people)<=6:
        for i in range(int(input_number_people)):
            round_names.append(enter_number_of_rounds(input_number_people))
            round_drinks.append(enter_number_of_rounds(input_number_people)) 


