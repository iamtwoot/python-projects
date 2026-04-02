from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

# Row 2
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

# Row 3
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="ew")

password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)

# Row 4
add_button = Button(text="Add")
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()