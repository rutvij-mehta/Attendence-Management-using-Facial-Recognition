from __future__ import print_function
from flask import Flask, jsonify, request, json
#from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
from flask_uploads import UploadSet, configure_uploads, IMAGES
#from werkzeug import secure_filename
import extract, df

import MySQLdb

app = Flask(__name__)

#global m

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print(request.files)
    #global m
    #t = m
    
    if request.method == 'POST' and 'file' in request.files:
        filename = photos.save(request.files['file'])
        print(filename)
        
        """
        db = MySQLdb.connect("localhost","root","Rutvij123","AMFR")
        c = db.cursor()
        subject = "SPCC"
        sql = 'select sid from subject where month=4 and sname={0}'.format(subject)
        c.execute(sql)
        sid = c.fetchone()[0]

        f = extract.attendance(filename)
        for i in f["result"]:
            #sql = 'update attendance set count=count+1 where stid={0} and sid={1}'.format(i,sid)


        return jsonify({"result" : f})
        """
        return jsonify({"count" : extract.attendance(filename)})

    
    return jsonify({"count" : 0})


@app.route('/')
def index():
    global m
    m=3
    return "Hello"

@app.route("/validate", methods=['GET','POST'])
def validate():
    print("Connected")
    data2= request.get_json(force=True)
    
    uid = data2["email"]
    password = str(data2["password"])
    print(uid,password)
    db = MySQLdb.connect("localhost","root","Rutvij123","AMFR")
    c = db.cursor()
    print(c)
    sql = "SELECT * FROM user WHERE uid='{0}' and password='{1}'".format(uid,password)
    
    try:
        c.execute(sql)
    except:
            print("Error")

    js = c.fetchone()
    if(js):
        count = 1
    else:
        count = 0

    db.close()
    return jsonify({"count" : count})



@app.route("/register", methods=['GET','POST'])
def register():
    print("in register")
    data = request.get_json(force=True)

    email = data["username"]
    password = data["password"]
    name = data["name"]
    uid = data["age"]

    db = MySQLdb.connect("localhost","root","Rutvij123","AMFR")
    cursor = db.cursor()

    sql = "INSERT INTO user VALUES({0},'{1}','{2}','{3}')".format(uid,str(name),str(email),str(password))

    print(sql)

    cursor.execute(sql)

    db.commit()
    return jsonify({"count" : 1})


@app.route("/defaulter", methods=['GET','POST'])
def defaulter():
    data = request.get_json(force=True)
    
    subject = data["subject"]
    month = data["month"]
    print(subject,month)
    list = ['January','February','March','April','May','June','July','August','September','October','November','December']
    month = list.index(month)+1
    print(month)
    if month>4 and month <=12:
        return jsonify({"count":[]})
        
    return jsonify({"count" : df.check(subject,month)})


#WORKING FINE. TESTED
"""
@app.route("/test", methods=['GET', 'POST'])
def tes():
    json_data = request.get_json(force=True)
    print(json_data["email"])
    return "Hi"


"""

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001, debug=True)