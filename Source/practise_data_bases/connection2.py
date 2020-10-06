import pymysql
#import Names.txt

#def main():
connection = pymysql.connect(
host="localhost",
port=33066,
user="root",
passwd="password",
database="BrewApp"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM BrewApp.Drinks")
while True:
    row = cursor.fetchone()

    if row == None:
        break
    print("Drink - " + str(row[0]) + " " + "Drink_type - " + str(row[1]) + " " )
connection.commit()
cursor.close()
connection.close()
#
# main()