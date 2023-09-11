from bottle import route, run, template
import sqlite3
conn=sqlite3.connect("pets.db")
<<<<<<< HEAD
=======
# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)
>>>>>>> origin/main

@route("/")
def get_index():
    return template("<b>Hello, there {{name}}!!!</b>", name="index")

<<<<<<< HEAD
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
=======
>>>>>>> origin/main
pets = [
    {'id':1, "name":"Dorothy", "kind":"dog"},
    {'id':2, "name":"Casey", "kind":"dog"},
    {'id':3, "name":"Flipper", "kind":"fish"},
    {'id':4, "name":"Cowabelle", "kind":"cow"}
]

<<<<<<< HEAD
@route("/pets")
def get_hello():
    return template("pets.tpl", pets=pets)
'''


=======
@route("/hello/<name>")
def get_hello(name):
    return template("hello.tpl", name=name) 

@route("/pets")
def get_hello():
    return template("pets.tpl", pets=pets)
>>>>>>> origin/main

@route("/pets")
def get_pets():
    cur=conn.cursor()
    res=cur.execute("select * from pet");
<<<<<<< HEAD
    data=res.fetchall()
    print(data)
    names=[item[0] for item in list(cur.description)]
    print(names)
    return template("pets.tpl",names=names,data=data)

=======
    data=result.fetch()
    print(data)
    names=[item[0] for item in list(cursor.description)]
    print(names)
    return template("pets.tpl",names=names,data=data)



>>>>>>> origin/main
run(host='localhost', port=8080)