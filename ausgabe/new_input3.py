"""
Das Programm bekommt einen String übergeben, zeigt den in einem neuen Fenster an und erwartet eine Eingabe
Diese Eingabe wird dann zurückgegeben. Soll die Input-funktion immitieren.
"""

import ttkbootstrap as tb

from main_programms import globals

def new_input(prompt: str):
    win = tb.Toplevel(globals.root)

    win.title("Input")
    win.minsize(400, 200)
    win.grab_set()

    result = [""]

    def bestaetigen():
        result[0] = entry.get()
        win.destroy()

    label = tb.Label(win, text=prompt, font=("Helvetica", 12))
    label.pack(pady=20)

    entry = tb.Entry(win, font=("Helvetica", 12))
    entry.pack(pady=10)
    entry.focus()

    btn = tb.Button(win, text="Bestätigen", command=bestaetigen)
    btn.pack(pady=20)

    win.bind("<Return>", lambda e: bestaetigen())

    win.update()
    
    window_width = win.winfo_width() # die größe vom Bildschirm und Fenster
    window_height = win.winfo_height() # berechnen zu können, 
    screenwidth = win.winfo_screenwidth() # um zu wissen, wo das Fenster 
    screenheight = win.winfo_screenheight() # angezeigt werden soll
    x_postion = int((screenwidth - window_width) // 2)
    y_position = int((screenheight - window_height) // 2.5) # leicht über der mitte des Bildschirms 

    win.geometry(f"{window_width}x{window_height}+{x_postion}+{y_position}") # wird das Fenster plaziert

    win.wait_window()


    return result[0]
