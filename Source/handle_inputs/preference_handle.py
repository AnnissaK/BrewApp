from Source.CSV_data_storage.save_csv import save_round
from Source.data_bases.saving_databases import insert_round_data

def age_restriction_for_preferences(age_of_person_name,age_of_owner,input_name,input_owner,drink):
    input_type = input('for you as the owner, is your favourite drink Alcoholic, enter y for yes and n for no?')
    if input_type=='y':
        integer_age_person = int("".join(map(str, age_of_person_name)))
        if integer_age_person<=18:
            print('you are not old enough to order your favourite drink')
        if age_of_owner <=18:
            print('you are not old enough to order your favourite drink')
        else: 
            print(f'you can buy your favourite drink ')
            insert_round_data(input_owner,input_name,drink)
    elif input_type =='n':
        print('There are no age restrictions on soft drinks')
        insert_round_data(input_owner,input_name,drink)