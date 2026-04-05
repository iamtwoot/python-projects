import random
import pandas as pd

class Cards:

    def __init__(self):
        try:
            data = pd.read_csv("data/to_learn.csv")
        except FileNotFoundError:
            data = pd.read_csv("data/russian_words.csv")

        self.to_learn = data.to_dict("records")
        self.current_card = None


    def next_card(self):
        self.current_card = random.choice(self.to_learn)
        return self.current_card


    def mark_known(self):
        self.to_learn.remove(self.current_card)
        pd.DataFrame(self.to_learn).to_csv("data/to_learn.csv", index=False)
