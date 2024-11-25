import customtkinter
from customtkinter import *


app = CTk()
app.geometry("600x400")
app.title("FTP Chat | Made with ❤")

switch_var = customtkinter.StringVar(value="on")
def mode_event():
    if switch_var.get() == "on":
        set_appearance_mode("dark")
    elif switch_var.get() == "off":
        set_appearance_mode("light")

switch = CTkSwitch(master=app, text="Dark Mode", variable=switch_var, onvalue="on", offvalue="off", command=mode_event)

switch.place(relx=0.81, rely=0.01, anchor="nw")

ftp_settings_btn = CTkButton(master=app, text="FTP Settings", width=125, height=30, corner_radius=32, fg_color="#e63505",
                             hover_color="#b52a04", border_color="#e63505", border_width=2)
ftp_settings_btn.place(relx=0.01, rely=0.01, anchor="nw")





app.mainloop()