# Anzeigen des jeweiligen Levels
def level_weitergabe(string, status):
    import ttkbootstrap as tb
    from lernen.erklärungen import erklärungen
    from lernen.aufgaben import aufgaben
    from math import ceil
    if status == "a": # aufgabe
        ausgabe, lösung = aufgaben(string) # Speichert den Text der Angezeigt werden soll
    elif status == "e": # erklärungen
        ausgabe = erklärungen(string)
        lösung = None

    def button(lösung:str):
        import main_programms.globals as globals
        aufgabe_t = globals.aufgabe_widget

        aufgabe_t.config(state = "normal", width = (len(lösung)+ 9))
        aufgabe_t.delete(1.0, "end")
        aufgabe_t.insert("end", f"Aufgabe: {lösung.capitalize()}")
        aufgabe_t.config(state = "disabled", width = (len(lösung)+ 9))
        aufgabe_t.grid(row = 0, column= 0, pady = 10, sticky= "w")

        globals.prüfen_widget.grid(row = 0, column= 1, pady = 10, padx = 12, sticky= "e")

        win.destroy()
    
    def resize_text(widget:tb.Text):
        widget.tag_configure("spacing", spacing1=2, spacing2=2, spacing3=2)
        widget.config(state = "normal")
        widget.tag_add("spacing", "1.0", "end")
        widget.update_idletasks()

        lines = int(widget.index("end").split(".")[0])
        first = widget.dlineinfo("1.0")
        last = widget.dlineinfo("end-1c")

        if first and last:
            line_height = first[3]  
            extra_spacing = 4
            content_height = (
                widget.dlineinfo("end-1c")[1]
                + widget.dlineinfo("end-1c")[3]
                + extra_spacing * lines)
        
        else:
            widget.after(5, lambda: resize_text(widget))
            return

        line_height = widget.dlineinfo("1.0")[3]
        needed_lines = max(1, ceil(content_height / line_height))

        widget.config(height = needed_lines)
        widget.config(state = "disabled")

        
    win = tb.Toplevel()
    win.title(string)
    win.resizable(False, True)

    text_l = tb.Text(win, font = ("Helvetica", 12))
    text_l.config(width=60, wrap="word", background="#222222", highlightbackground="#222222", highlightcolor="#222222")
    text_l.pack(padx=20, pady=10)
    text_l.insert("end", ausgabe)

    text_l.bind("<KeyRelease>", lambda: resize_text(text_l))
    win.update()
    resize_text(text_l)

    if lösung != None:    
        ok_b = tb.Button(win, text="Aufgabe bearbeiten", command = lambda: button(lösung))
        ok_b.pack(pady=10)
    
    else:
        ok_b = tb.Button(win, text="OK", command = win.destroy)
        ok_b.pack(pady=10)

    win.update_idletasks()  # Das Fenster anzeigen, um 

    window_width = win.winfo_width() # die größe vom Bildschirm und Fenster
    window_height = win.winfo_height() # berechnen zu können, 
    screenwidth = win.winfo_screenwidth() # um zu wissen, wo das Fenster 
    screenheight = win.winfo_screenheight() # angezeigt werden soll
    x_postion = int((screenwidth - window_width) // 2)
    y_position = int((screenheight - window_height) // 2.5) # leicht über der mitte des Bildschirms 

    win.geometry(f"{window_width}x{window_height}+{x_postion}+{y_position}") # wird das Fenster plaziert

    win.mainloop()