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


# Default Arguments
# Parametern können Standardwerte gegeben werden, diese können überschrieben werden, müssen aber nicht
def subtrahiere(x: int, y: int, z=0):
	return x - y - z


subtrahiere(4, 5)
subtrahiere(4, 5, 6)  # Dritte Zahl hier auch möglich, 0 wird überschrieben


# Verwendungszwecke:
# Funktionen konfigurieren
def test(x=0, y=0, z=0, b=False, s="", l=None):
	print()

test(z=5, l=[1, 2, 3])  # Nur z und l befüllen
test(x=10, s="Text")  # Nur x und s befüllen

# Funktion mit einem boolean konfigurieren
def addiereOderSubtrahiere(x: int, y: int, sub=False):  # Funktion, die in 95% der Fälle normal ausgeführt wird, und in 5% der Fälle einen Sonderfall abdeckt (über den boolean)
	if sub:
		print(x - y)
	else:
		print(x + y)

addiereOderSubtrahiere(4, 9)
addiereOderSubtrahiere(4, 9)
addiereOderSubtrahiere(4, 9)
addiereOderSubtrahiere(4, 9)
addiereOderSubtrahiere(4, 9)
addiereOderSubtrahiere(4, 9)
addiereOderSubtrahiere(4, 9, True)

# * Parameter (Arbitrary Arguments)
# Gibt die Möglichkeit, beliebig viele Parameter zu übergeben
def summe(*zahlen: int):
	x = 0
	for zahl in zahlen:
		x += zahl
	return x

summe(1, 2, 3)
summe(1, 2, 3, 4, 5, 6)
summe(1)
summe()  # Keine Parameter sind auch beliebig viele Parameter

def test():
	pass  # Leere Operation, Platzhalter für späteren Code

# ** Parameter (Arbitrary Keyword Arguments)
# Ermöglicht, beliebig viele benannte Parameter zu übergeben
def printTeilnehmer(**teilnehmer: str):
	for key, value in teilnehmer.items():
		print(f"Der Teilnehmer {key} namens {value} nimmt am Kurs teil")

printTeilnehmer(T1="Lukas", T2="Michelle", T3="Anika")

# Unpacking
# Mit * und ** können Listen oder Dictionaries in ihre Einzelteile zerlegt werden für die entsprechenden Parameter (*args, **kwargs)
# Damit können *args und **kwargs mit einer Liste oder einem Dictionary befüllt werden
zahlenListe = [1, 2, 3, 4, 5, 6]
summe(*zahlenListe)

teilnehmer = {
	"T1": "Lukas",
	"T2": "Michelle",
	"T3": "Anika"
}
printTeilnehmer(**teilnehmer)


# Übung 1:
# Wir wollen eine Funktion erstellen, die beliebig viele Zahlen als Parameter erhalten kann
# Und uns die größte dieser Zahlen zurückgibt

# Übung 2:
# Wir wollen eine Funktion erstellen, die einen String als Parameter erhält
# Die Funktion soll dann in der Konsole ausgeben, aus wie vielen Klein- und Großbuchstaben der String besteht
# Die Funktion soll zusätzlich zählen wie viele Sonderzeichen (Nummern inkludiert) enthalten sind und das
# ebenfalls ausgeben
# Sonderzeichen: 4 | Groß: 3 | Klein: 12
