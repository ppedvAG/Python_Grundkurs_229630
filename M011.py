# Fehlerbehandlung

# Es gibt Fehler die auftreten können die nicht einfach durch ifs abgefangen können
# Diese Fehler können verarbeitet werden mit der try-except Mechanik

# zahl = int(input("Gib eine Zahl ein: "))  # Wenn der User keine Zahl eingibt, tritt ein ValueError auf

# userInput = input("Gib eine Zahl ein: ")
# if userInput.isnumeric():
# 	zahl = int(userInput)

try:  # Hier ist der Code enthalten, der getestet werden soll
	zahl = int(input("Gib eine Zahl ein: "))
	if zahl == 0:
		raise ZeroDivisionError  # Fehler selbst werfen, wird vorallem in Packages (= Code der von anderen Leuten verwendet werden soll) verwendet
except ValueError as e:  # Wenn der ValueError auftritt, wird der except Block ausgeführt
	print(e)  # Gibt die Python interne Fehlermeldung weiter
	print("Keine Zahl eingegeben")  # Exit Codes: Code 0 wenn alles in Ordnung ist, nicht Code 0 wenn ein Fehler auftritt (einzelne Codes sollten Dokumentiert werden)
except KeyboardInterrupt:
	print("Programm abgebrochen über Stop Button")
except EOFError:
	print("Programm abgebrochen durch Strg + D in der Konsole")
except:  # In except ohne Fehler werden alle anderen Fehler abgefangen
	print("Allgemeine Fehlerbehandlung")
else:
	print("Code ohne Fehler durchgelaufen")
finally:
	print("Wird immer ausgeführt")  # Auch bei unbehandelten Fehlern

# Eigene Exception
class CoffeeError(Exception):
	pass

raise CoffeeError