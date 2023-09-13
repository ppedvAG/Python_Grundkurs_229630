# Funktionen
# Ermöglichen, Code in Strukturen abzulegen um diesen mehrmals zu verwenden und wiederzuverwenden

# Syntax:
# def <Funktionsname>(<Parameter1>, <Parameter2>, ...):
#   <Body, Code der Funktion>
# Die def Zeile wird auch als Head/Kopf der Funktion bezeichnet

# Die Hallo Funktion printed einfach Hallo und danach Welt in die Konsole
def hallo():  # Keine Parameter durch leere Klammern ()
	print("Hallo")  # Hier wieder Einrückungen beachten
	print("Welt")

hallo()
hallo()
hallo()

# Funktion mit Parameter
# Parameter: Die Funktion kann vom Benutzer Werte empfangen und diese verarbeiten

def hallo(name):
	print(f"Hallo {name}")

hallo("Lukas")
hallo("Michelle")
hallo("Anika")

hallo(123)  # name sollte ein String sein, kann aber durch das Typsystem in Python alles mögliche sein
hallo([1, 2, 3])
hallo(True)

# Bei Parametern kann eine Typempfehlung angegeben werden
def halloString(name: str):
	print(f"Hallo {name}")

halloString("Lukas")
halloString(123)
halloString([1, 2, 3])
halloString(True)

def halloString(name: str):
	if type(name) == str:  # Durch eine if den Typ abfragen vor dem ausführen des Codes
		print(f"Hallo {name}")

halloString("Lukas")
halloString(123)
halloString([1, 2, 3])
halloString(True)

# Mehrere Parameter (beliebig viele Parameter)
def printAddiere(x: int, y: int):
	print(x + y)

printAddiere(4, 5)
printAddiere(4.5, 5.2)

# Funktionen mit Rückgabewert
summe = sum([1, 2, 3])  # Die sum Funktion gibt einen Wert zurück (die Summe)
print(summe)  # Die print Funktion gibt keinen Wert zurück

def addiere(x: int, y: int) -> float:  # Hier explizit angeben das diese Funktion einen float zurückgibt
	return x + y  # Über return definieren das diese Funktion ein Ergebnis hat

ergebnis = addiere(5, 6)  # Ergebnis der Funktion in eine Variable schreiben
print(ergebnis * 2)

