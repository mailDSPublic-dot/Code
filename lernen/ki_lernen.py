"""
Das Programm erstellt einen KI Chatbot. Zum lernen von Python.
"""
class AI():
    def __init__(self):
        from openai import OpenAI
        api_key_1 = "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"
        api_key_2 = "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"
        try:
            self.client = OpenAI(
                api_key=api_key_1,
                base_url="https://openrouter.ai/api/v1"
            )
        except:
            try:
                self.client = OpenAI(
                    api_key=api_key_2,
                    base_url="https://openrouter.ai/api/v1"
                )
            except:
                self.client = None
        self.gespräch = [{"role": "system", "content": "Du bist ein Lehrer, welcher Dinge für Python erklärt. Schweife nicht zu sehr aus. Antworte nur auf Fragen für Python, sonst schreibe, dass du nicht darauf ausgelegt bist diese Frage zu beantworten."}]


    def oberfläche(self):
        import sys, os
        import ttkbootstrap as tb
        from bindings.fokus_nicht_eingabe import fokus_nicht_eingabe
        from bindings.fokus_eingabe import fokus_eingabe
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # fügt den Pfad mit den fokus den Programmen, die dieses Programm sehen kann hinzu

        root = tb.Window(themename="darkly")
        root.state("zoomed")

        ausgabe = tb.Text(root, height=10, font=("Helvetica", 12))
        ausgabe.insert("1.0", "KI Ausgabe")
        ausgabe.config(state="disabled")
        ausgabe.pack(fill="both", expand=True, padx=5, pady=5)

        eingabe = tb.Text(root, height=5, font=("Helvetica", 12))
        eingabe.pack(fill="both", expand=True, padx=5, pady=5)

        bestaetigen = tb.Button(root, text="Bestätigen", bootstyle="primary", command = lambda: self.ausgabe_generieren(eingabe, ausgabe, root, bestaetigen))
        bestaetigen.pack(padx=10, pady=10, side = "right")

        eingabe.bind("<FocusIn>", lambda e: fokus_eingabe(eingabe))
        eingabe.bind("<FocusOut>", lambda e: fokus_nicht_eingabe(eingabe))

        fokus_nicht_eingabe(eingabe) # damit schon der Text eingefügt wird

        root.mainloop()


    def ausgabe_generieren(self, eingabe_f, ausgabe_f, root, button):
        self.abbrechen_flag = False
        if button["text"] == "Abbrechen":
            self.abbrechen_flag = True
            button.config(text = "Bestätigen")
            return
        
        else:
            prompt = eingabe_f.get(1.0, "end")
            eingabe_f.delete(1.0, "end")
            button.config(text = "Abbrechen")
            
            if ausgabe_f.get(1.0, "end") == "KI Ausgabe\n":
                # Löschen der Überschrift
                ausgabe_f.config(state = "normal")
                ausgabe_f.delete(1.0, "end")
                ausgabe_f.config(state = "disabled")
                # Einfügen des User-Prompts
                ausgabe_f.config(state = "normal")
                ausgabe_f.insert("end", f"User:\n{prompt}\n\n\nKI:\n")
                ausgabe_f.config(state = "disabled")

            else:
                # Einfügen des User-Prompts
                ausgabe_f.config(state = "normal")
                ausgabe_f.insert("end", f"\n\n\nUser:\n{prompt}\n\n\nKI:\n")
                ausgabe_f.config(state = "disabled")
            
            self.gespräch.append({"role" : "user", "content" : prompt})

            # Die Grafik aktualisieren, damit man auch die Änderungen sieht
            root.update()
            self.zwspeicher = ""
            self.ask_ai_openrouter(self.gespräch)
            self.stream_chunk(ausgabe_f, root, button)


            

        

    def stream_chunk(self, ausgabe_f, root, button):
        if self.abbrechen_flag == True:
            return

        try:
            chunk = next(self.response)
            text = chunk.choices[0].delta.content

        except StopIteration:
            button.config(text="Bestätigen")
            self.gespräch.append({"role" : "assistant", "content" : self.zwspeicher})
            button.config(text = "Bestätigen")
            return

        ausgabe_f.config(state = "normal")
        ausgabe_f.insert("end", text)
        ausgabe_f.config(state = "disabled")
        root.update()

        self.zwspeicher += text
        try:
            ausgabe_f.see("end")
        except:
            pass    
        root.after(10, lambda: self.stream_chunk(ausgabe_f, root, button))


    def ask_ai_openrouter(self, prompt):
        try:
            self.response = self.client.chat.completions.create( 
                model="arcee-ai/trinity-large-preview:free",
                messages=prompt,
                stream = True
            )

        except Exception as e:
            return f"Es gab ein Problem bei der Anfrage der KI, probiere es später wieder\n{e}"

    