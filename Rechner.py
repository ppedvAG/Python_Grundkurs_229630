class Rechner:
	def readInput(self, text):
		while True:
			try:
				zahl = int(input(text))
				return zahl
			except ValueError:
				pass

	def rechne(self, zahl1, zahl2, operation):
		if operation == 1:
			return zahl1 + zahl2
		if operation == 2:
			return zahl1 - zahl2
		if operation == 3:
			return zahl1 * zahl2
		if operation == 4:
			return zahl1 / zahl2


rechner = Rechner()
zahl1 = rechner.readInput("Gib Zahl1 ein: ")
zahl2 = rechner.readInput("Gib Zahl2 ein: ")
operation = rechner.readInput("Gib eine Operation ein: ")
ergebnis = rechner.rechne(zahl1, zahl2, operation)
print(ergebnis)