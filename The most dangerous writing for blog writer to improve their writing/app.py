import time
from tkinter import *

char = ""


# -------------------- Function to control The APP -----------------#
def get_text():
    global char, seconds
    typed_text = text_area.get("1.0", 'end-1c')
    if len(typed_text) > len(char):
        seconds = 0
        char = typed_text
    detect_is_type()


seconds = 0
full_time = 10


def detect_is_type():
    global seconds, char
    seconds += 1
    time_label.config(text=f"Second:{full_time - int(seconds / 700)} ", fg="black")
    if int(seconds / 700) > 4:
        time_label.config(text=f"Second:{full_time - int(seconds / 700)} To delete all screen text", fg="#EB455F")
    if int(seconds / 700) > 6:
        time_label.config(text=f"Second: {full_time - int(seconds / 700)} To delete all screen text", fg="red")

    if seconds > full_time * 700:
        text_area.delete("1.0", "end")
        # title.config(text=f"Lost 🤣",font=("Arial",20,"bold"))
        seconds = 0
        char = ''


# -------------------------------- UI ------------------------------#
window = Tk()
window.config(width=600, height=500, pady=30, padx=30)
window.title("The most dangerous writing!")
title = Label(text="The most Dangerous writing app for blog writer!\nWrite as fast as possible!💪",
              font=("Arial", 16, "bold"))
title.grid(row=0, column=0, padx=15)
time_label = Label(text="Second", font=("Arial", 14, "bold"))
time_label.grid(row=1, column=0, pady=20)
text_area = Text(window, width=60, height=20, font=("Arial", 12, "bold"), foreground="orangered", bg="light blue")
text_area.focus()
text_area.grid(row=2, column=0)


def my_mainloop():
    time.sleep(0.00001)
    get_text()
    window.after(1, my_mainloop)  # run again after 1000ms (1s)


window.after(1, my_mainloop)  # run first time after 1000ms (1s)
window.wm_attributes("-transparentcolor", "white")
window.mainloop()
