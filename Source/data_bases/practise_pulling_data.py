import csv
from csv import DictReader

import pymysql
from csv import DictReader
def connect_host():
    connection = pymysql.connect(
	host="localhost",
    port=33066,
	user="root",
	passwd="password",
	database="BrewApp"
	)
    return connection
    
def curser_connect():
    cursor = connect_host().cursor()
    return cursor

file_path = 'Source/data_bases/csv_load.csv'
def load_csv(file_path):
    data_list = []
    with open(file_path,'r') as csv_file:
        csv_reader = DictReader(csv_file)
        for row in csv_reader:
            data_list.append(row['Display Name'])
            string =' '.join((map(str,data_list)))
            x_names = string.split(' ')
            first_names=[]
            surnames=[]
            for i,x in enumerate(x_names):
                if i % 2 == 0:
                    first_names.append(x.title())
                else:
                    surnames.append(x.title())
        return surnames,first_names

print(load_csv(file_path))

def upload_data_to_database():
    for i,s in zip(load_csv(file_path)[1],load_csv(file_path)[0]):
        args = (i,s)
    curser_connect().execute("INSERT INTO practise_csv(`First Name`,Surname) VALUES(%s),(%s)",args)
    connect_host().commit()
    connect_host().close()
    curser_connect().close()




            

           



   
            
           
