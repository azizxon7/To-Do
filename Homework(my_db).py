# Homework(my_db).py
import sqlite3
# # 1-vazifa
my_db=sqlite3.connect("mening_bazam.db")
c=my_db.cursor()
# # 2-vazifa
# c.execute("""CREATE TABLE ustozlar
# (
#        ism text,
#        fan text,
#        yosh integer,
#        shahar text
#        )"""
# )
# # 3-vazifa
# c.execute("INSERT INTO ustozlar VALUES ('Guli', 'Musiqa', 30, 'Fargona');")
# c.execute("INSERT INTO ustozlar VALUES ('Rayxon', 'Ingliz tili', 18, 'Margilon');")
# c.execute("INSERT INTO ustozlar VALUES ('Olima', 'Rus tili', 40, 'Oltariq');")
# c.execute("INSERT INTO ustozlar VALUES ('Yulduz', 'Chizmachilik', 19, 'Quvasoy');")
# c.execute("INSERT INTO ustozlar VALUES ('Halima', 'Texnologiya', 18, 'Quva');")
# # 4-vazifa
# datas=[
#     ('Ali', 'Jismoniy tarbiya', 31, 'Xorazm'), 
#     ('Mansur', 'Tarix', 21, 'Xiva'), 
#     ('Halim', 'Texnologiya', 24, 'Guliston'),
#     ('Olim', 'Matematika', 40, 'Beshariq'), 
#     ('Doniyor', 'Kimyo', 20, 'Toshkent')
#     ('Vali', 'Jismoniy tarbiya', 31, 'Xorazm'), 
#     ('Mahmud', 'Tarix', 21, 'Xiva'), 
#     ('Hokim', 'Texnologiya', 24, 'Guliston'),
#     ('Davron', 'Matematika', 40, 'Beshariq'), 
#     ('Dilshod', 'Kimyo', 20, 'Toshkent')
#     ('Hasan', 'Jismoniy tarbiya', 31, 'Xorazm'), 
#     ('Husan', 'Tarix', 21, 'Xiva'), 
#     ('Husayn', 'Texnologiya', 24, 'Guliston'),
#     ('Otabek', 'Matematika', 40, 'Beshariq'), 
#     ('Xoliq', 'Kimyo', 20, 'Toshkent')]
# c.executemany("INSERT INTO ustozlar VALUES (?, ?, ? ,?);", datas)
# # 5-vazifa
# c.execute('SELECT * FROM ustozlar')
# a=c.fetchall()
# print(a)
# # 6-vazifa
# c.execute('SELECT ism, fan FROM ustozlar')
# a=c.fetchall()
# print(a)
# # 7-vazifa
# c.execute("SELECT * FROM ustozlar WHERE fan LIKE '%Kimyo%'")
# a=c.fetchall()
# print(a)
# # 8-vazifa
# c.execute("SELECT * FROM ustozlar WHERE yosh>20")
# a=c.fetchall()
# print(a)
# # 9-vazifa
# c.execute("SELECT * FROM ustozlar WHERE ism LIKE '%m%'")
# c.execute("""CREATE TABLE shaharlar
# (
#        nom text,
#        maydon integer,
#        aholi integer
#        )"""
# )
# # 10-vazifa
# cities=[('Margilon', 400000, 2000000), ('Fargona', 800000, 4000000), ('Xorazm', 1400000, 1000000), ('Samarqand', 800000, 10000000),
#  ('Namangan', 400000, 122000), ('Qoqon', 230000, 78000000), ('Guliston', 12000, 5000000), ('Toshkent', 1000000, 12000000),
#  ('Andijon', 400000, 2000000), ('Buxoro', 400000, 22000000),]
# c.executemany("INSERT INTO shaharlar VALUES (?, ?, ? ,?);", cities)
# # 11-vazifa
# c.execute("SELECT * FROM shaharlar WHERE ahooli>100000")
# a=c.fetchall()
# print(a)
my_db.commit()
my_db.close()