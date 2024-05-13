# Import mysql
import mysql.connector as sql

# Method show_films


def show_films(cursor, title):
    # method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute('''select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id''')
    # get the results from the cursor object
    films = cursor.fetchall()
    print("\n -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]))


# Main method
def main():

    # Create connection to database
    connection = sql.connect(
        "user":"root",
	    "password":"Dang1khoa1!!",
	    "host":"127.0.0.1",
	    "database": "movies",
     )

    # Create cursor
    cursor = connection.cursor()

    # Displaying existing records in database
    show_films(cursor, "DISPLAYING FILMS")

    # Perform Insertion of new movie
    insertQuery = " INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Star Wars', '2000', '155', 'George Lucas', (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'),(SELECT genre_id FROM genre WHERE genre_name = 'SciFi') );"
    connection.commit()
    cursor.execute(insertQuery)
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Perform Update of Alien movie
    updateQuery = " update film set genre_id = (select genre_id from genre where genre_name = 'Horror') where film_name = 'Alien';"
    connection.commit()
    cursor.execute(updateQuery)
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete Gladiator movie from table
    deleteQuery = " delete from film where film_name = 'Gladiator';"
    connection.commit()
    cursor.execute(deleteQuery)
    show_films(cursor, "DISPLAYING FILMS AFTER Delete")

// Calling main() function
main()