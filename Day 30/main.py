# Day 30 of Udemy's 100 Days of Python programming course
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
FONT_NAME = "Helvetica"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """Generates a password consisting of random letters, symbols and numbers."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
# Insert the generated password into the password entry field.
    password_entry.insert(0, password)
# Copy the password to the clipboard.
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """Saves users inputs to a text file."""
# Takes the inputs from the entry fields.
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

# If the website or password fields have nothing in them, display a warning to the user.
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Error!", message = "You have left an area blank!")
    else:
        # Attempt to open the data file and read in the data.
        try:
            with open("data.json", "r") as data_file:
                # Read in the JSON file data.
                data = json.load(data_file)
        # If the file does not exist, create it and write the data to the newly created file.
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent = 4)
        # If the file does exist, update the data with the new data, and write said data to the file.
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Save updated data to JSON file.
                json.dump(data, data_file, indent = 4)
        # Regardless of success or failure, clear the website and password entry fields.
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    """Searches a file for a password entry and displays it to the user if it exists."""
    # Retrieve the website name from the entry field.
    website = website_entry.get()
    # If the website entry field is blank, display an error box to the user.
    if len(website) == 0:
        messagebox.showinfo(title = "Error!", message = "The website field is blank!")
    else:
        try:
            # Attempt to open the file and read in the data.
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        # If the file does not exist, display an error box to the user.
        except FileNotFoundError:
            messagebox.showinfo(title = "Error!", message = "A password file does not exist!\nPlease create a password before searching.")
        # If the file does exist
        else:
            # and the website is in the data file, retrieve the email and password and 
            # then display it to the user with an info box.
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title = website, message = f"Email: {email}\n\nPassword: {password}")
            # and the website does not exist, display an errox box to the user stating 
            # that there is not entry for the website entered.
            else:
                messagebox.showinfo(title = "Error!", message = "No entry for this website exists!")
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)

canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
logo_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_image)
canvas.grid(row = 0, column = 1)

website_label = Label(text = "Website:", font = (FONT_NAME))
website_label.grid(row = 1, column = 0)

website_entry = Entry(width = 20)
website_entry.grid(row = 1, column = 1)
website_entry.focus()

search_button = Button(text = "Search", font = (FONT_NAME), relief = "groove", width = 16, command = find_password)
search_button.grid(row = 1, column = 2)

email_username_label = Label(text = "Email/Username:", font = (FONT_NAME))
email_username_label.grid(row = 2, column = 0)

email_username_entry = Entry(width = 45)
email_username_entry.grid(row = 2, column = 1, columnspan = 2)
email_username_entry.insert(0, "youremailhere@gmail.com")

password_label = Label(text = "Password:", font = (FONT_NAME))
password_label.grid(row = 3, column = 0)

password_entry = Entry(width = 20)
password_entry.grid(row = 3, column = 1)

generate_password_button = Button(text = "Generate Password", font = (FONT_NAME), relief = "groove", command = generate_password)
generate_password_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", width = 38, relief = "groove", command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)


window.mainloop()