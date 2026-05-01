def update():
    import os, requests, threading
    import ttkbootstrap as tb
    from main_programms import installer, globals

    win = None
    neuste_version = None
    lokale_version = None



    def update_laden():
        nonlocal win
        globals.root.destroy()
        update = installer.main()
        update.gui()

    def gui():
        nonlocal win
        win = tb.Toplevel(globals.root)

        win.title("Update verfügbar!")

        text = tb.Label(win, wraplength= 1000, background = "#222222", foreground="#FFFFFF", text = "Es ist eine neue Version von GuidedCoding verfügbar. Aktualisierte Versionen enthalten in der Regel Verbesserungen und Fehlerbehebungen. Sie können Ihre aktuelle Version weiterhin verwenden; empfohlen wird jedoch ein Update auf die neueste Version.")
        text.grid(row = 0, column = 0, pady = 10, padx = 8)


        button = tb.Button(win, text = "Update laden", command = update_laden)
        button.grid(row = 1, column = 0, pady = 10)

        win.update_idletasks()  # Das Fenster anzeigen, um 

        window_width = win.winfo_width() # die größe vom Bildschirm und Fenster
        window_height = win.winfo_height() # berechnen zu können, 
        screenwidth = win.winfo_screenwidth() # um zu wissen, wo das Fenster 
        screenheight = win.winfo_screenheight() # angezeigt werden soll
        x_postion = int((screenwidth - window_width) // 2)
        y_position = int((screenheight - window_height) // 2.5) # leicht über der mitte des Bildschirms 

        win.geometry(f"{window_width}x{window_height}+{x_postion}+{y_position}") # wird das Fenster plaziert



    def worker():
        nonlocal lokale_version, neuste_version

        try: lokale_version = os.getenv("version_guidedcoding") # probiert die systemvariabel version_guidedcoding auszulesen
        except: lokale_version = "Nicht_verhanden" # wenn es die nicht gibt setzte nicht_vorhanden
            
        try:
            url = "https://api.github.com/repos/mailDSPublic-dot/GuidedCoding/releases/latest"
            data = requests.get(url).json()
            neuste_version = data["tag_name"].lstrip("v")
        except: lokale_version = neuste_version
        
        if lokale_version != neuste_version: # wenn die lokale eine andere ist als die online version
            globals.root.after(0, gui) # öffne das fenster im main thread
        


    

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()





