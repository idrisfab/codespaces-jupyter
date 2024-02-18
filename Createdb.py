import sqlite3

conn = sqlite3.connect('my_database.db')

c = conn.cursor()

create_table_1 = '''CREATE TABLE IF NOT EXISTS table1 (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                    );'''

create_table_2 = '''CREATE TABLE IF NOT EXISTS table2 (
                    id INTEGER PRIMARY KEY,
                    product_name TEXT NOT NULL,
                    price REAL
                    );'''

create_table_3 = '''CREATE TABLE IF NOT EXISTS table3 (
                    id INTEGER PRIMARY KEY,
                    category TEXT NOT NULL,
                    description TEXT
                    );'''

create_table_4 = '''CREATE TABLE IF NOT EXISTS table4 (
                    id INTEGER PRIMARY KEY,
                    date TEXT NOT NULL,
                    event TEXT
                    );'''

c.execute(create_table_1)
c.execute(create_table_2)
c.execute(create_table_3)
c.execute(create_table_4)

insert_into_table_1 = '''INSERT INTO table1 (name, age)
                          VALUES ('John Doe', 30),
                                 ('Jane Doe', 25),
                                 ('Mike Tyson', 50);'''

c.execute(insert_into_table_1)

conn.commit()
conn.close()
