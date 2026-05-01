import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import ttkbootstrap as tb
current_file = None # Das File gerade wurde nicht gespeichert
# Funktion Speichern unter
def speichern_unter(eingabe_code_t):
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension="*.py", # öffnet den File Dialog und speichert den Speicherort
                                            filetypes=[("Python", "*.py"),
                                            ("Textdatei", "*.txt"),
                                            ("Alle Datein", "*.*")])
    if not file_path: # Wenn das Fenster geschlossen wurde, ohne einen Pfad auszuwählen
        return

    current_file = file_path # Das File wurde gespeichert

    text = eingabe_code_t.get("1.0", "end") # holt sich den eingegeben Programmcode

    with open(file_path, "w", encoding= "utf-8") as file: # erstellt/öffnet ein File
        file.write(text) # und schreibt den Programmcode rein


# ------------------------------------------------------------------------------------------------------------
# Funktion Speichern
def speichern(eingabe_code_t):
    global current_file
    if not current_file: # Wenn noch nicht gespeichert wurde
        return speichern_unter(eingabe_code_t) # Wird speichern unter aufgerufen
    text = eingabe_code_t.get("1.0", "end") # Sonst wird der Programmcode geholt

    with open(current_file, "w", encoding = "utf-8") as file: # Ein File geöffnet/erstellt
        file.write(text) # und der Programmcode hineingeschrieben


# ------------------------------------------------------------------------------------------------------------
# Funktion Datei öffnen
def oeffnen(eingabe_code_t):
    global current_file
    from main_programms.highlight_code import highlight_code
    file_path = filedialog.askopenfilename(defaultextension="*.py", # speichert einen Filepath von angeklickten File
                                        filetypes=[("Python", "*.py"),
                                        ("Textdatei", "*.txt"),
                                        ("Alle Datein", "*.*")])
    if not file_path: # Wenn keine Datei angeklickt wurde
        return # breche ab

    current_file = file_path # Es gibt eine Datei zum speichern

    with open(current_file, "r", encoding="utf-8") as file: # öffnet das angeklickte file
        eingabe_code_t.delete("1.0", "end") # Löscht den bisher eingegeben Code
        eingabe_code_t.insert("1.0", file.read()) # Gibt den Code aus dem File ein
    highlight_code(eingabe_code_t) # und highlightet den Code


# ------------------------------------------------------------------------------------------------------------
# Funktion für eine neue Datei
def neu(eingabe_code_t):
    global current_file
    eingabe_code_t.delete("1.0", "end") # Löscht den eingegeben Code
    current_file = None # Es wurde noch nicht gespeichert


# ------------------------------------------------------------------------------------------------------------
# Funktion Ausschneiden
def cut(eingabe_code_t):
    eingabe_code_t.event_generate("<<Cut>>") # Schneidet den Code aus


# ------------------------------------------------------------------------------------------------------------
# Funktion Kopieren
def copy(eingabe_code_t):
    eingabe_code_t.event_generate("<<Copy>>") # Kopiert den Code


# ------------------------------------------------------------------------------------------------------------
# Funktion Einfügen
def paste(eingabe_code_t):
    from main_programms.highlight_code import highlight_code
    eingabe_code_t.event_generate("<<Paste>>") # Fügt den Code ein 
    highlight_code(eingabe_code_t) # und highlightet ihn


# ------------------------------------------------------------------------------------------------------------
# Funktion letzte Eingabe rückgängig machen
def undo(eingabe_code_t):
    try:
        eingabe_code_t.edit_undo() # Probiert die letzt Aktion rückgängig zu machen
    except:
        pass


# ------------------------------------------------------------------------------------------------------------
# Funktion letzte Eingabe wiederherstellen
def redo(eingabe_code_t):
    try:
        eingabe_code_t.edit_redo() # Probiert die zuletzt rückgängig gemachte Aktion wiederherzustellen 
    except:
        pass


# ------------------------------------------------------------------------------------------------------------
# Funktion zeigt alle Shortcuts an
def alle_shortcuts():
# Öffnet eine Messagebox, welche alle Shortcuts anzeigt
    messagebox.showinfo(title = "Shortcuts", message="""Control + s >> Speichern\n 
Control + z >> Rückgängig machen\n
Control + y >> Rückgängig gemachte Aktion wiederherstellen\n
Control + Enter >> Code ausführen
Tabulator >> 4 Leerzeichen""")


# ------------------------------------------------------------------------------------------------------------
# Funktion erklärt die App
def about():
# Öffnet eine Messagebox, welche einen Infotext über das Programm anzeigt
    messagebox.showinfo(title= "About", message = "Guided Coding ist ein Python‑Ausführungsframework "+ 
                        "mit integrierter Fehleranalyse. Das System führt Benutzereingaben "+
                        "aus und überwacht dabei sowohl Exceptions als auch "+
                        "Laufzeitverhalten. Sobald ein Fehler auftritt, wird automatisch ein KI‑gestütztes "+
                        "Analysemodul aktiviert. Dieses Modul interpretiert den Traceback, identifiziert "+
                        "die zugrunde liegende Ursache und liefert eine verständliche, kontextbezogene "+
                        "Erklärung inklusive möglicher Lösungsansätze.\nGuided Coding verbindet damit eine "+
                        "direkte Code‑Execution Engine mit intelligenter Fehlersicht, um Debugging‑Prozesse "+
                        "zu beschleunigen und Lernkurven deutlich zu verkürzen.")


