"""
Die Funktion bekommt Code und erwartete Ausgabe und inputs.
Gibt zurück, ob die erwartete Ausgabe mit der Ausgabe übereinstimmt
"""
def run_test(inputs, expected_output, usercode):
    import io, sys
    from lernen.testen.input_ersetzten import input_ersetzten

    try:
        code = input_ersetzten(usercode, inputs) # Ersetzt input mit den variablen
    except Exception as e:
        return False, f"Bitte nur {len(inputs)} inputs() verwenden." # Gibt den Fehler zurück

    def run_python(code: str):
        buffer = io.StringIO() # definiert als variable
        old_stdout = sys.stdout 
        sys.stdout = buffer # lenkt den output um

        try:
            exec(code, {}) # führt den Code aus

        except Exception as e:
            sys.stdout = old_stdout 
            return e

        sys.stdout = old_stdout
        return buffer.getvalue() # gibt die Ausgabe aus


    output = run_python(code) # speichert die Rückgabe
    try: output = output.strip()
    except: pass

    try: output = output.lower()
    except: pass

    if output == expected_output.lower():
        return(True, None)

    else:
        return(False, output)