import mysql.connector
from mysql.connector import errorcode

def show_films(cursor, title):
    cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
 
    films = cursor.fetchall()
    print("\n -- {} --".format(title))
    
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

config = {
    "user": "root",
    "password": "Dang1khoa1!!",
    "host": "localhost",
    "database": "Movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    if db.is_connected():
        print("Connection to MySQL database successful!")
        
        # Create a cursor object
        cursor = db.cursor()
        
        # Call the show_films function with the cursor and title
        show_films(cursor, "Displaying Films")
        
    else:
        print("Connection to MySQL database failed!")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("Connection closed.")
