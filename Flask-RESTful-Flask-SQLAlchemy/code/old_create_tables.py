import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_tables = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_tables)

create_tables = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,name text, price real)"
cursor.execute(create_tables)

# cursor.execute("INSERT INTO items VALUES ('piano', 10.99)")

connection.commit()

connection.close()
