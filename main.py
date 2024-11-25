import customtkinter
from customtkinter import *
from PIL import Image


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.resizable(False, False)
        self.label = customtkinter.CTkLabel(self, text="FTP Username", anchor="nw")
        self.label.place(rely=0.05, relx=0.05)


class App(customtkinter.CTk):
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x450")
        self.title("FTP Chat | Made with ❤")
        self.resizable(False, False)

        switch_var = customtkinter.StringVar(value="on")
        def mode_event():
            if switch_var.get() == "on":
                set_appearance_mode("dark")
            elif switch_var.get() == "off":
                set_appearance_mode("light")

        switch = CTkSwitch(master=self, text="Dark Mode", variable=switch_var, onvalue="on", offvalue="off", command=mode_event)

        switch.place(relx=0.81, rely=0.01, anchor="nw")

        settings_img = Image.open("settings_icon.png")

        ftp_settings_btn = CTkButton(master=self, text="FTP Settings", width=125, height=30, corner_radius=32, fg_color="#e63505",
                                     hover_color="#b52a04", border_color="#e63505", border_width=2, image=CTkImage(dark_image=settings_img, light_image=settings_img), command=self.open_toplevel)
        ftp_settings_btn.place(relx=0.01, rely=0.01, anchor="nw")

        self.toplevel_window = None

        reader = CTkTextbox(master=self, corner_radius=16, height=300, width=550, border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFCC70", state="disabled")
        reader.place(relx=0.5, rely=0.45, anchor="center")

        send = CTkTextbox(master=self, corner_radius=16, height=50, width=400, border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFCC70")
        send.place(relx=0.375, rely=0.9, anchor="center")

        send_img = Image.open("send_icon.png")

        send_btn = CTkButton(master=self, text="Send Message", width=50, height=30, corner_radius=16, fg_color="#e63505",
                             hover_color="#b52a04", border_color="#e63505", border_width=2, image=CTkImage(dark_image=send_img, light_image=send_img))
        send_btn.place(relx=0.73, rely=0.93, anchor="sw")



if __name__ == "__main__":
    app = App()
    app.mainloop()