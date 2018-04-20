import MySQLdb

import random

#Used Script
db = MySQLdb.connect("localhost","root","Rutvij123","AMFR")
cursor = db.cursor()

sql = "INSERT into attendance values({0}, {1}, {2}, {3})"

id = 0
for i in range(31, 47):
    for x in range(2, 10):
        count = random.sample([7, 8, 9, 10], 1)[0]

        sql_exec = sql.format(id, i, x, count)

        id = id + 1

        cursor.execute(sql_exec)


        



db.commit()
db.close()