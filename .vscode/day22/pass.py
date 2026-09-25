from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_list = (
        random.choices(letters, k=8)
        + random.choices(numbers, k=2)
        + random.choices(symbols, k=2)
    )

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(
            title="Oops",
            message="Please don't leave any fields empty!"
        )
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\n\n"
                f"Email: {email}\n"
                f"Password: {password}\n\n"
                f"Is it okay to save?"
    )

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(
                f"{website} | {email} | {password}\n"
            )

        website_entry.delete(0, END)
        password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "your@email.com")

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Generate Password Button
generate_button = Button(
    text="Generate Password",
    command=generate_password
)
generate_button.grid(row=3, column=2)

# Add Button
add_button = Button(
    text="Add",
    width=36,
    command=save
)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()