import random
from tkinter import *
from tkinter import messagebox
import time

# --------------------- Functions ---------------#
demos = [
    "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less "

    "Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy.",
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer.",
    "The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorumby Cicero are also."]

text = ""
ok_run = False
char = 0
sec = 0
second = 0


# ------------------------ functions -------------------------#
def timer():
    global sec, second
    sec += 1
    second = int(sec / 1000)


def create_text():
    global text
    demo.config(state=NORMAL)
    demo.delete("1.0", "end")
    screenText.config(state=NORMAL)
    screenText.delete("1.0", "end")
    text = random.choice(demos)
    demo.insert(END, text)
    demo.config(state=DISABLED)


def match():
    global char
    typed_text = screenText.get("1.0", 'end-1c')
    for i in range(len(typed_text)):
        demo.tag_add("forward", f"1.{i + 1}", f"1.{i + 2}")
        demo.tag_config("forward", background="blue", font=("Arial", 19, "normal"))
        if len(typed_text) <= len(text):
            if typed_text[i] == text[i]:
                char += 1
                speedLabel.config(text=f"speed: {char} character in {second} second")
                demo.tag_add("accurate", f"1.{i}", f"1.{i + 1}")
                demo.tag_config("accurate", background="orange", foreground="black", font=("Arial", 16, "underline"))
            elif typed_text[i] != text[i]:
                demo.tag_add("wrong", f"1.{i}", f"1.{i + 1}")
                demo.tag_config("wrong", background="red", foreground="black", font=("Arial", 16, "underline"))
        elif len(typed_text) > len(text):
            screenText.config(state=DISABLED)
            # messagebox.showerror(title="Error", message="You override the specified text")


# ---------------------- UI ---------------------#
window = Tk()
window.config(pady=20, padx=20, bg="#176B87")
title = Label(text="MASTER TYPING", bg="#176B87", fg="white", font=("Arial", 30, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=15)
canvas = Canvas(width=400, height=200, bg="white")
demo = Text(canvas, height=10, width=48, highlightthickness=0, font=("Montserrat", 16, "normal"))

demo.insert(END, "Demo text\nPress the 👇'Create Text' button to creat a text")
demo.config(state=DISABLED)
demo.grid(row=1, column=0, columnspan=2, pady=12, padx=12)

canvas.grid(row=1, column=0, columnspan=2)
screenText = Text(window)
createText = Button(text="Create Text", command=create_text, bg="#213363", fg="white", font=("Arial", 12, "bold"))
createText.grid(row=2, column=0, columnspan=2, pady=20)
Label(window, text="Type below to test your SPEED", bg="#176B87", fg="white", font=("Arial", 15)).grid(column=0, row=3,
                                                                                                       padx=10,
                                                                                                       columnspan=2)

# Text Widget
screenText = Text(window, width=50, height=6, font=("Montserrat", 16, "normal"))
screenText.focus()
screenText.grid(column=0, row=4, columnspan=2)
# ------------------typing area -------------------#

speedLabel = Label(text="Your speed per minute!", fg="white", bg="#176B87", font=("Arial", 14, "bold"))
speedLabel.grid(row=5, column=0, columnspan=2)


def my_mainloop():
    match()
    window.after(1, my_mainloop)  # run again after 1000ms (1s)


window.after(1, my_mainloop)  # run first time after 1000ms (1s)

window.mainloop()
