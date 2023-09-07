import sqlite3
conn=sqlite3.connect("pets.db")
cur=conn.cursor()
res=cur.execute("select * from pet");
data=result.fetch()
print(data)
names=[item[0] for item in list(cursor.description)]
print(names)