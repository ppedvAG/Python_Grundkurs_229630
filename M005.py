# List Comprehension
# Gibt die Möglichkeit, schnell aus einer Schleife eine Liste zu erzeugen
# Das Muster wird über eine Schleife dargestellt, daraus wird dann eine Liste

# Mit Schleife
zahlen = []
for i in range(1, 11):
	zahlen.append(i)
print(zahlen)

# Mit List Comprehension
zahlenLC = [i for i in range(1, 11)]  # Hier in der Klammer eine Schleife angeben, danach vor die Schleife gehen und den Variablennamen einsetzen
print(zahlenLC)

# Alle geraden Zahlen von 1 bis 100
zahlenGerade = []
for i in range(1, 101):
	if i % 2 == 0:
		zahlenGerade.append(i)
print(zahlenGerade)

# Mit LC
zahlenGeradeLC = [i for i in range(1, 101) if i % 2 == 0]  # Es können nach der Schleife noch Bedingungen in Form einer If hinzugefügt werden
print(zahlenGeradeLC)

# Alle Zahlen hoch sich selbst
zahlenPotenziert = []
for i in range(1, 101):
	zahlenPotenziert.append(i ** i)
print(zahlenPotenziert)

# Mit LC
zahlenPotenziertLC = [i ** i for i in range(1, 101)]  # Hier kann der Wert beeinflusst werden, bevor er in die Liste geschrieben wird
print(zahlenPotenziertLC)

# Kleines 1x1 mit List Comprehension
kleines1x1 = [f"{i}*{j}={i * j}" for i in range(1, 11) for j in range(1, 11)]  # Verschachtelte Schleife mit List Comprehension
print(kleines1x1)

# List Comprehension mit Ternary Operator
# Links kann auch if-else eingebaut werden, um den Ausdruck zu verändern

# Liste von 1 bis 100, bei der bei jeder Zahl mit erwähnt wird, ob die gerade oder ungerade ist
geradeUngerade = [f"{i} gerade" if i % 2 == 0 else f"{i} ungerade" for i in range(1, 101)]  # Links wird nur beeinflusst, wie die Elemente ausschauen
print(geradeUngerade)

durch3 = [f"{i} durch 3 teilbar" if i % 3 == 0 else f"{i} nicht durch 3 teilbar" for i in range(1, 101)]  # Links wird nur beeinflusst, wie die Elemente ausschauen
print(durch3)

# List Comprehension mit einer String Liste
stringListe = ["DaS", "isT", "eInE", "LisTE"]

# Alle Wörter finden mit einem großen Anfangsbuchstaben
kleinGross = [s for s in stringListe if s[0].isupper()]
print(kleinGross)

# Alle Wörter finden, die ein e enthalten innerhalb von einem Text
text = "Das ist ein Text der einige Wörter enthält"
textListe = text.split(" ")
print(textListe)  # ['Das', 'ist', 'ein', 'Text', 'der', 'einige', 'Wörter', 'enthält']

enthaeltE = [wort for wort in textListe if "e" in wort]
enthaeltECount = [wort for wort in textListe if wort.count("e") > 0]
print(enthaeltE)

# Übung 1
# Schreibe eine List-Comprehension die nur Zahlen aus einer Range von 1 bis inklusive 30 in die neue Liste packt,
# falls die Zahl durch 6 teilbar ist
# Bevor die Zahl in die neue Liste gepackt wird, soll sie um 12 erhöht werden

# Übung 2
# Schreibe eine List-Comprehension die aus einem Text alle Kleinbuchstaben nimmt und Groß in die Liste schreibt

# Übung 3
# Schreibe eine List-Comprehension die aus einem Text alle Anfangsbuchstaben nimmt

# Übung 4
# Schreibe eine List-Comprehension die aus einem Text alle Wörter nimmt die 3 oder weniger Zeichen haben
