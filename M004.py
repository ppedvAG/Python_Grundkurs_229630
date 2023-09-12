# Schleifen

# Führt Code mehrmals aus
# Wenn am Ende der Schleife die Bedingung noch wahr ist, wird sie nochmal ausgeführt, solange die Bedingung nicht mehr wahr ist

# while-Schleife
# Führt Code aus solange eine Bedingung wahr ist
a = 0
b = 10

# Hier wird geprüft, ob die Bedingung wahr ist
# Wenn die Bedingung falsch ist, wird der Code in der Schleife nicht mehr ausgeführt, und der Code danach geht weiter
while a < b:
	print(a)
	print("a kleiner b")
	a += 1  # In Python gibt es kein ++/--
# Hier am Ende der Schleife wird zurück gesprungen zum Schleifenkopf (while ...)

print("Nach der Schleife")

# break und continue
# Ermöglichen, das Steuern der Schleife
# break: Beenden der Schleife, sollte mit einer if kombiniert werden
# continue: Springt zum Schleifenkopf zurück, sollte mit einer if kombiniert werden

a = 0
while a < b:
	print(a)
	print("a kleiner b")
	a += 1
	if a == 5:
		break  # Springt aus der Schleife heraus

print("Nach der Schleife")

a = 0
while a < b:
	a += 1
	if a == 5:
		continue  # Springt in den Schleifenkopf zurück
	print(a)
	print("a kleiner b")

# Endlosschleife
# Mache etwas bis zu einem bestimmten Punkt
while True:
	print(a)
	a += 1
	if a > 500:
		break  # "bis zu einem bestimmten Punkt"-Bedingung

# for-Schleife
# Ein Konstrukt, mit dem eine Liste iteriert werden kann (-> jedes Element der Liste durchgegangen werden kann)
# Benötigt eine Liste/Tupel/Set/String/... zum durchgehen
# Wird als foreach in anderen Sprachen bezeichnet

liste = [7, 3, 8, 10, 2]
for zahl in liste:  # Gehe die Liste Element für Element durch, zahl ist hier das derzeitige Element
	print(zahl)  # 7 -> 3 -> 8 -> 10 -> 2 -> Ende

i = 0
while i < len(liste):
	print(liste[i])
	i += 1

# Konventionelle for-Schleife aus anderen Sprachen
for i in range(10):  # for (int i = 0; i < 10; i++)
	print(i)

for i in range(5, 20, 2):  # for (int i = 5; i < 20; i += 2)
	print(i)

strListe = ["Das", "ist", "eine", "Liste"]
for wort in strListe:
	print(wort)
	if "e" in wort:  # wort: Das derzeitige Wort
		print("Das derzeitige Wort enthält e")

for buchstabe in "Ein Text":
	print(buchstabe)

# else bei einer Schleife
# Ermöglicht, nach erfolgreichem Abschluss der Schleife, Code auszuführen
c = 0
d = 10
while c < d:
	c += 1
	if c == 5:
		break  # Else wird verhindert
else:
	print("Schleife ohne break beendet")

# Funktioniert auch bei for-Schleife
for i in range(10):
	if i == 5:
		break
else:
	print("Schleife ohne break beendet")

# fstring
# Formatted String
# Code in einen String einbinden
# Arbeit ersparen

a = 5
output = "Die Zahl ist: " + str(a)  # Ohne fstring
output2 = f"Die Zahl ist: {a}"  # Mit fstring

for i in range(0, 10):
	# 3 Ausgaben: Die Zahl selbst, Die Zahl hoch 2, Die Gleichung von Zahl hoch 2
	# print("Die Zahl ist: " + str(i))
	# print("Die Zahl^2 ist: " + str(i ** 2))
	# print(str(i) + "^2=" + str(i ** 2))

	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl^2 ist: {i ** 2}")
	print(f"{i}^2={i ** 2}")

# Verschachtelte Schleifen
# Schleifen in Schleifen
# Für jeden Durchgang der äußeren Schleife, wird die innere Schleife vollständig ausgeführt
for i in range(10):  # Die äußere Schleife wird 10 mal ausgeführt
	for j in range(10):  # Die innere Schleife wird 10*10=100 mal ausgeführt
		print(f"{i}: {j}")

csv = [["Ein", "CSV", "File"],
		["Zwei", "CSV", "File"],
		["Drei", "Zeilen", "CSV"]]

for zeile in csv:
	print(zeile)
	for wert in zeile:
		print(wert)

# Übung 1:
# FizzBuzz
# 1. Schleife schreiben, die von 1 bis inklusive 100 hochzählt
# 2. Wir müssen in der Schleife jede Zahl auf ihre Teilbarkeit prüfen:
# Falls sie durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls sie durch 5 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls sie sowohl durch 3 als auch 5 teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls sie weder durch 3 noch 5 teilbar ist, soll die Zahl selbst in der Konsole ausgegeben werden
# 1
# 2
# Fizz
# 4
# Buzz
# ...
# 14
# FizzBuzz

# Übung 2:
# Schreibe eine Schleife die dir alle Zahlen von 1 bis 200 zur Verfügung stellt
# Lass dir jede Zahl erst in der kardinalen und dann daneben in der ordinalen Schreibweise darstellen
# Zahl + Endung 'st', 'nd', 'rd' oder 'th'
# 1st, 2nd, 3rd, 4th, ..., 21st, 22nd, 23rd, 24th
# Bonus: Berücksichtige alle Zahlen die mit 11, 12 oder 13 enden
for i in range(1, 201):
	if i % 100 in [11, 12, 13]:  # i % 100 == 11 or i % 100 == 12 or i % 100 == 13
		print(f"{i}th")
	elif i % 10 == 1:
		print(f"{i}st")
	elif i % 10 == 2:
		print(f"{i}nd")
	elif i % 10 == 3:
		print(f"{i}rd")
	else:
		print(f"{i}th")

for i in range(1, 201):
	endung = str(i)[-1]
	if endung == "1":
		print(f"{i}st")
	elif endung == "2":
		print(f"{i}nd")
	elif endung == "3":
		print(f"{i}rd")
	else:
		print(f"{i}th")

# Übung 3:
# Stoppuhr
# Bevor die Minute hochtickt, müssen die Sekunden einmal eine vollkommene Umdrehung hinter sich gebracht haben
# time.sleep(Float) Funktion hier nützlich

# Übung 4:
# Erstelle eine Schleife die das kleine Einmaleins von 1 bis 10 berechnet, und jeden einzelnen
# Schritt in der Konsole ausgibt
# "1 x 1 = 1"
# "1 x 2 = 2"
# ...
# "5 x 5 = 25"
# ...
# "7 x 4 = 28"
# ...
# "10 x 10 = 100"