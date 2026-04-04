from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    if password_entry:
        password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Error",
            message="Please don`t leave any fields empty!",
        )

    else:
        with open ("data.txt", "a") as data_file:
            new_entry = f"{website} | {email} | {password}\n"
            data_file.write(new_entry)

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(130, 100, image=img)
canvas.grid(row=0, column=1)

# Row 1
website_label = Label(text="Website")
website_label.grid(row=1, column=0, sticky="W")

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

# Row 2
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0, sticky="W")

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "example@mail.com")

# Row 3
password_label = Label(text="Password")
password_label.grid(row=3, column=0, sticky="W")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="ew")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

# Row 4
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()