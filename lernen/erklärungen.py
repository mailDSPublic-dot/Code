def erklärungen(level):
    ausgabe = None

    if level == "Datentypen":
        # Beschreibung
        ausgabe = \
"""
Datentypen geben an, welche Art von Wert gespeichert wird.
Wichtige Datentypen sind:

int  → ganze Zahl (z.B. 25)
float → Kommazahl (z.B. 2.5)
str  → Text (z.B. "Hallo")
bool → Wahr/Falsch (True/False)

Beispiele:

zahl = 25
kommazahl = 2.5
text = "Hallo"
wahrheit = True

Man kann Datentypen umwandeln:
str(52) → "52"
int("eins") → Fehler
"""

    elif level == "Variablen":
        # Beschreibung
        ausgabe = \
"""
Variablen speichern Werte, die du später wieder benutzen kannst.
Du gibst ihnen einen Namen und einen Wert.

Beispiele:

name = "Max"
alter = 25
preis = 4.99
fertig = True
"""

    elif level == "print":
        # Beschreibung
        ausgabe = \
"""
print() zeigt etwas auf dem Bildschirm an.
Alles in den Klammern wird ausgegeben.

Beispiel:

print("Hallo")
"""

    elif level == "Rechenoperatoren":
        # Beschreibung
        ausgabe = \
"""
Python kann mit verschiedenen Rechenzeichen arbeiten:

+  Addition
-  Subtraktion
*  Multiplikation
/  Division
// Ganzzahlige Division
%  Rest (Modulo)
** Potenz

Beispiel:
ergebnis = 5 + 3
"""

    elif level == "Mathematische Rechenoperatoren":
        # Beschreibung
        ausgabe = \
"""
So rechnest du in Python:

ergebnis = 35 + 7     # 42
ergebnis = 90 - 48    # 42
ergebnis = 7 * 6      # 42
ergebnis = 126 / 3    # 42.0
ergebnis = 128 // 3   # 42
ergebnis = 192 % 50   # 42
ergebnis = 2 ** 6     # 64
"""

    elif level == "Rechenoperationen mit Strings":
        # Beschreibung
        ausgabe = \
"""
Mit Strings kannst du + und * benutzen.

Beispiele:

"Hi" + "Du" → "HiDu"
3 * "Ha" → "HaHaHa"
"""

    elif level == "input":
        # Beschreibung
        ausgabe = \
"""
input() wartet auf eine Eingabe des Nutzers.
Die Eingabe ist immer ein Text (String).

Beispiel:

name = input("Wie heißt du? ")
"""

    elif level == "if-Bedingung, else":
        # Beschreibung
        ausgabe = \
"""
Mit if prüfst du eine Bedingung.
Ist sie True (wahr), wird der Code ausgeführt.
else passiert, wenn die Bedingung falsch ist.

Beispiel:

if zahl > 10:
    print("Groß")
else:
    print("Klein")
"""

    elif level == "elif-Bedingung":
        # Beschreibung
        ausgabe = \
"""
elif bedeutet: „wenn die nächste Bedingung stimmt“.
Damit kannst du mehrere Fälle prüfen.

Beispiel:

if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
else:
    print("Andere Note")
"""

    elif level == "while-Schleife":
        # Beschreibung
        ausgabe = \
"""
Eine while-Schleife wiederholt Code,
solange die Bedingung wahr ist.

Beispiel:

zahl = 1
while zahl <= 5:
    print(zahl)
    zahl += 1
"""

    elif level == "for-Schleife":
        # Beschreibung
        ausgabe = \
"""
Eine for-Schleife wiederholt Code eine bestimmte Anzahl von Malen.
range(start, ende) zählt bis ende-1.

Beispiel:

for i in range(1, 6):
    print(i)
"""

    elif level == "Listen Überblick":
        # Beschreibung
        ausgabe = \
"""
Listen speichern mehrere Werte in einer Variable.

Beispiele:

zahlen = [1, 2, 3]
woerter = ["Hallo", "ich", "bin", "Max", "Mustermann"]
"""

    elif level == "Listen-Zugriff":
        # Beschreibung
        ausgabe = \
"""
Auf Listen greifst du über den Index zu.
Der erste Index ist 0. Du kannst auch von hinten (-anzahl) zugreifen.

Beispiele:

zahlen = [10, 20, 30, 40]

zahlen[0] → 10
zahlen[-1] → 40

Elemente hinzufügen:
zahlen.append(5)
zahlen.insert(1, 30)
zahlen.extend([4, 9])
"""

    elif level == "Listen-Zugriff mit for":
        # Beschreibung
        ausgabe = \
"""
Mit einer for-Schleife kannst du alle Elemente einer Liste durchgehen.

Beispiel:

zahlen = [1, 2, 3]

for x in zahlen:
    print(x)
"""

    elif level == "Listen-Befehle":
        # Beschreibung
        ausgabe = \
"""
Wichtige Listenbefehle:

remove() → entfernt Wert
pop() → entfernt Element an einem Index
len() → Länge der Liste
clear() → leert die Liste
sort() → sortiert die Liste

Beispiel:

zahlen = [3, 1, 4]

zahlen.remove(1)
wert = zahlen.pop(0)
laenge = len(zahlen)
zahlen.sort()
"""

    elif level == "Vergleichsoperatoren":
        ausgabe = \
"""
Vergleichsoperatoren werden benutzt, um zwei Werte zu vergleichen.
Sie liefern immer True oder False zurück.

Wichtige Vergleichsoperatoren:
==  gleich
!=  ungleich
<   kleiner als
>   größer als
<=  kleiner oder gleich
>=  größer oder gleich

Beispiele:
5 == 5   → True
3 != 4   → True
2 < 1    → False
"""

    elif level == "Logische Operatoren":
        ausgabe = \
"""
Logische Operatoren verbinden mehrere Bedingungen.

Wichtige logische Operatoren:
and  → beide Bedingungen müssen wahr sein
or   → mindestens eine Bedingung muss wahr sein
not  → kehrt den Wahrheitswert um

Beispiele:
2 == 1 + 1 and 3 == 4 - 2  → False
2 == 1 + 1 or 3 == 4 - 2   → True
not 2 == 1 + 1             → False
"""

    elif level == "def":
        ausgabe = \
ausgabe = """
Funktionen helfen dir, Code übersichtlich zu machen.
Du kannst damit eigene Befehle erstellen, die du später wieder aufrufen kannst.

Eine Funktion wird mit def erstellt.
Der Name steht hinter def, danach kommen Klammern und ein Doppelpunkt.

Beispiel:

def begruessung():
    print("Hallo!")

Eine Funktion wird so aufgerufen:

begruessung()

Funktionen können auch Werte zurückgeben:

def addiere(a, b):
    return a + b

ergebnis = addiere(3, 5)   # ergebnis = 8
"""





    return ausgabe