# ------------------------------------------------------------------------------------------------------------
# Funktion zeigt mögliche Tutorials
def tutorials():
    import webbrowser
    win = tk.Toplevel() # Erstellt ein Fenster
    win.title("Tutorials") # Titel = Tutorials
    win.resizable(False, False) # Nicht vergrößer/kleinerbar
    win.grab_set() # Man muss erst das Fenster wegklicken, bevor man etwas anderes klicken kann

    message = tb.Label(win, text = " Offizielle Python Tutorials: \n https://wiki.python.org/moin/BeginnersGuide/Programmers\n \n oder ein Tutorial auf Youtube von Bro Code:\n https://www.youtube.com/watch?v=Sg4GMVMdOPo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT")
    message.grid(row = 1, column = 1, columnspan = 2, pady=10, padx = 10)

    offiziell = tb.Button(win, text = "Offizielle Python Tutorials", command = lambda: webbrowser.open("https://wiki.python.org/moin/BeginnersGuide/Programmers"))
    offiziell.grid(row = 2, column = 1, pady=10)

    inoffiziell = tb.Button(win, text = "Tutorial auf Youtube von Bro Code", command = lambda: webbrowser.open("https://www.youtube.com/watch?v=Sg4GMVMdOPo&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT"))
    inoffiziell.grid(row = 2, column = 2, pady=10)

    win.update_idletasks()  # Das Fenster anzeigen, um 

    window_width = win.winfo_width() # die größe vom Bildschirm und Fenster
    window_height = win.winfo_height() # berechnen zu können, 

    screenwidth = win.winfo_screenwidth() # um zu wissen, wo das Fenster 
    screenheight = win.winfo_screenheight() # angezeigt werden soll

    x_postion = int((screenwidth - window_width) // 2)
    y_position = int((screenheight - window_height) // 2.5) # leicht über der mitte des Bildschirms 

    win.geometry(f"{window_width}x{window_height}+{x_postion}+{y_position}") # wird das Fenster plaziert

    win.mainloop() # Initialisiert das Fenster


# ------------------------------------------------------------------------------------------------------------
# Funktion aktiviert den Prüfungsmodus
def prüfungsmodus(prüfungsmodus_t, status):
    import threading, time, os, datetime
    from main_programms import globals
    from time import sleep
    variablen = {}
    datei_ordner = os.path.dirname(os.path.abspath(__file__)) # der order des aktuellen files
    config_dateipfad = os.path.join(datei_ordner, "config.txt") # der Pfadname zu einer "config.txt" Datei im Ordner
    

    def aktualisiere_datei():
        with open(config_dateipfad, "w") as f:
            for key, value in variablen.items():
                f.write(f"{key} = {value}\n")

    def worker(endzeit, config_dateipfad):
        nonlocal variablen
        if globals.lernen_untermenu == None: # Wenn das Menu beim start noch nicht initiiert worde
            sleep(0.01) # warte 10ms
            worker(endzeit, config_dateipfad) # starte die funktion neu
            return # beende die alte Funktion
        
        globals.lernen_untermenu.entryconfig(0, state= "disabled") # deaktiert die KI
        globals.lernen_untermenu.entryconfig(1, state= "disabled") # deaktiviert das Lernen Untermenu

        datum = datetime.datetime.fromtimestamp(endzeit) # bekommt das koplette Datum
        uhrzeit = datum.strftime("%H:%M") # Nimmt nur die Stunden und die Minuten

        globals.prüfungsmodus_an = True # Setzt den Prüfungsmodus für alle Programme auf True

        prüfungsmodus_t.grid(row = 0, column= 0, pady = 10, sticky= "w")
        prüfungsmodus_t.delete(1.0, "end")
        prüfungsmodus_t.insert("end", f"Prüfungsmodus bis {uhrzeit}Uhr")
        prüfungsmodus_t.config(state = "disabled")

        variablen["pruefungsmodus"] = endzeit
        aktualisiere_datei()

        while time.time() < endzeit: # solgange die aktuelle zeit vor der endzeit ist
            time.sleep(1) # schlafe eine Sekunde

        try: 
            del variablen["pruefungsmodus"]
            aktualisiere_datei()
        except: pass
            

        globals.prüfungsmodus_an = False # setzt den globalen Prüfungsmudus auf aus
        prüfungsmodus_t.grid_forget() # löscht die Anzeige für den Prüfungsmodus


    if os.path.exists(config_dateipfad): # wenn die datei schon existiert
        with open(config_dateipfad, "r", encoding="utf-8") as f: # öffne sie lesend
            exec(f.read(), {}, variablen)

            if "pruefungsmodus" in variablen:
                endzeit = float(variablen["pruefungsmodus"]) # wandle in eine Kommazahl um

                if endzeit < time.time(): # wenn die Zeit kleiner als die aktuelle ist
                    del variablen["pruefungsmodus"]
                    aktualisiere_datei()
                    return
            else:
                if status == 0:
                    return
                zeit_gerade = time.time() # bekomme die aktuelle zeit
                endzeit = zeit_gerade + 43200 # berechne die endzeit (Zeit gerade + 12 Stunden)
    else:
        zeit_gerade = time.time() # bekomme die aktuelle zeit
        endzeit = zeit_gerade + 43200 # berechne die endzeit (Zeit gerade + 12 Stunden)


    threading.Thread(target=worker, args=(endzeit, config_dateipfad,), daemon=True).start() # starte den Thread, welcher den Prüfungsmodus anschaltet