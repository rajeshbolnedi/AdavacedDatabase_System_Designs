import dataset
db = dataset.connect('sqlite:///pets.db')
table = db['pet']
data=list(table.find())
data=[dict(item)] for item in data]
print(data)
