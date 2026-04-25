def master(code, ausgabe_ki_t):
    from main_programms import globals
    from lernen.testen.run_test import run_test
    from lernen.testen.lösungen import rückgabe_modul

    def insert_antwort(ausgabe, erwartet):
        ausgabe_ki_t.config(state = "normal")
        ausgabe_ki_t.delete(1.0, "end")
        if ausgabe and erwartet:
            ausgabe_ki_t.insert("end", f"Falsches Ergebnis: \n\"{ausgabe}\"\n\nEs wurde erwartet:\n{erwartet}")
        elif ausgabe:
            ausgabe_ki_t.insert("end", f"Falsches Ergebnis:\n{ausgabe}")
        else:
            ausgabe_ki_t.insert("end", f"Der Test wurde bestanden!")
            globals.aufgabe_prüfen_b.grid_forget()
            globals.aufgabe_anzeigen_b.grid_forget()

        ausgabe_ki_t.config(state = "disabled")


    aufgabe = globals.aufgabe_name_t
    
    inputs, erwartet = rückgabe_modul(aufgabe)
    if inputs != False: # Wenn es inputs gibt
        if isinstance(erwartet, list): # wenn es mehrere Inputs gibt
            for index, eingabe in enumerate(inputs): # für jeden input
                ausgabe = erwartet[index] # ausgabe zuordnen
                richtig, ausgabe = run_test(eingabe, ausgabe, code) # test laufen lassen
                if not richtig: # Wenn die Antwort Falsch ist
                    insert_antwort(ausgabe, erwartet[index]) # 
                    return
            insert_antwort(None, None) # Gib aus, das der Test bestanden wurde

        else: # wenn es keine Liste ist
            richtig, ausgabe = run_test(eingabe, ausgabe, code)
            if not richtig:
                insert_antwort(ausgabe, None)
                return
            insert_antwort(None, None)

    else: # Wenn es keine Inputs gibt
        richtig, ausgabe = run_test(None, erwartet, code)
        if not richtig:
            insert_antwort(ausgabe, None)
            return
        insert_antwort(None, None)