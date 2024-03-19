import tkinter
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager by TahaLearns")
window.config(padx=20, pady=20)
password_image = PhotoImage(file="password.png")

canvas = Canvas(width=300, height=240, highlightthickness=0)
canvas.create_image(150, 150, image=password_image)
canvas.grid(row=0, column=1)

# Website Entry [2 Labels]
website_text = Label(text="Website:")
website_input = Entry(width=35)
website_text.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2)
# Email/Username Entry [2 Labels]
email_text = Label(text="Email/Username:")
email_input = Entry(width=35)
email_text.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2)
# Password Entry [3 Labels]
password_text = Label(text="Password:")
password_input = Entry(width=21)
password_generate_button = Button(text="Generate Password")
password_text.grid(row=3, column=0)
password_input.grid(row=3, column=1)
password_generate_button.grid(row=3, column=2)
# Add Button [1 Label]


window.mainloop()