#have to go back to file and put curser on next line or throws error
#generic function
import datetime
import calendar
import csv
import sys
from csv import DictReader, reader, writer
import pymysql
from prettytable import PrettyTable
from Source.Classes.add_class_data import (add_faves_class,load_into_round_class, load_people)
from Source.Classes.drink_and_people_class import Drink, Person
from Source.Classes.favourites_class import Favourites
from Source.Classes.round_class import Round
from Source.CSV_data_storage.csv_load_data import load_into_list
from Source.CSV_data_storage.save_csv import save_csv_items, save_round
from Source.people_list.people_to_append import people
from Source.printing_functions.print_table_items import print_table
from Source.data_bases.load_into_drinks import drinks                                                   
from Source.data_bases.pulling_data_app import connection_f
from Source.data_bases.saving_databases import handle_user_people,handle_user_drinks,insert_round_data
from Source.data_bases.preference_list import favourites_list
from Source.main_part.menu_handler import menu_option,output,return_to_input
from PIL import Image
# img = Image.open('soft-drinks.jpg')
# img.show()

#from Source.main_part.return_input import return_to_input


#file_people_list = 'Source/CSV_data_storage/person.csv'
#file_drink_list = 'Source/CSV_data_storage/drinks.csv'
#people = []
#fave_dictionary='Source/CSV_data_storage/favourites_dictionary.csv'
#drinks=[]
#fave_menu = {}


    

if __name__ == "__main__":
    # start()
    menu_option()
    
