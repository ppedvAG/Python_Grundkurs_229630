# Klassen und Objekte

# Klasse
# Bauplan für Objekte, aus einer Klasse können beliebig viele Objekte erzeugt werden
# Klassen haben Strukturen bestehend aus Funktionen und Variablen. Die daraus erzeugten Objekte haben dann diese Struktur
# Innerhalb der Klasse werden keine konkreten Werte angegeben -> Nur ein Bauplan
# z.B.: Klasse Auto
# Variablen: Marke, Maximalgeschwindigkeit, AnzSitze
# Funktionen: Beschleunige, Bremse, Lenken, ...
# -> Objekte ["Audi", 250, 5], ["BMW", 300, 5], ["VW", 200, 5]

wort = "Text"  # String Objekt erstellt mit Wert "Text"
wort.title()  # Vom String Objekt die title() Funktion verwendet

wort2 = "Test"  # String Objekt 2
wort2.lower()  # lower() bezieht sich nur auf dieses Objekt

print(type(wort))  # <class 'str'>
print(type(123))  # <class 'int'>
print(type(True))  # <class 'bool'>
print(type([1, 2, 3]))  # <class 'list'>

if type(wort) == str:  # Typvergleich, wird verwendet um zu schauen was der Typ des Objekts anhand einer Variable ist
	print("wort hat den str Typ")


# Person Klasse
class Person:
	# Die __init__ Funktion
	# Enthält den Code, der bei Erstellung des Objekts ausgeführt wird
	# Wird generell immer benötigt
	# Wird in anderen Sprachen als Konstruktor bezeichnet
	# self: Bezieht sich auf das Objekt selbst. Ermöglicht, innerhalb von der Klasse das gegebene Objekt anzusprechen
	def __init__(self, vorname: str, nachname: str, alter: int, hobbies=None, adresse="", geschwister=None, haarfarbe="", groesse=0):  # Hier werden die konkreten Werte später bei Objekterstellung übergeben
		self.vorname = vorname
		self.nachname = nachname
		self.alter = alter
		self.hobbies = hobbies  # Ab hier optionale Parameter, werden mit <Name>=<Standardwert> definiert
		self.adresse = adresse
		self.geschwister = geschwister
		self.haarfarbe = haarfarbe
		self.groesse = groesse

	# Hier wird eine Funktion definiert die am Ende auf allen Objekten angefügt wird
	def sprechen(self, text: str):
		print(f"Die Person sagt {text}")

	def printName(self):
		print(f"Die Person heißt {self.vorname} {self.nachname}")  # Hier mit self.<Variable> auf die konkreten Werte des Objekts zugreifen

# ----------------------------------------------------------------

# Außerhalb der Klasse

person1 = Person("Lukas", "Kern", 25, groesse=178)  # Person erstellt, hat die Werte Vorname, Nachname, Alter, Größe befüllt
print(person1.vorname)
person1.sprechen("Hallo")  # Die sprechen Funktion wurde in der Klasse definiert, dadurch hat diese Objekt die Funktion
person1.printName()

# Dynamische Variablen
# In Python können Objekten einfach neue Variablen hinzugefügt werden (von außen)
# Sollte generell vermieden werden
person1.geschlecht = "M"
print(person1.geschlecht)

# Variablen löschen
del person1.geschlecht

# Objekte in Action
class Kurs:
	def __init__(self, titel: str, tage: int, *teilnehmer: Person):
		self.titel = titel
		self.tage = tage
		self.teilnehmer = list(teilnehmer)

	def beitreten(self, teilnehmer: Person):
		self.teilnehmer.append(teilnehmer)

	def listTeilnehmer(self):
		for tn in self.teilnehmer:
			print(f"Die Person {tn.vorname} {tn.nachname} nimmt am Kurs teil")

person1 = Person("", "", 25)
person2 = Person("", "", 23)
person3 = Person("", "", -1)
kurs = Kurs("Python Grundkurs", 6, person1, person2, person3)  # Verschachtelte Objekte Kurs[Titel, Tage, Personen[person1, person2, person3]]
kurs.listTeilnehmer()

# Übung 1:
# 1. Erstelle eine Fahrzeug-Klasse
# 2. Diese Klasse soll typische Eigenschaften eines Fahrzeuges enthalten: (in __init__)
#     - Fahrzeug-Name
#     - Preis
#     - Maximale Geschwindigkeit
#     - Derzeitige Geschwindigkeit
#     - Motorzustand (An/Aus)
# 3. Die Klasse soll auch folgende Methoden enthalten:
#     - Beschleunigen (Erhöhe bzw Verringere die Derzeitige Geschwindigkeit aber übersteige nicht das Maximum) -> Parameter int (Wieviel soll beschleunigt werden)
#     - StarteMotor (Setze Motorzustand auf True, funktioniert nur wenn das Auto noch nicht gestartet ist)
#     - StoppeMotor (Motor kann nur gestoppt werden, wenn das Auto nicht fährt)
#     - Beschreibung (Gibt alle Informationen über die Klasse wieder)
# 4. Erstelle eine Instanz der Klasse und nutze die Beschreibungs Funktion (Konkrete Werte)
