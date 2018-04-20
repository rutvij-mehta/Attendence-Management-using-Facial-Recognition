import MySQLdb


#Used Script
db = MySQLdb.connect("localhost","root","Rutvij123","AMFR")
cursor = db.cursor()

list = ["Priyanka Lubal","Miheer Mahadik","Yogesh Mahajan","Rutvij Mehta","Ankit Morajkar","Abha Mutalik","Ananya Navelkar","Simran Nayak","Neha Nikam","Ananya Ojha","Abhishek Padalkar","Rahul Paknikar","Swanand Pande","Chinmay Paradkar","Vishwa Pardeshi","Siddhanth Parikh"]

for i in range(31,47):
    sql = 'INSERT into student values({0},"{1}")'.format(i,list[i-31])
    print sql
    cursor.execute(sql)

db.commit()
db.close()