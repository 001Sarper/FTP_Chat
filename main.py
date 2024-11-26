import customtkinter
from customtkinter import *
from PIL import Image


def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(CenterWindowToDisplay(self, 500, 450, self._get_window_scaling()))
        self.resizable(False, False)
        self.title("FTP Settings")

        self.title1 = CTkLabel(self, text="FTP Settings", anchor="n", font=CTkFont(size=14))
        self.title1.place(rely=0.02, relx=0.41)

        self.chat_username_label = customtkinter.CTkLabel(self, text="Chat Username", anchor="nw")
        self.chat_username_label.place(rely=0.10, relx=0.05)

        self.chat_username = CTkTextbox(master=self, corner_radius=8, height=25, width=450,  border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFCC70")
        self.chat_username.place(relx=0.05, rely=0.14)

        self.chatlog_path_label = customtkinter.CTkLabel(self, text="Chatlog Path", anchor="nw")
        self.chatlog_path_label.place(rely=0.26, relx=0.05)

        self.chatlog_path = CTkTextbox(master=self, corner_radius=8, height=25, width=450, border_color="#FFCC70",
                                        border_width=2, scrollbar_button_color="#FFCC70")
        self.chatlog_path.place(relx=0.05, rely=0.30)

        self.ftp_username_label = customtkinter.CTkLabel(self, text="FTP Username", anchor="nw")
        self.ftp_username_label.place(rely=0.42, relx=0.05)

        self.ftp_username = CTkTextbox(master=self, corner_radius=8, height=25, width=450, border_color="#FFCC70",
                                        border_width=2, scrollbar_button_color="#FFCC70")
        self.ftp_username.place(relx=0.05, rely=0.46)

        self.ftp_password_label = customtkinter.CTkLabel(self, text="FTP Password", anchor="nw")
        self.ftp_password_label.place(rely=0.58, relx=0.05)

        self.ftp_password = CTkTextbox(master=self, corner_radius=8, height=25, width=450, border_color="#FFCC70",
                                       border_width=2, scrollbar_button_color="#FFCC70")
        self.ftp_password.place(relx=0.05, rely=0.62)

        self.ftp_port_label = customtkinter.CTkLabel(self, text="FTP Server IP", anchor="nw")
        self.ftp_port_label.place(rely=0.74, relx=0.05)

        self.ftp_server = CTkTextbox(master=self, corner_radius=8, height=25, width=150, border_color="#FFCC70",
                                       border_width=2, scrollbar_button_color="#FFCC70")
        self.ftp_server.place(relx=0.05, rely=0.78)

        save_img = Image.open("icons/save_icon.png")

        self.save_changes_btn = CTkButton(master=self, text="Save Changes", width=50, height=30, corner_radius=16, fg_color="#e63505",
                             hover_color="#b52a04", border_color="#e63505", border_width=2, image=CTkImage(dark_image=save_img, light_image=save_img))
        self.save_changes_btn.place(relx=0.5, rely=0.85, anchor="sw")


    def save_changes_btn(self):


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

        reader = CTkTextbox(master=self, corner_radius=16, height=300, width=550, border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFCC70", state="disabled")
        reader.place(relx=0.5, rely=0.45, anchor="center")

        send = CTkTextbox(master=self, corner_radius=16, height=50, width=400, border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFCC70")
        send.place(relx=0.375, rely=0.9, anchor="center")

        send_img = Image.open("icons/send_icon.png")

        send_btn = CTkButton(master=self, text="Send Message", width=50, height=30, corner_radius=16, fg_color="#e63505",
                             hover_color="#b52a04", border_color="#e63505", border_width=2, image=CTkImage(dark_image=send_img, light_image=send_img))
        send_btn.place(relx=0.73, rely=0.93, anchor="sw")



if __name__ == "__main__":
    app = App()
    app.mainloop()