# In- und Output

# Es gibt mehrere in Python mehrere Funktionen für Input und Output
# print(...)

# input(String)
# Wartet auf den User, bis er eine Eingabe tätigt
# Die Eingabe kommt in das Skript hinein und kann danach verarbeitet werden

# name = input("Gib deinen Namen ein: ")
# print(f"Dein Name ist {name}")

# zahl = input("Gib eine Zahl ein: ")
# zahl = int(zahl)  # Wandle den String zu einer Zahl um -> Typecast, Cast, Casting, Konvertierung
# print(f"Die Zahl mal zwei ist {zahl * 2}")

# open
# Ermöglich uns, Dateien zu öffnen und sie auszulesen oder zu beschreiben
file = open("Test.txt", "w")
file.write("Das ist ein Test\n")
file.write("Das ist ein weiterer Test")  # Die Texte werden nur zwischengespeichert
file.flush()  # Schreibe den zwischengespeicherten Inhalt tatsächlich in die Datei
file.close()

# Die Zeilen werden in die selbe Zeile geschrieben
# -> Escape Sequenzen
# Zeichen die in Strings eingebaut werden können, die nicht einfach mit der Tastatur getippt werden können
# Escape Sequenzen fangen immer mit einem \ an, in einem String wird ein \ und das danach folgende Zeichen immer als Escape Sequenz interpretiert
# \n: Zeilenumbruch, \t: Tabulator
# https://docs.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170
text = "Das ist\nein\" Text"
text2 = 'Das ist\nein\' Text'
print(text)

pfad = "C:\\Users\\lk3\\source\\repos\\Python_Grundkurs_2023_09_11\\venv\\Scripts\\python.exe"

# rstring
# raw string
# Ignoriert Escape Sequenzen
# Besonders nützlich bei Pfaden
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2023_09_11\venv\Scripts\python.exe"

# with-Statement
# Ermöglicht, einen Stream zu öffnen und automatisch am Ende des Blocks zu schließen
# Sollte generell immer verwendet werden wenn Stream verwendet werden

with open("Test.txt", "w") as file:
	file.write("Das ist ein Test2\n")
	file.write("Das ist ein weiterer Test2")  # Die Texte werden nur zwischengespeichert

# Exists
# Prüft ob eine Datei existiert
# Befindet sich in os.path
import os.path
if os.path.exists("Test.txt"):
	print("Datei existiert bereits")

# mkdir
# Erstellt einen Ordner
import os
os.mkdir("Ordner")

# Übung 1:
# Funktion die dem User die Möglichkeiten (w, r, a) gibt
# User soll eine davon auswählen über input()
# Wenn der User keine valide Möglichkeit eingibt, soll die Eingabe wiederholt werden
# Danach soll ein File geöffnet werden und eine Erfolgsmeldung in das File geschrieben werden

# Übung 2:
# Erstelle ein Programm, das zwei Integer oder Floats abfragt
# Gib dem Nutzer die Möglichkeit per Tastendruck zwischen Addition, Subtraktion, Multiplikation und Division zu wählen.
# -> Zahl zwischen 1 und 4 -> Rechenoperation auswählen
# Bei Ungültiger Eingabe soll der Benutzer erneut nach seiner Entscheidung gefragt werden.
# Lasse das Ergebnis inklusive der Rechnung in der Konsole ausgeben
# Frage nach Ende der Operation ob der Benutzer eine neue Rechnung (Wiederholen) durchführen will
