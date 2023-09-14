# Module
# Sind Libraries (Code Sammlung) die zusätzliche Funktionalitäten in unseren Code einbinden können
# Haben generell eine Thematik
# Müssen importiert und/oder installiert werden

# Wie importiere ich Module?
# Syntax:
# import <Name>: Import alles aus diesem Modul, Member des Moduls müssen mit <Name>.<Membername> angesprochen werden
# from <Name> import <Member1>, <Member2>, ...: Importiert nur bestimmte Dinge aus dem Modul. Diese Member werden in meinem Skript direkt implementiert -> können jetzt ohne Name verwendet werden
# Zusätzlich kann mit as <Alias> ein Alias vergeben werden. Dadurch kann ein Modul über diesen Alias angesprochen werden

# import M006
# M006.hallo("Lukas")  # Über den import wird Zugriff auf alle Variablen, Funktionen und Klassen (Member) ermöglicht
# print(M006.verbindeStrings("T1", "T2", "T3"))

# Bei einem Import wird IMMER das gesamte Skript ausgeführt

from M006 import hallo
hallo("Lukas")  # Hier wurde die hallo Funktion jetzt direkt implementiert
# print(verbindeStrings("T1", "T2", "T3"))  # Nicht möglich, da bei dem from import diese Funktion nicht angegeben wurde

import M006 as M
M.hallo("Lukas")  # Hier kann jetzt über M auf M006 zugegriffen werden (anschaulicher bei längeren Modulnamen)

# Main-Methode
# Wird nur dann ausgeführt, wenn das Skript direkt ausgeführt
# Wird nicht bei Imports ausgeführt
# Steht generell am Ende von einem Python Skript

# __name__
# Ist immer der Name des Skripts selbst, oder __main__ wenn das Skript direkt gestartet wird
print(__name__)

if __name__ == "__main__":
	print("Das ist das Hauptskript")