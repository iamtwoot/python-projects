from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
MAIN_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


# -------------------------- SETUP UI --------------------------------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

# Images
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

# Card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_text(400, 150, text="language", font=MAIN_FONT)
canvas.create_text(400, 263, text="word", font=WORD_FONT)

# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)
wrong_button.config(borderwidth=0)

right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)
right_button.config(borderwidth=0)


window.mainloop()


