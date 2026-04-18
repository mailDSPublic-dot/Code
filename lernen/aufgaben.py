"""
Bekommt ein Level und gibt dazu eine passende Aufgabe und die zugehörige Lösung zurück.
"""
def aufgaben(level):
    from lernen.testen import lösungen as lö

    ausgabe = None
    lösung = None

    if level == "Anleitung":
        ausgabe = \
"""
In den folgenden Aufgaben kannst du dein Wissen anwenden.
Es wird immer genau angegeben, was in der Ausgabe stehen soll.
Entweder steht es in Anführungszeichen oder man muss einfach eine Zahl ausgeben.
Bitte achte darauf, dass nur das ausgegeben wird was gefordert ist.
"""
        lösung = None


    elif level == "Begrüßung":
        ausgabe = \
"""
Schreibe ein Programm, das als Eingabe einen Namen abfragt und dann
"Hallo Name" ausgibt.
"""
        lösung = lö.begrüßung.__name__


    elif level == "Alterskontrolle":
        ausgabe = \
"""
Schreibe ein Programm, das ein Geburtsjahr abfragt.
Wenn die Person 18 Jahre oder älter ist, gib aus:
"Du bist volljährig"
sonst:
"Du bist noch minderjährig".
"""
        lösung = lö.alterskontrolle.__name__

    elif level == "Gerade oder ungerade":
        ausgabe = \
"""
Schreibe ein Programm, das eine Zahl abfragt
und ausgibt, ob sie 
"gerade"
oder
"ungerade" 
ist.
"""
        lösung = lö.gerade_ungerade.__name__


    elif level == "Notenrechner":
        ausgabe = \
"""
Schreibe ein Programm, das eine Punktzahl von 0–100 abfragt und dann eine Note ausgibt:

100–95  → "Sehr gut"
95–80   → "Gut"
80–60   → "Befriedigend"
60–40   → "Ausreichend"
40–20   → "Mangelhaft"
20–0    → "Ungenügend"
"""
        lösung = lö.notenrechner.__name__


    elif level == "Passwort abfrage":
        ausgabe = \
"""
Schreibe ein Programm, das einen Benutzernamen und ein Passwort abfragt.
Wenn der Benutzername "Max" und das Passwort "passwort" ist, gib aus:
"Anmeldung erfolgreich"
sonst:
"Anmeldung fehlgeschlagen".
"""
        lösung = lö.passwort_abfrage.__name__

    elif level == "Summe bis n":
        ausgabe = \
"""
Schreibe ein Programm, das eine Zahl n abfragt und die Summe 
aller ungeraden Zahlen von 1 bis einschließlich n berechnet und ausgibt.
"""
        lösung = lö.summe_bis_n.__name__

    elif level == "Vielfache von 3 und 5":
        ausgabe = \
"""
Schreibe ein Programm, das die Summe aller Zahlen unter 1000 berechnet,
die durch 3 oder 5 teilbar sind und die Summe dann ausgibt.
"""
        lösung = lö.vielfache_3_und_5.__name__


    elif level == "Gerade Fibonacci-Zahlen":
        ausgabe = \
"""
Die Fibonacci-Folge startet mit 1 und 2.
Jede weitere Zahl ist die Summe der beiden vorherigen.

Die ersten zehn Zahlen sind:
1, 2, 3, 5, 8, 13, 21, 34, 54, 88

Berechne die Summe aller geraden Fibonacci-Zahlen,
die kleiner als 4.000.000 sind.
"""
        lösung = lö.gerade_fibonacci_zahlen.__name__


    elif level == "Wörter zählen":
        ausgabe = \
"""
Schreibe ein Programm, das einen Satz abfragt
und ausgibt, wie viele Wörter darin vorkommen.
"""
        lösung = lö.woerter_zaehlen.__name__



    return ausgabe, lösung