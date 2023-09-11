# List
# Typ, der mehrere Werte halten kann
# Hat einen Index
# Ist veränderbar, bestehende können verändert/entfernt werden und neue Elemente können hinzugefügt werden
# Duplikate sind erlaubt
# Verschiedene Datentypen sind erlaubt (sollte vermieden werden)

meineListe = [1, 2, 3, 4, True, "Ein Text"]
print(meineListe)

# Mittels Index auf Elemente zugreifen
print(meineListe[0])  # 1
print(meineListe[0:3])  # [1, 2, 3]
print(meineListe[-1])  # Ein Text

# Einen Wert in der Liste aktualisieren
meineListe[0] = 10
print(meineListe)

# List Funktionen
# list.append(Element)
# Fügt ein Element am Ende an
meineListe.append(50)  # Einzelnes Element anhängen
print(meineListe)

meineListe += [50, 100]  # Liste von Elementen anhängen (Elemente werden ausgepackt aus der gegebenen Liste)
meineListe.append([50, 100])  # Hier wird eine Liste angehängt, unpraktisch
meineListe.extend([50, 100])  # Selbiges wie +=, nur als Funktion
print(meineListe)

# list.pop(Index)
# Entfernt ein Element am gegebenen Index
meineListe.pop(9)
print(meineListe)

meineListe.remove("Ein Text")  # Sucht ein Element, und entfernt das erste Vorkommen davon
meineListe.insert(4, False)  # Fügt ein Element an einer bestimmten Stelle ein
meineListe.sort()
print(meineListe)

# len(List)
# Gibt die Länge der Liste aus
print(len(meineListe))


# Tuple
# Verhält sich ähnlich wie die Liste
# Hat auch einen Index und Funktionen
# Es kann nicht verändert werden
# Duplikate sind erlaubt
meinTupel = (1, 2, 3, 4)  # Über die Klammern wird der Typ des Objekts bestimmt (normale Klammern: Tupel, eckige Klammern: List, geschwungene Klammern: Set oder Dictionary)
print(meinTupel)

print(meinTupel[0])
# meinTupel[0] = 2  # Nicht möglich

# Tupel über Umweg anpassen
temp = list(meinTupel)
temp[0] = 10
meinTupel = tuple(temp)
print(meinTupel)

# Unpacking
# "Auspacken"
# Zerlegt eine Collection in ihre Einzelteile, und schreibt diese Teile in einzelne Variablen
a, b, c, d = meinTupel
print(a)
print(b)
print(c)
print(d)

# Funktioniert bei allen iterierbaren Typen
a, b, c, d = "Test"
print(a)
print(b)
print(c)
print(d)


# Range
# Ermöglicht, das erstellen von einer Sequenz von Zahlen
# Wird häufig in Schleifen verwendet
# Enthält keine Werte, sondern nur einen Bereich der "gemerkt" wird
# Range wird tatsächlich generiert, wenn es zu einer Liste konvertiert wird
print(range(10000000000000))  # range Objekt (keine konkreten Werte)
# print(list(range(100_000_000)))  # Wandle mir dieses Range Objekt zu einer Liste um

print(list(range(100)))  # Liste von 0-99 (Obergrenze exkludiert)
print(list(range(-10, 10)))  # Liste von -10 bis 9
print(list(range(0, 100, 5)))  # Nur jede 5te Zahlen von 0 bis 100


# Set
# Funktioniert ähnlich wie Liste (Elemente hinzufügen und entfernen)
# WICHTIG: Kann keine Duplikate enthalten
meinSet = {1, 2, 3}
print(meinSet)

meinSet.add(4)
print(meinSet)

meinSet.add(4)
print(meinSet)

# Häufigster Anwendungsfall: Duplikate entfernen
duplikatListe = [1, 2, 2, 2, 3, 4, 4, 5]
duplikatListe = set(duplikatListe)
duplikatListe = list(duplikatListe)
print(duplikatListe)


# Dictionary
# Liste von Key-Value Paaren
# Index, Duplikate erlaubt, neue Elemente, Elemente entfernen, Elemente bearbeiten
# Keys müssen eindeutig sein
meinCar = {
	"Marke": "Audi",
	"Modell": "A3",
	"Baujahr": 2017
}

print(meinCar)

print(meinCar["Marke"])  # Hier einzelne Werte über einen Textbasierten Index statt einem Nummernbasierten Index angreifen

# Schlüssel hinzufügen oder anpassen
meinCar["KM"] = 10000
print(meinCar)

meinCar["KM"] = 20000
print(meinCar)

# dict.pop(Index)
# Element entfernen am gegebenen Index
meinCar.pop("KM")
print(meinCar)

meinCar["Baujahr"] = None  # None = null
print(meinCar)  # Hier wird Baujahr nicht gelöscht, sondern entleert

# dict.items(), dict.keys(), dict.values()
# Gibt die Items als Liste von Tupeln zurück, oder die Keys/Values als Liste
print(meinCar.keys())
print(meinCar.values())
print(meinCar.items())


# Konvertierungen
# Typen von einer Variable in einen anderen Typen umwandeln
# Jeder Typ hat einen Konstruktor der dem Namen des Typens entspricht
print(int(4.9))  # Versucht, 4.5 zu einem int zu konvertieren (Kommastellen werden abgeschnitten)
print(str(3))  # Versucht, 3 in einen String zu konvertieren
# print(list(3))  # Versucht, 3 in eine Liste zu konvertieren (nicht möglich)
print(list([3]))
print([3])
print(tuple([1, 2, 3]))
print(int(True))  # 1
print(int(False))  # 0
print(bool(0))  # False
print(bool(-1))  # True

# Übung 1
# Wir haben 3 vorgegebene Listen
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]
# Kombiniere die drei Listen in eine ganze Liste und schließe Duplikate aus

# Übung 2
# Erstelle einen String und wandele ihn in eine Liste um, dabei soll jedes einzelne Zeichen ein Element der Liste werden

# Übung 3
# Lasse eine Liste erstellen die bei 0 beginnt und alle geraden Zahlen bis 20 enthält
# Nicht selbst schreiben, sondern Python machen lassen
