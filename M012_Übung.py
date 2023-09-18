import datetime

import M012
import os

db = M012.DBConnector()

files = os.listdir("Personen")

# db.executeStatement("DROP TABLE Personen2")
# db.executeStatement("CREATE TABLE Personen2 (id int primary key, name varchar(50), gebdat datetime, age int, beruf varchar(50), gehalt int)")
#
# for file in files:
# 	with open(os.path.join("Personen", file)) as io:
# 		lines = [line.rstrip("\n") for line in io.readlines()]
# 		db.executeStatement(f"INSERT INTO Personen2 VALUES({lines[0]}, '{lines[1]}', '{lines[2]}', {lines[3]}, '{lines[4]}', {lines[5]})")

# Model Klassen
# Klasse, die nur dafür da ist um eine Datenstruktur zu repräsentieren

class Person:
	def __init__(self, row):
		self.id = int(row[0])
		self.name = row[1]
		self.gebdat = row[2]
		self.age = int(row[3])
		self.beruf = row[4]
		self.gehalt = int(row[5])

result = db.select("SELECT * FROM Personen2 ORDER BY id")
personen = list()  # [Person(row) for row in result]
for row in result:
	personen.append(Person(row))

for person in personen:
	print(person.name)  # Viel angenehmer zum mit Arbeiten als ein Tupel