import pymysql

c = pymysql.connect(
    host="localhost",
    user="root",
    password="Rish2205"
)
cur = c.cursor()
cur.execute("create database if not exists Test")
cur.execute("use test")
cur.execute("create table if not exists Class12a(name varchar(25), age int, DOB date)")
cur.execute("insert into Class12a values ('Rishab', 20, '2005-02-02') ")
cur.execute("insert into Class12a values ('Raman', 20, '2005-05-27') ")
cur.execute("select * from Class12a")
print(cur.fetchall())

for i in cur:
    print(i)

print("Rishab is Great")