import csv
from csv import DictReader
from csv import reader
import pymysql
#import Names.txt
file = 'test_csv_pymysql'
#def main():
connection = pymysql.connect(
host="localhost",
port=33066,
user="root",
passwd="password",
database="BrewApp"
)

file_path = 'Source/data_bases/csv_load.csv'
cursor = connection.cursor()
with open(file_path,'r') as csv_file:
    csv_data = csv.reader(csv_file)
    next(csv_data)
    for row in csv_data:
        cursor.execute("INSERT INTO practise_csv(`User Name`,Name,`Display Name`,`Job Title`,Department,`Office Number`,`Office Phone`,`Mobile Phone`,Fax,Address,City,`State or Province`,`ZIP or Postal Code`,`Country or Region`)\
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)

connection.commit()
cursor.close()
connection.close()
#
# main()