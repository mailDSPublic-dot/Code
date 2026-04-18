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

    win.wait_window()


    return result[0]
