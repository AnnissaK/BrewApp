
#def name_function(x):
    #x = input('Enter list of people':)
    #get_people = list(x)
    #return(get_people)

#def drink_function(y):
    #y = input('enter list of drinks:')
    #get_drinks = list(y)
    #return(get_drinks)
    #return (favourite_drinks)
#print(drink_function(['coke','sprite','vodka','iron-bru']))
import sys
args = sys.argv

GET_PEOPLE = 'get-people'
GET_DRINK = 'get-drink'
peoples =['h','i','j','k']
drinks = ['f','g','k','l']

if len(sys.argv)< 2:
    print('need more input')
    exit()
elif len(sys.argv)> 2: 
    print('can only do one at time')
    exit()

def print_table(title,data):
    width = width_table(title,data)
    print_header(title,width)
    for item in data:
        print(f'| {item}')
    seperator(width)
    


def print_header(title,width):
    seperator(width)
    print(f'| {title}')
    seperator(width)

def seperator(width):
    print(f"+ {'='* width}")


def width_table(title,data):
    longest =len(title)
    for item in data:
        if len(item)> longest:
            longest = len(item)
    return longest


command = args[1]
try:
    if command == GET_PEOPLE:
        print_table('People',peoples)
            #print('+====================\n|'+ person + '\n+=================')
            #call function
    elif command == GET_DRINK:
        print_table('Drinks',drinks)
            #print('+================\n' + drink + '\n+===================' )
except:
    print(f'"{command}" is not an command that I recognise.')



    
