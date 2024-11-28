import time
from datetime import datetime
from io import StringIO, BytesIO
import customtkinter
from customtkinter import *
from PIL import Image
import json
from ftplib import FTP, error_perm, all_errors
import threading

def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

class ToplevelWindow(customtkinter.CTkToplevel):
    def save_changes(self):
        with open("config.json", "r") as json_file:
            config = json_file.read()
        with open("config.json", "w") as json_file:
            new_config = json.loads(config)
            new_config['chat_username'] = self.chat_username.get("0.0", "end").strip()
            new_config['chatlog_path'] = self.chatlog_path.get("0.0", "end").strip()
            new_config['ftp_username'] = self.ftp_username.get("0.0", "end").strip()
            new_config['ftp_password'] = self.ftp_password.get("0.0", "end").strip()
            new_config['ftp_server'] = self.ftp_server.get("0.0", "end").strip()
            new_config_json = json.dumps(new_config, indent=2)
            json_file.write(new_config_json)
            print("Config Saved Successfully")
            self.destroy()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(CenterWindowToDisplay(self, 500, 450, self._get_window_scaling()))
        self.resizable(False, False)
        self.title("FTP Settings")

        with open("config.json", "r") as json_file:
            config1 = json_file.read()
            config2 = json.loads(config1)
            chat_username = config2['chat_username']
            chatlog_path = config2['chatlog_path']
            ftp_username = config2['ftp_username']
            ftp_password = config2['ftp_password']
            ftp_server = config2['ftp_server']


        self.title1 = CTkLabel(self, text="FTP Settings", anchor="n", font=CTkFont(size=14))
        self.title1.place(rely=0.02, relx=0.41)

        self.chat_username_label = customtkinter.CTkLabel(self, text="Chat Username", anchor="nw")
        self.chat_username_label.place(rely=0.10, relx=0.05)

        self.chat_username = CTkTextbox(master=self, corner_radius=8, height=25, width=450,  border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFCC70")
        self.chat_username.place(relx=0.05, rely=0.14)
        self.chat_username.insert("0.0", chat_username)

        self.chatlog_path_label = customtkinter.CTkLabel(self, text="Chatlog Path", anchor="nw")
        self.chatlog_path_label.place(rely=0.26, relx=0.05)

        self.chatlog_path = CTkTextbox(master=self, corner_radius=8, height=25, width=450, border_color="#FFCC70",
                                        border_width=2, scrollbar_button_color="#FFCC70")
        self.chatlog_path.place(relx=0.05, rely=0.30)
        self.chatlog_path.insert("0.0", chatlog_path)

        self.ftp_username_label = customtkinter.CTkLabel(self, text="FTP Username", anchor="nw")
        self.ftp_username_label.place(rely=0.42, relx=0.05)

        self.ftp_username = CTkTextbox(master=self, corner_radius=8, height=25, width=450, border_color="#FFCC70",
                                        border_width=2, scrollbar_button_color="#FFCC70")
        self.ftp_username.place(relx=0.05, rely=0.46)
        self.ftp_username.insert("0.0", ftp_username)

        self.ftp_password_label = customtkinter.CTkLabel(self, text="FTP Password", anchor="nw")
        self.ftp_password_label.place(rely=0.58, relx=0.05)

        self.ftp_password = CTkTextbox(master=self, corner_radius=8, height=25, width=450, border_color="#FFCC70",
                                       border_width=2, scrollbar_button_color="#FFCC70")
        self.ftp_password.place(relx=0.05, rely=0.62)
        self.ftp_password.insert("0.0", ftp_password)

        self.ftp_port_label = customtkinter.CTkLabel(self, text="FTP Server IP", anchor="nw")
        self.ftp_port_label.place(rely=0.74, relx=0.05)

        self.ftp_server = CTkTextbox(master=self, corner_radius=8, height=25, width=150, border_color="#FFCC70",
                                       border_width=2, scrollbar_button_color="#FFCC70")
        self.ftp_server.place(relx=0.05, rely=0.78)
        self.ftp_server.insert("0.0", ftp_server)

        save_img = Image.open("icons/save_icon.png")

        self.save_changes_btn = CTkButton(master=self, text="Save Changes", width=50, height=30, corner_radius=16, fg_color="#e63505",
                             hover_color="#b52a04", border_color="#e63505", border_width=2, image=CTkImage(dark_image=save_img, light_image=save_img), command=self.save_changes)
        self.save_changes_btn.place(relx=0.5, rely=0.85, anchor="sw")




class App(customtkinter.CTk):
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            self.toplevel_window.after(50, self.toplevel_window.lift)
        else:
            self.toplevel_window.focus()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(CenterWindowToDisplay(self, 600, 450, self._get_window_scaling()))
        self.title("FTP Chat | Made with ❤")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.last_chatlog = ""  # Speichert den letzten Zustand des Chatlogs
        self.reading_file = True


        switch_var = customtkinter.StringVar(value="on")
        def mode_event():
            if switch_var.get() == "on":
                set_appearance_mode("dark")
            elif switch_var.get() == "off":
                set_appearance_mode("light")

        switch = CTkSwitch(master=self, text="Dark Mode", variable=switch_var, onvalue="on", offvalue="off", command=mode_event)

        switch.place(relx=0.30, rely=0.027, anchor="nw")

        settings_img = Image.open("icons/settings_icon.png")

        ftp_settings_btn = CTkButton(master=self, text="FTP Settings", width=125, height=30, corner_radius=32, fg_color="#e63505",
                                     hover_color="#b52a04", border_color="#e63505", border_width=2, image=CTkImage(dark_image=settings_img, light_image=settings_img), command=self.open_toplevel)
        ftp_settings_btn.place(relx=0.045, rely=0.02, anchor="nw")

        self.toplevel_window = None

        reader_font = CTkFont(family="Arial", size=13)

        self.reader = CTkTextbox(master=self, corner_radius=16, font=reader_font, height=300, width=550, border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFCC70", state="disabled")
        self.reader.place(relx=0.5, rely=0.45, anchor="center")

        self.send = CTkEntry(master=self, corner_radius=16, height=50, width=550, border_color="#FFCC70", border_width=2)
        self.send.place(relx=0.5, rely=0.9, anchor="center")
        self.send.bind("<Return>", self.send_message)

        thread = threading.Thread(target=self.read_file)
        thread.start()



    def on_closing(self):
        print("Closing..")
        self.destroy()
        self.reading_file = False

    def send_message(self, event):
        try:
            # Laden der Konfiguration mit Fehlerhandling
            try:
                with open("config.json", "r") as json_file:
                    config = json.load(json_file)
            except FileNotFoundError:
                print("Fehler: Die Datei 'config.json' wurde nicht gefunden.")
                return
            except json.JSONDecodeError as e:
                print(f"Fehler beim Lesen der Konfiguration: {e}")
                return

            # Extraktion der Konfigurationsdaten mit Validierung
            try:
                chat_username = config['chat_username']
                chatlog_path = config['chatlog_path']
                ftp_username = config['ftp_username']
                ftp_password = config['ftp_password']
                ftp_server = config['ftp_server']
            except KeyError as e:
                print(f"Fehlender Konfigurationsparameter: {e}")
                return

            # FTP-Verbindung herstellen
            try:
                ftp = FTP(ftp_server, ftp_username, ftp_password)
            except all_errors as e:
                print(f"Fehler beim Verbinden mit dem FTP-Server: {e}")
                return

            try:
                # Datei vom Server abrufen
                r = BytesIO()
                ftp.retrbinary(f'RETR {chatlog_path}', r.write)
                r.seek(0)
                chatlog_content = r.getvalue().decode("utf-8")
            except error_perm as e:
                print(f"Fehler beim Abrufen der Datei: {e}")
                ftp.quit()
                return
            except UnicodeDecodeError as e:
                print(f"Fehler beim Dekodieren der Datei: {e}")
                ftp.quit()
                return

            # Nachricht anhängen
            current_time = datetime.now().strftime("%H:%M:%S")
            stored = f"{chatlog_content}[{current_time}] {chat_username} >> {self.send.get()} \n"

            # Datei auf den Server hochladen
            try:
                ftp.storbinary(f'STOR {chatlog_path}', BytesIO(stored.encode('utf-8')))
            except error_perm as e:
                print(f"Fehler beim Hochladen der Datei: {e}")
            except UnicodeEncodeError as e:
                print(f"Fehler beim Kodieren der Nachricht: {e}")
            finally:
                ftp.quit()

            # Eingabefeld leeren
            self.send.delete(0, 'end')

        except Exception as e:
            # Allgemeines Fehlerhandling
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

    reading_file = True
    def read_file(self):
        with open("config.json", "r") as json_file:
            config1 = json_file.read()
            config2 = json.loads(config1)
            chatlog_path = config2['chatlog_path']
            ftp_username = config2['ftp_username']
            ftp_password = config2['ftp_password']
            ftp_server = config2['ftp_server']

        ftp = FTP(ftp_server, ftp_username, ftp_password)
        try:
            while self.reading_file:
                if ftp.sock is None:  # Verbindung prüfen
                    ftp.connect(ftp_server)
                    ftp.login(ftp_username, ftp_password)

                r = BytesIO()
                try:
                    ftp.retrbinary(f'RETR {chatlog_path}', r.write)
                except Exception as e:
                    print(f"Fehler beim Abrufen der Datei: {e}")
                    continue

                # Chatlog-Daten extrahieren
                chatlog_content = r.getvalue().decode('utf-8')

                # Überprüfen, ob neue Nachrichten vorhanden sind
                if chatlog_content != self.last_chatlog:
                    new_content = chatlog_content[len(self.last_chatlog):]  # Nur neue Nachrichten
                    self.last_chatlog = chatlog_content  # Aktualisiere den gespeicherten Chatlog

                    # Textbox aktualisieren
                    self.reader.configure(state="normal")
                    self.reader.insert('end', new_content)  # Nur neue Inhalte anhängen
                    self.reader.configure(state="disabled")

                    # Nur bei neuen Nachrichten nach unten scrollen
                    self.reader.see("end")

                time.sleep(1)
        finally:
            ftp.quit()



if __name__ == "__main__":
    app = App()
    app.mainloop()