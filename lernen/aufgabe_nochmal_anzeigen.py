def aufgabe_nochmal_anzeigen():
    import ttkbootstrap as tb
    from main_programms import globals

    win = tb.Toplevel(globals.root)
    win.title(globals.aufgabe_name.capitalize())

    ausgabe_t = tb.Label(win, text = globals.aufgabe, background="#222222", foreground="#FFFFFF", font = ("Helvetica", 12))
    ausgabe_t.grid(row = 0, column = 0, padx = 20, pady = 10)


    bestaetigen = tb.Button(win, text = "Bestätigen", command = win.destroy)
    bestaetigen.grid(row = 1, column = 0, pady = 20)


    win.update_idletasks()  # Das Fenster anzeigen, um 

    window_width = win.winfo_width() # die größe vom Bildschirm und Fenster
    window_height = win.winfo_height() # berechnen zu können, 
    screenwidth = win.winfo_screenwidth() # um zu wissen, wo das Fenster 
    screenheight = win.winfo_screenheight() # angezeigt werden soll
    x_postion = int((screenwidth - window_width) // 2)
    y_position = int((screenheight - window_height) // 2.5) # leicht über der mitte des Bildschirms

    win.geometry(f"{window_width}x{window_height}+{x_postion}+{y_position}") # wird das Fenster plaziert

    win.mainloop() 