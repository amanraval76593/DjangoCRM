import mysql.connector

database = mysql.connector.connect(
    host="Localhost",
    user="aman7",
    password="Aman@76593",
)

# prepae a cursor object using cursor() method

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("Database created successfully")
