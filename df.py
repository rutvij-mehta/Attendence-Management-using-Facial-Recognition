import MySQLdb


#Code for checking defualter
def check(subject, month):
    db = MySQLdb.connect("localhost","root","Rutvij123","AMFR")
    cursor = db.cursor()

    sql = 'SELECT total from subject where sname = "{0}" and month = {1}'.format(subject,month)
    cursor.execute(sql)
    total = cursor.fetchone()[0]

    
    check = total*0.75

    sql = 'SELECT sid from subject where sname = "{0}" and month = {1}'.format(subject,month)
    cursor.execute(sql)
    ide = cursor.fetchone()[0]

    sql = 'SELECT stid from attendance where count<{0} and sid = {1}'.format(check,ide)
    cursor.execute(sql)
    defaulter = cursor.fetchall()

    indices = [defaulter[i][0] for i, x in enumerate(defaulter)]

    return indices
    
    