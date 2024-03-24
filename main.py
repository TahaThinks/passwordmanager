from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Not Valid", message="One or More Fields are empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Email: {email}\n"
                                                              f" Password: {password}\n Is it ok to Save?")
        if is_ok:
            try:
                with open("taha_passwords.json", 'r') as file:
                    # Read Old Data
                    data = json.load(file)
                    # Updating Old Data with new Data
                    data.update(new_data)

            except FileNotFoundError:
                with open("taha_passwords.json", "w") as file:
                    # Saving new Data
                    json.dump(new_data, file, indent=4)
            else:
                with open("taha_passwords.json", "w") as file:
                    # Saving updated Data
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSOWRD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("taha_passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(titel="Error", message="Not Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")


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
website_entry = Entry(width=23)
website_entry.focus()
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1)
# Search Button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
# Email/Username Entry [2 Labels]
email_label = Label(text="Email/Username:")
email_entry = Entry(width=42)
email_entry.insert(0, "tahalearns@email.com")
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)
# Password Entry [3 Labels]
password_text = Label(text="Password:")
password_entry = Entry(width=23)
password_generate_button = Button(text="Generate Password", command=generate_password)
password_text.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
password_generate_button.grid(row=3, column=2)
# Add Button [1 Label]
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
