from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website == "" or password == "" or email == "":
        messagebox.showwarning(title="Not Valid", message="One or More Fields are empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Email: {email}\n Password: {password}\n Is it ok to Save?")

        if is_ok:
            with open("taha_passwords.txt",'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager by TahaLearns")
window.config(padx=50, pady=50)
password_image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=0, columnspan=3)

# Website Entry [2 Labels]
website_label = Label(text="Website:")
website_entry = Entry(width=42)
website_entry.focus()
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=2)
# Email/Username Entry [2 Labels]
email_label = Label(text="Email/Username:")
email_entry = Entry(width=42)
email_entry.insert(0,"tahalearns@email.com")
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)
# Password Entry [3 Labels]
password_text = Label(text="Password:")
password_entry = Entry(width=23)
password_generate_button = Button(text="Generate Password")
password_text.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
password_generate_button.grid(row=3, column=2)
# Add Button [1 Label]
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()