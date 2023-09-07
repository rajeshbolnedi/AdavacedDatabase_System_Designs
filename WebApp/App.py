from bottle import route, run, template
import sqlite3
conn=sqlite3.connect("pets.db")

@route("/")
def get_index():
    return template("<b>Hello, there {{name}}!!!</b>", name="index")

"""
@route('/hello/<name>')
def index(name):
   return template('<b>Hello {{name}}</b>!', name=name)
"""

'''
@route("/hello/<name>")
def get_hello(name):
    return template("hello.tpl", name=name) 
'''

'''
pets = [
    {'id':1, "name":"Dorothy", "kind":"dog"},
    {'id':2, "name":"Casey", "kind":"dog"},
    {'id':3, "name":"Flipper", "kind":"fish"},
    {'id':4, "name":"Cowabelle", "kind":"cow"}
]

@route("/pets")
def get_hello():
    return template("pets.tpl", pets=pets)
'''



@route("/pets")
def get_pets():
    cur=conn.cursor()
    res=cur.execute("select * from pet");
    data=res.fetchall()
    print(data)
    names=[item[0] for item in list(cur.description)]
    print(names)
    return template("pets.tpl",names=names,data=data)

run(host='localhost', port=8080)