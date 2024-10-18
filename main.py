from tkinter import *
from tkinter import messagebox
from random import *
from pyperclip import *
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [(choice(letters)) for char in range(randint(8, 10))]

    password_symbols = [(choice(symbols)) for char in range(randint(2, 4))]

    password_numbers = [(choice(numbers)) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_box.insert(0, password)

    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_box.get()
    email = email_box.get()
    password = password_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops!", message="Please make sure you haven't left any fields empty."
        )
    else:
        is_okay = messagebox.askokcancel(
            title=email,
            message=f"These are the details entered:\nWebsite: {website}\nPassword:{password}\nIs is okay to save?",
        )
        if is_okay:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_box.delete(0, END)
                password_box.delete(0, END)


# ---------------------------- search ----------------------P--------- #
def find_password():
    website = website_box.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="This data does not exit.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Error", message=f"There are no details of {website}"
            )


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.minsize(400, 400)
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels:

website = Label(text="Website:", font=("ariel", 12), padx=5, pady=5)
website.grid(column=0, row=1, sticky="E")

email_username = Label(text="Email/UserName:", font=("ariel", 12), padx=5, pady=5)
email_username.grid(column=0, row=2)

password = Label(text="Password:", font=("ariel", 12), padx=5, pady=5)
password.grid(column=0, row=3, sticky="E")

# Entries:

website_box = Entry(width=21)
website_box.grid(column=1, row=1, sticky="W", padx=5, pady=5)
website_box.focus()


email_box = Entry(width=35)
email_box.insert(0, "example@gmail.com")
email_box.grid(column=1, row=2, columnspan=2, sticky="W", padx=5, pady=5)

password_box = Entry(width=21)
password_box.grid(column=1, row=3, columnspan=2, sticky="W", padx=5, pady=5)

# Buttons:

search = Button(text="Search", width=14, command=find_password)
search.grid(column=2, row=1, sticky="W", padx=5, pady=5)

generate_password = Button(
    text="Generate Password", width=14, padx=5, pady=5, command=create_password
)
generate_password.grid(column=2, row=3, sticky="W", padx=5)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="W", padx=5, pady=5)


screen.mainloop()
