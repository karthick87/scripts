#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect("localhost","root","redhat123","energyDB")
cursor = db.cursor()
cursor.execute("insert into bankgirohistory values ('KARTHICK')")
db.commit()
db.close()

#try:
#   x.execute("insert into bankgirohistory values ('TEST123')"
#   db.commit()
#except:
#   db.rollback()
#db.close()
