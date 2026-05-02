# ersetzt alle inputs mit eingaben
def input_ersetzten(programm:str, inputs):
    zeilen = programm.splitlines()
    programm = ""
    count = 0
    input_count = 0
    def get_eingabe():
        nonlocal input_count
        if isinstance(inputs, list): 
            return inputs[input_count]
        return inputs

    for zeile in zeilen:
        if "input(" in zeile:
            eingabe = get_eingabe()
            start = zeile.find("input(") # index von input(
            ende = zeile[start + 6:] # der rest ohen input(

            anfang = zeile[:start] + '"' + eingabe + '"' # ersetzt input( mit dem test

            count = 1 # eine öffnende Klammer wurde schon gefunden
            index = 0

            while count != 0: # Solange keine schließende Klammer gefunden wurde
                zeichen = ende[index] 
                if zeichen == "(": # Wenn eine öffnende Klammer gefunden wurde
                    count += 1 # wird die variable noch eins erhöht, da noch eine schließende klammer gefunden werden muss
                elif zeichen == ")": # Wenn eine schließende Klammer gefunden wird
                    count -= 1 # Dann wird der count um eins verringert
                index += 1

            ende = ende[index:]
            zeile = anfang + ende

            if isinstance(inputs, list):
                input_count += 1 # beim nächsten mal nächsten input

        zeile += "\n"
        programm += zeile
    
    return (programm)