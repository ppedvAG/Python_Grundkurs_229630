import pyodbc as sql

class DBConnector:
	def __init__(self):
		try:
			self.connection = sql.connect("Driver={SQL Server Native Client 11.0};"
			                         "Server=WIN10-LK3;"
			                         "Database=PythonKurs;"
			                         "Trusted_Connection=yes;")  # Verbindung zur Datenbank herstellen über Connection String
			self.cursor = self.connection.cursor()

		except sql.InterfaceError:
			print("Verbindung kann nicht hergestellt werden")
			exit(1)

	def executeStatement(self, sql):
		self.cursor.execute(sql)
		self.cursor.commit()


connector = DBConnector()
connector.executeStatement("DROP TABLE Personen")
connector.executeStatement("CREATE TABLE Personen (id int primary key, vorname varchar(30), nachname varchar(30))")
connector.executeStatement("INSERT INTO Personen VALUES(0, '', '')")
connector.executeStatement("INSERT INTO Personen VALUES(1, '', '')")
connector.executeStatement("INSERT INTO Personen VALUES(2, '', '')")

# Web Request
import requests
response = requests.get("https://open.er-api.com/v6/latest/USD")
print(response.text)