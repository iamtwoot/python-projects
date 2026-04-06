##################### Extra Hard Starting Project ######################
import os
import random
import smtplib
import pandas as pd
import datetime as dt
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

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

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row["email"], msg=f"Subject:Happy Birthday!\n\n{text}")