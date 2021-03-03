from flask import Flask,render_template,request
from jinja2 import Template
from tinydb import TinyDB,Query
app=Flask(__name__)
q=Query()
db=TinyDB("database.json")
# "db.truncate()"

@app.route("/creat")
@app.route("/")
def creat():
    content="creat"
    
    return render_template("home.html",content=content)


@app.route("/add")
def add ():
    content="add"

    return render_template("add.html",content=content)

task_list=[]
@app.route("/form",methods=["POST","GET"])
def get_form():
       
    r=request.form
    
    task=r.get("task","")
    task_number=r.get("number","")
    task_state=r.get("state","False")

    task_dict={}
    task_dict["text"]=task
    task_dict["number"]=task_number
    task_dict["state"]=task_state

    task_list.append(task_dict)
    db.insert_multiple(task_list)
    
    return task


@app.route("/remove")
def remove():
    content="remove"
    data=db.search(q.number>"0")
    
    return render_template("home.html",content=content,data=data)

@app.route("/update")
def update():
    content="update"
    return render_template("home.html",content=content)

@app.route("/checking_task")
def checking_task():
    content="checking_task"
    return render_template("home.html",content=content)

@app.route("/clear")
def clear():
    content="clear"
    return render_template("home.html",content=content)

app.run(debug=True)