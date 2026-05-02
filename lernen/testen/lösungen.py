def begrüßung(): # hinzugefügt
    inputs = ["Max", "Mustermann"]
    erwartet = ["Hallo Max", "Hallo Mustermann"]
    return inputs, erwartet

def alterskontrolle(): # hinzugefügt
    inputs = ["2020", "1900"]
    erwartet = ["du bist noch minderjährig", "du bist volljährig"]
    return inputs, erwartet

def gerade_ungerade(): # hinzugefügt
    inputs = ["4", "99"]
    erwartet = ["gerade", "ungerade"]
    return inputs, erwartet

def notenrechner(): # hinzugefügt
    inputs = ["99", "92", "80", "65", "43", "22", "2"]
    erwartet = ["sehr gut", "gut", "gut", "befriedigend", "ausreichend", "mangelhaft", "ungenügend"]
    return inputs, erwartet

def passwort_abfrage(): # hinzugefügt
    inputs = [["Max", "passwort"], ["Ich", "vergessen"]]
    erwartet = ["anmeldung erfolgreich", "anmeldung fehlgeschlagen"]
    return inputs, erwartet

def summe_bis_n(): # hinzugefügt
    inputs = ["5", "100"]
    erwartet = ["15", "2500"]
    return inputs, erwartet

def vielfache_3_und_5(): # hinzugefügt
    inputs = False
    erwartet = "233168"
    return inputs, erwartet

def gerade_fibonacci_zahlen(): # hinzugefügt
    inputs = False
    erwartet = "4613732"
    return inputs, erwartet

def woerter_zaehlen(): # hinzugefügt
    inputs = ["Hallo ich bin Max Mustermann", "Ich schreibe hier 7 ganz kurze Wörter"]
    erwartet = ["5", "7"]
    return inputs, erwartet


#-----------------------------------------------------
def rückgabe_modul(name):
    name = name.strip()
    if name in aufgaben:
        return aufgaben[name]
    else:
        return None


aufgaben = {
    "begrüßung":begrüßung(),
    "alterskontrolle":alterskontrolle(),
    "notenrechner":notenrechner(),
    "passwort_abfrage":passwort_abfrage(),
    "vielfache_3_und_5":vielfache_3_und_5(),
    "gerade_fibonacci_zahlen":gerade_fibonacci_zahlen(),
    "gerade_ungerade":gerade_ungerade(),
    "summe_bis_n":summe_bis_n(),
    "woerter_zaehlen":woerter_zaehlen()
}
