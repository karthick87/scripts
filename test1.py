#!/usr/bin/python
import csv
import MySQLdb
db = MySQLdb.connect("localhost","root","redhat123","energyDB")
cursor = db.cursor()

with open('./data.txt') as file:
    reader = csv.reader(file)
    for dd in reader:
        cursor.execute("""INSERT INTO bankgirohistory VALUES(%s)""", dd)
db.commit()
cursor.close()
print "Done"
