import M008
M008.hallo("Lukas")  # Ich kann auch von hier auf M006 zugreifen (über M008 -> M006)
M008.M.hallo("Lukas")

# from M008.M import hallo
# hallo("Lukas")

# Der Modul Suchpfad
# Bestimmt, woher die Skripte von Imports kommen
# 3: Möglichkeiten
# - Der Ordner selbst (in dem das derzeitige Skript enthalten ist)
# - PYTHONPATH, der Pfad wo der Python Interpreter selbst liegt
# - Pfade, die bei der Installation von Python noch zusätzlich angegeben werden
# Wenn es nicht gefunden wird -> ModuleNotFoundError

import sys
for pfad in sys.path:
	print(pfad)  # Gibt alle Suchpfade aus

# Pakete installieren
# 2 Möglichkeiten
# - Über Python Packages
# - Über pip
#   - pip install <Name>
#   - pip uninstall <Name>

import numpy
numpy.round(5.5)

# __init__.py
# Ein Skript, dass ausgeführt wird, wenn der übergeordnete Ordner (Package) importiert wird
from Test import M008c
M008c.eineFunktion()

# Generell sinnvoller Ansatz
def main():
	pass

if __name__ == '__main__':
	main()