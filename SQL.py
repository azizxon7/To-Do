# import sqlite3
# SQL - Structured Query Language
# my_db=sqlite3.connect("students.db")
# c=my_db.cursor()
# c.execute("""CREATE TABLE students
# (
#        first_name text,
#        last_name text,
#        email text,
#        age integer
# )
# """)
# datas=[('Alixon', 'Kamoliddinov', 'AliKamol@mail.ru', 15), ('Mansur', 'Uzoqov', 'uzooqman@gmail.com', 18)]
# c.execute("INSERT INTO students VALUES ('Guli', 'Olimova', 'gul0lima@gmail.com', 30)")
# c.executemany("INSERT INTO students VALUES (?, ?, ? ,?)", datas)
# c.execute('SELECT first_name, age FROM students')
# c.execute('SELECT * FROM students')
# a=c.fetchall()
# print(a)
# c.execute("SELECT * FROM students WHERE age=34")
# c.execute("SELECT * FROM students WHERE age<34")
# c.execute("SELECT * FROM students WHERE first_name LIKE '%li%'")
# a=c.fetchall()
# print(a)
# my_db.commit()
# my_db.close()

''''''
