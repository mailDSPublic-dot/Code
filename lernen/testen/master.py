def master(code, ausgabe_ki):
    from main_programms import globals
    from lernen.testen.run_test import run_test
    from lernen.testen.lösungen import rückgabe_modul

    def insert_antwort(ausgabe):
        ausgabe_ki.config(state = "normal")
        ausgabe_ki.delete(1.0, "end")
        if ausgabe:
            ausgabe_ki.insert("end", f"Der Test wurde nicht bestanden!\n")
        else:
            ausgabe_ki.insert("end", f"Der Test wurde bestanden!")
        ausgabe_ki.config(state = "disabled")

    aufgabe = str(globals.aufgabe_widget.get(1.0, "end"))
    aufgabe = aufgabe[9:].lower().strip()
    
    inputs, erwartet = rückgabe_modul(aufgabe)
    if inputs != False:
        if isinstance(erwartet, list):
            for index, eingabe in enumerate(inputs):
                ausgabe = erwartet[index]
                richtig, ausgabe = run_test(eingabe, ausgabe, code)
                if not richtig:
                    insert_antwort(f"Falsches Ergebnis: {ausgabe}")
                    return
            insert_antwort(None)
        else:
            richtig, ausgabe = run_test(eingabe, ausgabe, code)
            if not richtig:
                insert_antwort(f"Falsches Ergebnis: {ausgabe}")
                return
            insert_antwort(None)

    else:
        if isinstance(erwartet, list):
            for erwartung in erwartet:
                richtig, ausgabe = run_test(None, erwartung, code)
                if not richtig:
                    insert_antwort(f"Falsches Ergebnis: {ausgabe}")
                    return
            insert_antwort(None)

        else:
            richtig, ausgabe = run_test(None, erwartet, code)
            if not richtig:
                insert_antwort(f"Falsches Ergebnis: {ausgabe}")
                return
            insert_antwort(None)