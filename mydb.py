import mysql.connector

# U connect metodi, koristite dictionary format za proslijeđivanje parametara
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sasa1459'
)

# Kreirajte cursor
cursorObject = dataBase.cursor()

# Izvršite SQL naredbu za kreiranje baze podataka
cursorObject.execute('CREATE DATABASE crmdatabase')

# Potvrdite izvršenje naredbe
print('Database created!')
