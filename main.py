from flask import Flask, render_template, request

app = Flask(__name__)

import datetime

now = datetime.datetime.now()
a = now.replace(hour=8, minute=0, second=0, microsecond=0)
b = now.replace(hour=18, minute=0, second=0, microsecond=0)
if (now > a) and (now < b):
    @app.route("/")
    def index():
        return render_template("login.html")


@app.route("/register", methods=["GET"])
def register():
    name = request.args.get('username')
    email = request.args.get('email')
    mobile = request.args.get('mobile')
    job = request.args.get('job')
    password = request.args.get('password')
    import pymongo
    con = pymongo.MongoClient("mongodb+srv://srag1985:srag1985@cluster0.cugfs.mongodb.net/user?retryWrites=true&w=majority")
    db = con['user']
    col = db['registration']
    if name != "" and email != "" and mobile != "" and job != "" and password != "":
        col.insert_one({"name": name, "email": email, "mobile": mobile, "job": job, "password": password})
        return render_template("index.html", msg="registration done")


@app.route("/login", methods=["GET"])
def login():
    name = request.args.get('username')
    password = request.args.get('password')
    import pymongo
    con = pymongo.MongoClient("mongodb+srv://srag1985:srag1985@cluster0.cugfs.mongodb.net/user?retryWrites=true&w=majority")
    db = con['user']
    col = db['registration']
    if name != "" and password != "":
        for i in col.find({"name": name, "password": password}):
            return render_template("login.html", msg="Authorised Entry ")
            break
        else:
            return render_template("login.html", msg="Invalid user")
    else:
        return render_template("login.html", msg="Field empty")


app.run(debug=True)
