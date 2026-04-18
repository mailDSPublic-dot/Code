"""
Das Programm bekommt einen String, welcher dann daruaf überprüft wird, ob er input( enthält. Wenn dies 
der Fall ist, wird inout( mit input_ersetzen( ersetzt und am anfang des Codes wird der Code aus
input_ersetzen eingefügt, bevor der komplette Code zurücgegeben wird.
"""

def input_ersetzten(code:str):
    if "input(" in code: #wenn input( im übergeben Code ist
        return code.replace("input(", "new_input(") #wird er ersetzt mit input_ersetzen(
    
    return code # Sonst gib den Code einfach wieder so zurück
