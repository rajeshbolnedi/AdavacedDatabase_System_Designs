import dataset
db = dataset.connect('sqlite:///pets.db')
table = db['pet']
data=list(table.find())
<<<<<<< HEAD
data = [dict(item) for item in data]
=======
data=[dict(item)] for item in data]
>>>>>>> origin/main
print(data)
