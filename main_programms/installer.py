import ttkbootstrap as tk
from tkinter import filedialog
import threading, os, time, requests, subprocess
class main():
    def __init__(self):
        self.projekt_ordner = os.path.dirname(os.path.abspath(__file__))
        self.projekt_ordner = os.path.join(self.projekt_ordner, "Code")

        self.current_step = None
        self.step_start_time = None
        self.install_dir = None
        self.fehlgeschlagen = False

    def verknüpfung_erstellen(self, name, target, icon = None):
        import win32com.client

        self.current_step = "Verknüpfung erstellen"
        self.step_start_time = time.time()

        self.text.insert("end", "Erstelle Verknüpfung")

        desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
        path = os.path.join(desktop, f"{name}.lnk")

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(path)
        shortcut.TargetPath = target

        if icon:
            shortcut.IconLocation = icon
        shortcut.save()

        self.current_step = None
        self.step_start_time = None

    # Beispiel:



    def download_from_github(self, url, ziel_pfad):
        self.current_step = "Downlaod von Github"
        self.step_start_time = time.time()

        try:
            self.text.config(state = "normal")
            self.text.insert("end", "Lade Datei von GitHub herunter...\n")
            self.text.config(state = "disabled")
            request = requests.get(url, stream=True, allow_redirects=True)
            request.raise_for_status()

            with open(ziel_pfad, "wb") as file:
                for chunk in request.iter_content(chunk_size=8192):
                    file.write(chunk)

            self.text.see("end")
        except Exception as e:
            self.text.config(state = "normal")
            self.text.insert("end", f"Es gab einen Fehler beim herunterladen der Datei von Github\n\n{e}\n")
            self.text.config(state = "disabled")
            self.fehlgeschlagen = True

        self.current_step = None
        self.step_start_time = None





    def update_timer(self):
        if self.current_step and self.step_start_time:
            elapsed = time.time() - self.step_start_time
            self.timer_label.config(text=f"{self.current_step} läuft seit {elapsed:.1f} Sekunden")
        else:
            self.timer_label.config(text="")
        self.root.after(99, self.update_timer)




    # ---------------------------------------------------------
    # THREAD
    # ---------------------------------------------------------

    def herunterladen(self):
        def worker():
            if not self.install_dir:
                self.install_dir = os.path.join(os.environ["LOCALAPPDATA"], "GuidedCoding")
                if os.path.isdir(self.install_dir):
                    import shutil
                    shutil.rmtree(self.install_dir)

            os.makedirs(self.install_dir, exist_ok=True)

            ziel_exe = os.path.join(self.install_dir, "GuidedCoding.exe")
            ziel_ico = os.path.join(self.install_dir, "App_Icon.ico")

            self.download_from_github("https://github.com/mailDSPublic-dot/GuidedCoding/releases/latest/download/GuidedCoding.exe", ziel_exe)
            self.download_from_github("https://github.com/mailDSPublic-dot/GuidedCoding/releases/latest/download/App_Icon.ico", ziel_ico)
            url = "https://api.github.com/repos/mailDSPublic-dot/GuidedCoding/releases/latest"
            data = requests.get(url).json()
            tag_name = data["tag_name"]

            subprocess.run(["setx", "version_guidedcoding", tag_name], shell=True)


            self.verknüpfung_erstellen(
            "GuidedCoding",
            ziel_exe,
            ziel_ico)

            if self.fehlgeschlagen == False:
                self.text.config(state = "normal")
                self.text.insert("end", "\n✔ Alle Schritte abgeschlossen\nGuidedCoding wurde installiert.\nEine Verküpfung wurde auf dem Desktop erstellt\nSie können die App jetzt öffnen!")
                self.text.see("end")
                self.text.config(state = "disabled")
            
            else:
                self.text.config(state = "normal")
                self.text.insert("end", "\nDer Download ist Fehlgeschlagen!\n\nBitte probieren sie es später erneut oder wenden sie sich an mailDSPublic@gmx.de")
                self.text.see("end")
                self.text.config(state = "disabled")

        threading.Thread(target=worker, daemon=True).start()

        
    def speicherort_festlegen(self):
        self.install_dir = filedialog.askdirectory()
        self.text.config(state = "normal")
        self.text.insert("end", f"\nSpeicherort geändert zu \"{self.install_dir}\"\n\n")
        self.text.config(state = "disabled")

        # ---------------------------------------------------------
        # GUI
        # ---------------------------------------------------------
    def gui(self):
            
        self.root = tk.Window(themename="darkly")
        self.root.title("Installer für GuidedCoding")

        self.schritte = [
            "pywin32"
        ]

        self.text = tk.Text(self.root, wrap="word", height=12,  font=("Helvetica", 10), width = 71)
        self.text.grid(column = 0, row = 0, columnspan=2)
        self.text.insert("end", "Herzlich Willkommen im Installer von GuidedCoding:\n\n")
        self.text.insert("end", "Klicke auf 'Herunterladen', um die Installation zu starten.\n\n")

        self.text.insert("end", f"Aktueller Speicherort:   \"{os.path.join(os.environ["LOCALAPPDATA"], "GuidedCoding")}\"\n")
        self.text.config(state = "disabled")


        self.timer_label = tk.Label(self.root, text="", font=("Helvetica", 10))
        self.timer_label.grid(column = 0, row = 1, columnspan=2, pady = 10)

        self.button = tk.Button(self.root, text="Herunterladen", command= self.herunterladen)
        self.button.grid(column = 1, row = 2, pady = 10)

        self.filedia = tk.Button(self.root, text="Anderen Speicherort festlegen", command=self.speicherort_festlegen)
        self.filedia.grid(column = 0, row = 2, pady = 10)

        self.root.update_idletasks()  # Das Fenster anzeigen, um 

        window_width = self.root.winfo_width() # die größe vom Bildschirm und Fenster
        window_height = self.root.winfo_height() + 10 # berechnen zu können, 
        screenwidth = self.root.winfo_screenwidth() # um zu wissen, wo das Fenster 
        screenheight = self.root.winfo_screenheight() # angezeigt werden soll
        x_postion = int((screenwidth - window_width) // 2)
        y_position = int((screenheight - window_height) // 2.5) # leicht über der mitte des Bildschirms 

        self.root.geometry(f"{window_width}x{window_height}+{x_postion}+{y_position}") # wird das Fenster plaziert
        self.update_timer()

        self.root.mainloop()


if __name__ == "__main__":
    fenster = main()
    fenster.gui()
