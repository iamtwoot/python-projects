from tkinter import *
from tkinter import messagebox
from cards import Cards

BACKGROUND_COLOR = "#B1DDC6"
MAIN_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

class FlashcardApp:

    def __init__(self):
        self.cards = Cards()
        self.flip_timer = None

        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.card_back_img = PhotoImage(file="images/card_back.png")
        self.card_front_img = PhotoImage(file="images/card_front.png")
        self.wrong_img = PhotoImage(file="images/wrong.png")
        self.right_img = PhotoImage(file="images/right.png")

        self.canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.bg_image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.card_title = self.canvas.create_text(400, 150, text="", font=MAIN_FONT)
        self.card_word = self.canvas.create_text(400, 263, text="", font=WORD_FONT)

        wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.next_card)
        wrong_button.grid(row=1, column=0)
        wrong_button.config(borderwidth=0)

        right_button = Button(image=self.right_img, highlightthickness=0, command=self.mark_known)
        right_button.grid(row=1, column=1)
        right_button.config(borderwidth=0)

        self.window.protocol("WM_DELETE_WINDOW", self.save_files)
        self.show_card()
        self.window.mainloop()


    def save_files(self):
        if messagebox.askokcancel(title="Goodbye", message="Update dictionary based on this session?"):
            self.cards.save_files()
            self.window.destroy()


    def next_card(self):
        self.cards.next_card()
        self.show_card()


    def mark_known(self):
        self.cards.mark_known()
        self.cards.next_card()
        self.show_card()


    def show_card(self):
        if self.flip_timer:
            self.window.after_cancel(self.flip_timer)

        self.canvas.itemconfig(self.bg_image, image=self.card_front_img)
        self.canvas.itemconfig(self.card_title, text="English")
        self.canvas.itemconfig(self.card_word, text=self.cards.current_card["Eng"])
        self.flip_timer = self.window.after(3000, self.flip_card)


    def flip_card(self):
        self.canvas.itemconfig(self.bg_image, image=self.card_back_img)
        self.canvas.itemconfig(self.card_title, text="Русский")
        self.canvas.itemconfig(self.card_word, text=self.cards.current_card["Ru"])


flash_app = FlashcardApp()




