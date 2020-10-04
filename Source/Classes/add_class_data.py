from Source.people_list.people_to_append import people
from Source.Classes.round_class import Round
from Source.Classes.drink_and_people_class import Person
from Source.Classes.favourites_class import Favourites
#from Source.Classes.favourites_class import Favourites

def add_faves_class(x,y):
    favourites1=[]
    for i,s in zip(x,y):
        F1 =Favourites(i)
        F1.add_to_favourites(i,s)
        favourites1.append(F1)
    return favourites1

def load_into_round_class(x,y,z):
    order_requests=[]
    for owner,name,drink in zip(x,y,z):
        R1=Round(owner)
        R1.add_order(name,drink)
        order_requests.append(R1)
    return order_requests

def load_people(x,y):
    for i,s in zip(x,y):
        people.append(Person(i,s))
    return people
