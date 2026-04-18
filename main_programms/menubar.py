def menubar(root, eingabe_code_t, prüfungsmodus):
    import ttkbootstrap as tb
    import main_programms.menubar_commands as menucom
    from lernen.fenster_lernen import level_weitergabe
    from lernen.ki_lernen import AI
    from main_programms import globals

    def ki():
        ai = AI()
        ai.oberfläche()

    # Menübar
    menubar = tb.Menu(root) # Erstellen einer Menubar 

    #File Menu
    file_menu = tb.Menu(menubar, tearoff=0) # Hinzufügen des File-Menus zur Menubar
    file_menu.add_command(label = "Neu", command = lambda: menucom.neu(eingabe_code_t)) # Buttons zum File-Menu hinzufügen
    file_menu.add_command(label = "Öffnen", command = lambda : menucom.oeffnen(eingabe_code_t))
    file_menu.add_command(label = "Speichern", command = lambda : menucom.speichern(eingabe_code_t))
    file_menu.add_command(label = "Speichern unter", command = lambda : menucom.speichern_unter(eingabe_code_t))
    file_menu.add_command(label = "Beenden", command = globals.root.destroy)
    menubar.add_cascade(label = "File", menu = file_menu) # Anzeigen des File Menus auf der Menuleiste



    # Edit Menu
    edit_menu = tb.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Ausschneiden", command = lambda : menucom.cut(eingabe_code_t))
    edit_menu.add_command(label="Kopieren", command = lambda : menucom.copy(eingabe_code_t))
    edit_menu.add_command(label="Einfügen", command = lambda : menucom.paste(eingabe_code_t))
    edit_menu.add_command(label="Undo", command = lambda : menucom.undo(eingabe_code_t))
    edit_menu.add_command(label = "Redo", command = lambda : menucom.redo(eingabe_code_t))
    
    menubar.add_cascade(label = "Edit", menu = edit_menu)


    # Lernen Menu
    lernen_menu = tb.Menu(menubar, tearoff = 0)

    lernen_untermenu = tb.Menu(lernen_menu, tearoff = 0)
    rechenoperationen_m = tb.Menu(lernen_menu, tearoff = 0)
    listen_m = tb.Menu(lernen_menu, tearoff = 0)
    

    lernen_untermenu.add_command(label = "Datentypen", command = lambda : level_weitergabe("Datentypen", "e")) # gibt den namen und ob aufgabe(a) oder erklärung (e) weiter
    lernen_untermenu.add_command(label = "Variablen", command = lambda : level_weitergabe("Variablen", "e"))
    lernen_untermenu.add_command(label = "print()", command = lambda : level_weitergabe("print", "e"))
    lernen_untermenu.add_command(label = "input()", command = lambda : level_weitergabe("input", "e"))
    lernen_untermenu.add_command(label = "Vergleichsoperatoren", command = lambda : level_weitergabe("Vergleichsoperatoren", "e"))
    lernen_untermenu.add_command(label = "if, else", command = lambda : level_weitergabe("if-Bedingung, else", "e"))
    lernen_untermenu.add_command(label = "Logische Operatoren", command = lambda : level_weitergabe("Logische Operatoren", "e"))
    lernen_untermenu.add_command(label = "elif", command = lambda : level_weitergabe("elif-Bedingung", "e"))
    lernen_untermenu.add_cascade(label = "Rechenarten", menu = rechenoperationen_m)
    rechenoperationen_m.add_command(label = "Rechenoperatoren", command = lambda:level_weitergabe("Rechenoperatoren", "e"))
    rechenoperationen_m.add_command(label = "Mathematische RO", command = lambda:level_weitergabe("Mathematische Rechenoperatoren", "e"))
    rechenoperationen_m.add_command(label = "RO mit Strings", command = lambda:level_weitergabe("Rechenoperationen mit Strings", "e"))
    lernen_untermenu.add_command(label = "while", command = lambda : level_weitergabe("while-Schleife", "e"))
    lernen_untermenu.add_command(label = "for", command = lambda : level_weitergabe("for-Schleife", "e"))
    lernen_untermenu.add_cascade(label = "Listen", menu = listen_m)
    listen_m.add_command(label = "Listen Überblick", command= lambda: level_weitergabe("Listen Überblick", "e"))
    listen_m.add_command(label = "Listen-Zugriff", command= lambda: level_weitergabe("Listen-Zugriff", "e"))
    listen_m.add_command(label = "Listen-Zugriff mit for", command = lambda : level_weitergabe("Listen-Zugriff mit for", "e"))
    listen_m.add_command(label = "Listen-Befehle", command= lambda: level_weitergabe("Listen-Befehle", "e"))
    lernen_untermenu.add_command(label = "def", command = lambda : level_weitergabe("def", "e"))


    komplexe_aufgaben_menu = tb.Menu(lernen_menu, tearoff = 0)
    komplexe_aufgaben_menu.add_command(label = "Anleitung", command = lambda : level_weitergabe("Anleitung", "a"))
    komplexe_aufgaben_menu.add_command(label = "Gerade oder ungerade", command = lambda : level_weitergabe("Gerade oder ungerade", "a"))
    komplexe_aufgaben_menu.add_command(label = "Begrüßung", command = lambda : level_weitergabe("Begrüßung", "a"))
    komplexe_aufgaben_menu.add_command(label = "Alterskontrolle", command = lambda : level_weitergabe("Alterskontrolle", "a"))
    komplexe_aufgaben_menu.add_command(label = "Login", command = lambda : level_weitergabe("Passwort abfrage", "a"))
    komplexe_aufgaben_menu.add_command(label = "Summe bis n", command = lambda : level_weitergabe("Summe bis n", "a"))
    komplexe_aufgaben_menu.add_command(label = "Notenrechner", command = lambda : level_weitergabe("Notenrechner", "a"))
    komplexe_aufgaben_menu.add_command(label = "Vielfache von 3 und 5", command = lambda : level_weitergabe("Vielfache von 3 und 5", "a"))
    komplexe_aufgaben_menu.add_command(label = "Gerade Fibinacci-Zahlen", command = lambda : level_weitergabe("Gerade Fibonacci-Zahlen", "a"))
    komplexe_aufgaben_menu.add_command(label = "Wörter zählen", command = lambda : level_weitergabe("Wörter zählen", "a"))


    lernen_menu.add_command(label = "KI zum Lernen", command = ki)
    
    lernen_menu.add_cascade(label = "Lernen", menu = lernen_untermenu)
    lernen_menu.add_cascade(label = "Komplexe Aufgabe", menu = komplexe_aufgaben_menu)

    menubar.add_cascade(label = "Lernen", menu = lernen_menu)


    # Hilfe Menu
    hilfe = tb.Menu(menubar, tearoff=0)
    hilfe.add_command(label = "Prüfungsmodus", command = lambda: menucom.prüfungsmodus(prüfungsmodus, 1))
    hilfe.add_command(label = "Shortcuts", command = menucom.alle_shortcuts)
    hilfe.add_command(label = "Tutorials", command = menucom.tutorials)
    hilfe.add_command(label = "About", command =  menucom.about)
    menubar.add_cascade(label = "Hilfe", menu = hilfe)

    return menubar