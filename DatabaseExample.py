#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost", "root", "root", "TESTDB")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)


# Execute insert query
sql = """insert into employee (firstname, lastname, age, sex, income)values('dipal', 'modi', 22, 'F', 400000)"""
try:
    cursor.execute(sql)
    db.commit()
except pymysql.DatabaseError:
    db.rollback()


# fetchall() − It fetches all the rows in a result set.
sql = """select * from employee"""
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)


# fetchone() − It fetches the next row of a query result set.
sql = """select * from employee"""
rowcount = cursor.execute(sql)
result = cursor.fetchone()
print(result)


# disconnect from server
db.close()



