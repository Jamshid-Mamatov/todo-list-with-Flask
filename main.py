from flask import Flask,render_template
from jinja2 import Template
app=Flask(__name__)


@app.route("/creat")
@app.route("/")
def creat():
    content="creat"
    
    return render_template("home.html",content=content)


@app.route("/add")
def add ():
    content="add"
    return render_template("home.html",content=content)

@app.route("/remove")
def remove():
    content="remove"
    return render_template("home.html",content=content)

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