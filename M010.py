# Vererbung
# Klassen können eine Oberklasse haben und dadurch eine Vererbungshierarchie herstellen
# Die Oberklasse gibt ihre Member (Variablen, Funktionen) an die Unterklassen weiter
# object ist die Oberklassen von allen Klassen in Python

# z.B.: Klasse Lebewesen[name, bewegen()]
# Klasse Mensch -> Oberklasse Lebewesen, implementiert sprechen()
# Klasse Katze -> Oberklasse Lebewesen, implementiert springen()
# Mensch und Katze sind Spezifizierungen von Lebewesen

class Lebewesen:
	"""
	Die Lebewesen Klasse fungiert als Oberklasse zu allen Lebewesen in diesem Projekt. Sie gibt einen Namen und die bewegen(Distanz) Funktion vor.
	"""
	def __init__(self, name: str):  # Hier wird die Struktur von __init__ vorgegeben, diese Struktur muss in den Unterklassen implementiert werden
		"""
		Hier werden die Standardwerte des Lebewesens gesetzt (Name).

		Es gibt zusätzlich noch eine Ausgabe das ein Lebewesen erstellt wurde.

		:param name: Der Name des Lebewesens
		"""
		self.name = name
		print("Lebewesen wurde erstellt")

	def bewegen(self, distanz: int):
		print(f"Das Lebewesen bewegt sich um {distanz}m.")

	def __str__(self):  # Gibt uns eine Stringrepräsentation des Objekts
		"""
		:return: Eine String Repräsentation des Objekts. Diese enthält eine Beschreibung und technische Daten.
		"""
		return f"Das Lebewesen heißt {self.name}. Die Daten des Lebewesens sind: {super().__str__()}"


class Mensch(Lebewesen):
	def __init__(self, name: str, alter: int):
		super().__init__(name)  # super(): Rufe Code von der Oberklasse auf, Verkettung der __init__ Methoden
		self.alter = alter
		print("Mensch wurde erstellt")

	def sprechen(self, text: str):  # Hier wird eine spezifische Funktion in der Mensch Klasse definiert
		print(text)

	def __str__(self):
		return f"Der Mensch heißt {self.name} und ist {self.alter} Jahre alt."


class Katze(Lebewesen):
	def __init__(self, name: str):
		super().__init__(name)

	def springen(self, distanz: int):
		print(f"Die Katze springt {distanz}cm.")


mensch = Mensch("Max", 33)  # __init__ von Mensch -> __init__ von Lebewesen -> __init__ von object
mensch.bewegen(10)  # Wird vererbt von Lebewesen
mensch.sprechen("Hallo")  # Kommt von Mensch selbst
print(mensch.alter)

katze = Katze("Garfield")
katze.springen(50)

print(mensch)  # <__main__.Mensch object at 0x0000020198D9B1C0> (Standard String Repräsentation wenn __str__ nicht überschrieben)
print(mensch)  # Das Lebewesen heißt Max (Bei Überschreibung der __str__ Methode bei Lebewesen)
print(mensch)  # Der Mensch heißt Max und ist 33 Jahre alt (Bei Überschreibung innerhalb von Mensch)
print(katze)  # Das Lebewesen heißt Garfield (In Katze gab es keine Überschreibung -> Funktion in Lebewesen)

# docstring
# Ermöglicht uns Dokumentationen zu schreiben um Klassen, Funktionen und Variablen zu beschreiben
# Werden mit """ <Text> """ oder ''' <Text> ''' geschrieben
# Müssen Unter den entsprechenden Member geschrieben werden