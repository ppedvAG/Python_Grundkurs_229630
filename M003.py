# Kontrollstrukturen+

# if-Anweisungen
# Überprüft eine Bedingung und führt den enthaltenen Code aus, wenn die Bedingung True ist
# Benötigt Vergleichsoperatoren und/oder Logische Operatoren

# Vergleichsoperatoren
# Bedingungen aufbauen
# ==, !=, <, >, <=, >=

a = 4
b = 8
if a < b:  # Am Ende von allen Strukturen in Python werden : benötigt
	print("a ist kleiner als b")  # Einrückungen beachten
	print("If Ende")  # Mehrere Codezeilen innerhalb der if

print("Nach der if")  # Außerhalb der if durch Einrückungen

if a < b:
	print("a kleiner b")
elif a == b:  # elif: Else-If, eine If die an eine andere If geknüpft ist
	print("a gleich b")
else:  # else: Ein anderer Zustand, muss mit if oder elif kombiniert werden
	print("a größer b")

if a < b:
	print("a kleiner b")
	if a < 5:
		print("a kleiner 5")  # 2 Einrückungen
		print("Innere if Ende")

# Logische Operatoren
# &: and, |: or, ~: not
# in: Prüft, ob ein Wert in einer Collection enthalten ist
# is: Prüft, ob zwei Objekte identisch sind (Speicheradressen)

if a < b and a < 5:  # Beide Bedingungen müssen True sein
	print("a kleiner b und kleiner 5")

if a < b or a < 5:  # Eine von beiden Bedingungen muss True sein
	print("a kleiner b oder kleiner 5")

if not (a < b or a < 5):  # if a >= b and a >= 5:
	print("a nicht kleiner b und nicht kleiner 5")

if a in [1, 2, 3, 4, 5]:
	print("a ist in der Liste enthalten")

if a not in [1, 2, 3, 4, 5]:
	print("a ist nicht in der Liste enthalten")

# Ternary-Operator
# Ermöglicht das Kürzen von if-elif-else Konstrukten in eine einzelne Zeile
if a < b:
	print("a kleiner b")
elif a == b:
	print("a gleich b")
else:
	print("a größer b")

print("a kleiner b" if a < b else "a gleich b" if a == b else "a größer b")

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7]
# Finde heraus welche Liste die längste ist (es können auch mehrere Listen die längsten sein)

# Übung 2
# Nimm die oberen drei Listen und überprüfe ob eine der Listen eine der drei Zahlen enthält: 3, 7, 10
