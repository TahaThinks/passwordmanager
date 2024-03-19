import tkinter
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager by TahaLearns")
window.config(padx=20, pady=20)
password_image = PhotoImage(file="password.png")

canvas = Canvas(width=300, height=300, highlightthickness=0)
canvas.create_image(150, 150, image=password_image)
canvas.pack()

# Website Entry [2 Labels]
# Email/Username Entry [2 Labels]
# Password Entry [3 Labels]
# Add Button [1 Label]

window.mainloop()