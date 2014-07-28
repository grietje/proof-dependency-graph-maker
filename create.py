import sqlite3

name = input("Name for this pdgm project: ")

print("Creating database:" + name + ".sqlite")
db = sqlite3.connect(name + ".sqlite")
cursor = db.cursor()

print("Creating table 'links'")
cursor.execute("CREATE TABLE links (source, target);")
db.commit()

db.close()

