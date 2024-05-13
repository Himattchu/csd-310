import mysql.connector
from mysql.connector import errorcode

config = {
	"user":"root",
	"password":"Dang1khoa1!!",
	"host":"127.0.0.1",
	"database": "bacchus",
	"raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}". format(config["user"], config["host"], config["database"]))
	
    cursor = db.cursor()

    create_tables_query =[
		"""
        CREATE Table Products(
		supplier varchar(255),
		item varchar(255),
		item_id int,
		qty int,
		date_received DATE, 
        )
        """,
		"""
        CREATE table Distribution (
		distribututor varchar(255),
		wine_id int,
		out_for_delivery_date DATE,
		delivery_date DATE,
		received_by varchar(255),
        )
        """
    ]
    for query in create_tables_query:
        cursor.execute(query)
    db.commit()


    product_data=[
	    ("ULine", "Bottles", "001","1000","4/1/2024"),
	    ("ULine", "Cork", "021","1000","4/1/2024"),
	    ("Staples", "Labels", "654","5000","4/6/2024"),
	    ("Staples", "Boxes", "456","5000","4/6/2024"),
	    ("Harbor Freight", "tubing", "141","500","5/5/2024"),
	    ("Harbor Freight", "vats", "121","100","5/5/2024"),
	    ("ULine", "Bottles", "001","1000","4/15/2024"),
	    ("ULine", "Cork", "021","1000","4/15/2024"),
	    ("Staples", "Labels", "654","5000","4/20/2024"),
	    ("Staples", "Boxes", "456","5000","4/20/2024"),
	    ("Harbor Freight", "Bottles", "141","500","5/19/2024"),
	    ("Harbor Freight", "Bottles", "121","250","5/19/2024"),
    ]
    distribution_data=[
	    ("UPS","2324","5/20/2024","6/3/2024","Will"),
	    ("UPS","3678","5/27/2024","6/4/2024","John"),
	    ("UPS","7982","6/6/2024","6/20/2024","James"),
	    ("UPS","8990","6/7/2024","6/20/2024","Jason"),
    ]

    cursor.executemany("INSERT INTO Products (supplier,item,item_id,qty,date_received)", product_data)
    cursor.executemany("INSERT INTO Distribution(distributor,wine_id, out_for_delivery_date, delivery_date, received_by)", distribution_data)


    db.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_EERROR:
        print(" The specified username or password are invalid")
		 
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
		 
    else:
        print (err)
finally: 
	db.close()