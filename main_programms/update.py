def update():
    import os, requests, threading, time
    import ttkbootstrap as tb
    from main_programms import installer, globals


    def update_laden():
        global win
        globals.root.destroy()
        win.destroy()
        update = installer.main()
        update.gui()


    def worker():
        lokale_version = os.getenv("version_guidedcoding")
        neuste_version = None
        try:
            url = "https://api.github.com/repos/mailDSPublic-dot/GuidedCoding/releases/latest"
            data = requests.get(url).json()
            neuste_version = data["tag_name"]
        except:
            lokale_version = None

        if lokale_version != neuste_version:
            gui()

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()


    def gui():
        win = tb.Window(themename="darkly")

        text = tb.Text(win)
        text.grid(row = 0, column = 0)

        button = tb.Button(win, text = "Update laden", command = update_laden)
        button.grid(row = 1, column = 0)
        

        text.insert("end", "Es ist eine neue Version von GuidedCoding verfügbar. Aktualisierte Versionen enthalten in der Regel Verbesserungen und Fehlerbehebungen. Sie können Ihre aktuelle Version weiterhin verwenden; empfohlen wird jedoch ein Update auf die neueste Version.")

        win.mainloop()
