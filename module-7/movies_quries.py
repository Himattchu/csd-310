import mysql.connector
from mysql.connector import errorcode

config = {
	"user":"root",
	"password":"Dang1khoa1!!",
	"host":"127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)
	print("\n Database user {} connected to MySQL on host {} with database {}". format(config["user"], config["host"], config["database"]))
	input ("\n\n Press any key to continue...")
except mysql.connector.Error as err:
	 if err.errno == errorcode.ER_ACCESS_DENIED_EERROR:
	 	print(" The spcified username or password are invalid")
		 
	 elif err.errno == errorcode.ER_BAD_DB_ERROR:
	 	print(" The spcified database does not exist")
		 
	 else:
	 	print (err)
		 
finally: 
	print ("--Displaying Studio Records--")
	cursor = db.cursor()
	cursor.execute("Select studio_id,studio_name FROM studio")
	film = cursor.fetchall()
	for studio in film:
		print ("Studio ID: {}\n Studio Name: {}\n ".format(studio[0], studio[1]))

	print ("--Displaying Genre Records--")
	cursor = db.cursor()
	cursor.execute("Select * FROM genre")
	records = cursor.fetchall()
	for genre in records:
		print ("Genre ID: {}\n Genre Name: {}\n ".format(genre[0], genre[1]))

	print ("--Displaying Short Film Records--")
	cursor = db.cursor()
	cursor.execute("select film_name, film_runtime FROM film WHERE film_runtime <120")
	short_film = cursor.fetchall()
	for film in short_film:
		print ("Film Name: {}\n runtime: {}\n ".format(film[0], film[1]))
	
	print ("--Displaying Director records--")
	cursor = db.cursor()
	cursor.execute("select film_name, film_director FROM film")
	film = cursor.fetchall()
	for director in film:
		print ("Film Name: {}\n Director: {}\n ".format(director[0], director[1]))

	
	db.close()