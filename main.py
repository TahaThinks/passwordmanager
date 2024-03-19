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
# Password Entry [3 Labels]
# Add Button [1 Label]

window.mainloop()