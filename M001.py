# Ich bin ein Kommentar
# Mehrzeilige Kommentare existieren nicht, es muss vor jede Zeile eine # geschrieben werden

# Variablen
# name = Wert
# 4 Typen: int (Ganze Zahlen), float (Kommazahlen), str (Text), bool (Wahr-/ Falschwerte)

x = 5

# Variablen in Python sind dynamisch typisiert -> Der Inhalt bestimmt den Variablentyp, nicht umgekehrt

# Typen
# Integer (int)
# Ganze Zahl

zahl = 10

grosseZahl = 3287952943765823765982436520436580165234158923465934208689342764586

# Float (float)
# Kommazahl

kommazahl = 3542.832

grosseKommazahl = 382174923759382145329857379032.437590135713259042436597123475

# String (str)
# Text, benötigt "" oder ''

meinText = "Ein Text"
meinText2 = 'Zwei Text'

# Boolean (bool)
# Wahr/Falsch Wert, True oder False möglich

wahr = True
falsch = False

# Komplexe Zahlen (complex)
# Mathematisch undefinierte Zahlen (i)

complex = 5 + 12j

# Funktionen
# Funktionen = Methoden
# Code der schon existiert, den wir verwenden können
# Haben manchmal ein Ergebnis (Rückgabewert)

# print(Wert)
# Gibt den angegebenen Wert auf der Konsole aus
print(zahl)
print("Zwei Text")

# String Funktionen

# str.lower() und str.upper()
# Schreiben den string lowercase oder UPPERCASE
meinText.lower()  # lower() gibt einen neuen String zurück, der originale String bleibt unverändert
print(meinText.lower())
print(meinText.upper())
print(meinText)

# str.islower() und str.isupper()
# Überprüft, ob alle Zeichen in dem String lowercase oder UPPERCASE sind
print(meinText.islower())
print(meinText.isupper())

# str.count(Zeichen)
# Gibt die Anzahl der Vorkommnisse des gegebenen Zeichens zurück
print(meinText.count("E"))
print(meinText.lower().count("e"))  # Funktionen können auch verkettet werden
print(meinText)

# Strings verbinden
print(meinText + meinText2)  # Mithilfe von + können Strings "addiert" (verbunden) werden
meinText += meinText2  # Mithilfe von += kann das Ergebnis direkt in die Variable geschrieben werden
print(meinText)  # Ein TextZwei Text

# Index
# Eine Collection an einer bestimmten Stelle angreifen
# Funktioniert bei allen Aufzählungstypen (list, dict, str, ...)
# Startet bei 0
meinText[0]  # Gib mir das Zeichen an der nullten Stelle
print(meinText[0])  # E
print(meinText[0:3])  # Gib mir alle Zeichen von 0 bis exklusive 3 -> Ein (ohne Abstand)
print(meinText[-1])  # Greift die Collection von rechts an -> t
print(meinText[-4:-1])
# print(meinText[-4:0])  # Geht nicht
print(meinText[-4:])  # Nimm alles von -4 bis zum letzten Zeichen -> Text
print(meinText[3:])
print(meinText[:3])

# len(Collection)
# Gibt die Länge einer Collection zurück
# Collections haben selbst keine length oder count Funktion, hier muss len verwendet werden
print(len(meinText))  # Anzahl der Zeichen in der Liste

liste = [1, 2, 3]
len(liste)

# Arithmetische Operatoren
# +, -, *, /
# %: Modulo (Rest einer Division)
# **: Potenzierungsoperator
# //: Ganzzahldivisionsoperator
zahl1 = 5
zahl2 = 8
zahl1 + zahl2  # Verändert keine Werte/Berechnet nur das Ergebnis und wirft es danach weg
print(zahl1 + zahl2)
summe = zahl1 + zahl2

zahl1 += zahl2  # mit += wird die Addition tatsächlich durchgeführt, und das Ergebnis wird in zahl1 geschrieben

# Operator mit = kann bei jedem Operator verwendet werden
zahl1 **= zahl2  # Ergebnis der Potenzierung wird in zahl1 geschrieben
print(zahl1)

# Arithmetik mit Strings
meinText += meinText2
print(meinText * 5)  # Ein TextZwei TextZwei TextEin TextZwei TextZwei TextEin TextZwei TextZwei TextEin TextZwei TextZwei TextEin TextZwei TextZwei Text



# Übung 1
# Lege drei numerische Variablen an, addiere sie zusammen und schreibe das Ergebnis in eine neue Variable
# Potenziere danach die Variable mit sich selbst und schreibe das Ergebnis erneut in eine Variable

# Übung 2
# Nimm die potenzierte Zahl aus Übung 1 und stelle fest ob diese Restlos durch 2 teilbar (gerade) ist

# Übung 3
# Lege zwei Variablen an: Vorname befüllt mit Max und Nachname befüllt mit Mustermann
# Verbinde diese zwei Variablen und zähle danach die Buchstaben 'M' und 'm'
# Das Ergebnis soll 3 sein

# Übung 4
# Schreibe deinen Vornamen ohne Großbuchstaben in eine Variable
# Verwende danach diese Variable, und gib diese mit dem ersten Buchstaben groß geschrieben aus
