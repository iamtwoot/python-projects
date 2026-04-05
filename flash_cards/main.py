from tkinter import *
from cards import Cards

BACKGROUND_COLOR = "#B1DDC6"
MAIN_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

class FlashcardApp:

    def __init__(self):
        self.cards = Cards()

        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.card_back_img = PhotoImage(file="images/card_back.png")
        self.card_front_img = PhotoImage(file="images/card_front.png")
        self.wrong_img = PhotoImage(file="images/wrong.png")
        self.right_img = PhotoImage(file="images/right.png")

        self.canvas = Canvas(
            width=800,
            height=526,
            highlightthickness=0,
            bg=BACKGROUND_COLOR
        )
        self.bg_image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.card_title = self.canvas.create_text(400, 150, text="", font=MAIN_FONT)
        self.card_word = self.canvas.create_text(400, 263, text="", font=WORD_FONT)

        # Buttons
        wrong_button = Button(image=self.wrong_img, highlightthickness=0,command=self.cards.next_card)
        wrong_button.grid(row=1, column=0)
        wrong_button.config(borderwidth=0)

        right_button = Button(image=self.right_img, highlightthickness=0, command=self.cards.mark_known)
        right_button.grid(row=1, column=1)
        right_button.config(borderwidth=0)

        self.window.mainloop()




