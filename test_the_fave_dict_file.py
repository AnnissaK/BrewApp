import os
def fave_dict_load_file(name, drink):
    if os.path.exists('fave_dict.txt'):
        append_write = 'a'
    else:
        append_write = 'w'
    with open('fave_dictionary.txt',append_write) as f:
        f.write(f"{name.rstrip('').lstrip('')} \n {drink.rstrip('').lstrip('')} \n")
        name_list =[]
        fave_drink =[]
        name_list.append(name)
        fave_drink.append(drink)
        fave_dict = (dict(zip(name_list,fave_drink)))
        print(fave_dict)

fave_dict_load_file('anne', 'coke')