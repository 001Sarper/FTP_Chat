import customtkinter
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("600x450")
app.title("FTP Chat | Made with ❤")
app.resizable(False, False)

switch_var = customtkinter.StringVar(value="on")
def mode_event():
    if switch_var.get() == "on":
        set_appearance_mode("dark")
    elif switch_var.get() == "off":
        set_appearance_mode("light")

switch = CTkSwitch(master=app, text="Dark Mode", variable=switch_var, onvalue="on", offvalue="off", command=mode_event)

switch.place(relx=0.81, rely=0.01, anchor="nw")

settings_img = Image.open("settings_icon.png")

ftp_settings_btn = CTkButton(master=app, text="FTP Settings", width=125, height=30, corner_radius=32, fg_color="#e63505",
                             hover_color="#b52a04", border_color="#e63505", border_width=2, image=CTkImage(dark_image=settings_img, light_image=settings_img))
ftp_settings_btn.place(relx=0.01, rely=0.01, anchor="nw")

reader = CTkTextbox(master=app, corner_radius=16, height=300, width=550, border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFCC70", state="disabled")
reader.place(relx=0.5, rely=0.45, anchor="center")

send = CTkTextbox(master=app, corner_radius=16, height=50, width=400, border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFCC70")
send.place(relx=0.375, rely=0.9, anchor="center")

send_img = Image.open("send_icon.png")

send_btn = CTkButton(master=app, text="Send Message", width=50, height=30, corner_radius=16, fg_color="#e63505",
                     hover_color="#b52a04", border_color="#e63505", border_width=2, image=CTkImage(dark_image=send_img, light_image=send_img))
send_btn.place(relx=0.73, rely=0.93, anchor="sw")



app.mainloop()