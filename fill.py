import sqlite3

name = input("Name of the pdgm project you are working on: ")

db = sqlite3.connect(name + ".sqlite")
cursor = db.cursor()

print("""Please enter source and target of your dependencies.

After each entry you have to confirm the entry. The question can be answered in four ways:
 y - yes:  Valid entry, continue with next entry
 n - no:   Invalid entry, continue with next entry
 d - done: Valid entry, submit and stop the program
 q - quit: Invalid entry, stop without submitting
The answers are case-insensitive. The default (empty) answer means [y]es.
Every other answer is a [n]o.
""")
source = ""

def newlink():
	global source, cursor
	source = input("Source[" + source + "]: ") or source
	target = input("Target: ")
	check = input("Do you want to add link (" + source + ", " + target + ")? [y]ndq: ") or "y"
	check = check.lower()
	if check == "y":
		cursor.execute("INSERT INTO links VALUES (?,?)", (source, target))
		print("Added link (" + source + ", " + target + ")")
		return 1
	elif check == "d":
		cursor.execute("INSERT INTO links VALUES (?,?)", (source, target))
		print("Added link (" + source + ", " + target + ")")
		return -1 
	elif check == "q":
		return -2
	else:
		return 0

additions = 0

while True:
	v = newlink()
	if v == -1:
		additions += 1
		break
	elif v == 1:
		additions += 1
	elif v == -2:
		break
		
print("Added %d links to the database." % (additions,))

db.commit()
db.close()
	





