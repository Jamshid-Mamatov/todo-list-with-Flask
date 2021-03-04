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
    print(r)
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
    content="r"
    data=db.search(q.number>"0")
    
    return render_template("remove.html",content=content,data=data)

@app.route("/rem",methods=["POST"])
def get_form_remove():
    r=request.form
    rem_num=r.get("remove_num",0)
    db.remove(q.number==rem_num)
    return "ok"


@app.route("/update")
def update():
    content="update"
    return render_template("update.html",content=content)

@app.route("/upd",methods=["POST"])
def get_update():
    r=request.form
    
    rem_task=r.get("task","")
    print(rem_task)
    db.remove(q.text==rem_task)

    task=r.get("task","")
    task_number=r.get("number","")
    task_state=r.get("state","False")

    task_dict={}
    task_dict["text"]=task
    task_dict["number"]=task_number
    task_dict["state"]=task_state

    
    db.insert(task_dict)
    
    return "ok"



@app.route("/checking_task")
def checking_task():
    content="checking_task"
    return render_template("home.html",content=content)

@app.route("/clear")
def clear():
    content="clear"
    return render_template("home.html",content=content)

app.run(debug=True)