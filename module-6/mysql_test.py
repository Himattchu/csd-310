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
	db.close()