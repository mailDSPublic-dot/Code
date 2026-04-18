def ausgabe_generieren(eingabe, ausgabefeld_ki):
    import io
    import contextlib
    import threading
    import tkinter as tk
    from main_programms import globals
    import ttkbootstrap as tb
    from ausgabe.new_input3 import new_input

    # Damit der Code nicht in irgendwo anderes angezeigt wird, wird er abgefangen.
    stdout = io.StringIO() # Speichert den Output in eine Variable um(STanDartOUTput)

    def run_exec():
        exec_globals = {
            "__builtins__": __builtins__,
            "__name__": "__main__",
            "globals": globals,
            "new_input": new_input,
            "tb": tb,
            "tk": tk,
        }

        with contextlib.redirect_stdout(stdout): # Leitet den Output in stdout um
            exec(eingabe, exec_globals) # führt den Code aus

    try:
        # Tkinter-Code muss auf dem GUI-Hauptthread ausgeführt werden.
        if threading.current_thread() is threading.main_thread() or globals.root is None:
            run_exec()
        else:
            fertig = threading.Event()
            fehler = [None]

            def runner():
                try:
                    run_exec()
                except Exception as exc:
                    fehler[0] = exc
                finally:
                    fertig.set()

            globals.root.after(0, runner)
            fertig.wait()
            if fehler[0] is not None:
                raise fehler[0]

        yield stdout.getvalue(), None
        return "fertig", None
        
    except Exception as fehler: # Wenn ein Fehler entsteht
        zeile = None # Zeile wird initialisiert

        try: # es wird probiert 
            zeile = fehler.lineno # die Zeile auszulesen
        except:
            pass
        
        yield fehler, zeile # Es wird der Fehler und die Zeile zurückgegen

        def ki_aufruf(fehler):
            ausgabefeld_ki.config(state="normal") # setzt den Status auf bearbeitbar
            ausgabefeld_ki.delete(1.0, "end") # Löscht die vorherige Antwort
            ausgabefeld_ki.see("end")

            if globals.prüfungsmodus_an == True: # guckt, ob der Prüfungsmodus aktiviert ist, dann wird keine KI zugeschalten
                ausgabefeld_ki.insert("end", "Prüfungsmodus aktiviert!")
                ausgabefeld_ki.config(state="disabled")
                return


            from ausgabe.chatbot5 import AI
            ki = AI()

            for ausgabe in ki.chatbot(eingabe, fehler):
                if globals.anfrage == True: # Solange die Anfrage genehmigt ist
                    ausgabefeld_ki.insert("end", ausgabe) # Gibt die Ausgabe der Ki in das Textfeld einausgabe =  # Speichert die Programmausgabe
                else:
                    ausgabefeld_ki.delete(1.0, "end") # Wenn eine neue ANfrage gestartet wurde lösche den alten KI Text
                    return
                    
            ausgabefeld_ki.config(state="disabled") # Setzt anschließen wieder auf Status: nicht bearbeitbar
            globals.anfrage = False # Wenn fertig, setzte die anfrage auf gerade keine Anfrage

        if globals.anfrage == True: # Wenn gerade eine Anfrage am laufen ist
            import time
            globals.anfrage = False # dann stoppe die aktuelle Anfrage
            time.sleep(0.21) # warte 0.01 länger, als der chunk der KI braucht, dmit der Status erkannt wird
        
        globals.anfrage = True # Es wird gleich eine Anfrage gemacht

        thread = threading.Thread(target = ki_aufruf, args = (fehler,), daemon = True)
        thread.start()

        return "fertig", None
        


        
