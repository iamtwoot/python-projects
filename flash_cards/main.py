import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
MAIN_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# -------------------------- GENERATE WORDS --------------------------- #
data = pd.read_csv("data/russian_words.csv")
to_learn = data.to_dict("records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(bg_image, image=card_front_img)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["Eng"], fill="black")
    flip_timer = window.after(3000, flip_card)


# -------------------------- FLIP CARDS ------------------------------- #
def flip_card():
    canvas.itemconfig(bg_image, image=card_back_img)
    canvas.itemconfig(card_title, text="Русский", fill="white")
    canvas.itemconfig(card_word, text=current_card["Ru"], fill="white")


# -------------------------- SETUP UI --------------------------------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

flip_timer = window.after(3000, flip_card)

# Images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

# Card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=MAIN_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
wrong_button.config(borderwidth=0)

right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
right_button.config(borderwidth=0)

next_card()

window.mainloop()


