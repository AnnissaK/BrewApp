import pymysql
def main():
	connection = pymysql.connect(
		host="localhost",
        port=33066,
		user="root",
		passwd="password",
		database="BrewApp"
	)
	cursor = connection.cursor()
	args = ("k", "k","k")
	cursor.execute("INSERT INTO Drinks (Drink,Drink_type,`Cost / £`) VALUES ( %s, %s,%s)", args)
	connection.commit()
	cursor.close()
	connection.close()

main()