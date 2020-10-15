from Source.data_bases.saving_databases import handle_user_people,handle_user_drinks

def add_name():
    try:
        user_input = input(str('add your name and age to the database separated by a space in the respective order:\n'))
    except (TypeError,ValueError) as e:
        print(f'{e}')
    handle_user_people(user_input)
    
    
                      
        
def add_drinks():
    try:
        user_input_drinks = input(str('''add the drink you want followed by a space with Non_Alcoholic or Alcoholic:
        PLEASE BE AWARE IF YOU DO NOT FOLLOW THE CORRECT FORMAT FOR DRINK TYPE YOU WILL BE CHARGED UNFAIRLY
        '''))
    except(TypeError,ValueError) as e:
        print(f'{e}')
    handle_user_drinks(user_input_drinks)
            