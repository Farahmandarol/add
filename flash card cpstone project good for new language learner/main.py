from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# -------------- GUI -------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# pick random word
data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")
curren_card = {}


def next_card():
    global curren_card, flip_timer
    window.after_cancel(flip_timer)
    curren_card = random.choice(words)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=curren_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)
    print(curren_card["French"])


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=curren_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)
    print(curren_card["English"])


flip_timer = window.after(3000, func=flip_card)
# label title and word
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=next_card, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)
next_card()
window.mainloop()
