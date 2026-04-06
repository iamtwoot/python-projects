##################### Extra Hard Starting Project ######################
import os
import random
import pandas as pd
import datetime as dt



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
birthdays = pd.read_csv("birthdays.csv")

for index, row in birthdays.iterrows():
    bd_date = dt.datetime(
        year=row["year"],
        month=row["month"],
        day=row["day"],
    )

    current_date = dt.datetime.today()

    if bd_date.day  == current_date.day and bd_date.month == current_date.month:

        letters = os.listdir("letter_templates/")
        random_letter = random.choice(letters)

        with open(f"letter_templates/{random_letter}") as letter_file:
            text = letter_file.read()
            text = text.replace("[NAME]", row["name"])

        # with open(f"letter_templates/{random_letter}", "w") as letter_file:
        #     letter_file.write(text)



