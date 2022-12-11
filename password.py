#***************************************************************************************************************
#
# File: password.py
#
# Version: 1.0
#
# Remarks:  This file creates a password manager with UI
#****************************************************************************************************************

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

#CONSTS
MAINFONTSMALL = ("Arial", 12, "bold")
MAINFONTBIG = ("Arial", 16, "bold")

# Create random Password
def create_password():
  pass_entry.delete(0,END)

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8,8))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers

  # Shuffling
  shuffle(password_list)

  # Joins chars in a list without spaces 
  password = "".join(password_list)
  # Change window text to show the new password.
  pass_entry.insert(0,password)

# Store password data to a json file
def save_data():
  website = website_entry.get().upper() # Needed due to case sensitivity
  # Get text inputed
  email = email_entry.get()
  password = pass_entry.get()

  # Holds dat from form to be written to file
  dictionary = {
    website:{
      "email": email,
      "password": password
    }
  }

  # Makes sure inpu entries contains some type of text
  if(website_entry.get() == "") or (email_entry.get() == "") or (pass_entry.get() == ""):
    messagebox.showerror(title="No data", message="Oops you left something blank")
  else:
    # See if file exists
    try:
      with open("pass.json", "r") as f:
        data = json.load(f)
    except FileNotFoundError:
      with open("pass.json","w") as f:
        json.dump(dictionary, f, indent=4)
    else:
      data.update(dictionary)

      with open("pass.json", "w") as f:
        json.dump(data, f, indent=4)     
    finally:
      website_entry.delete(0,END)
      pass_entry.delete(0, END)

# Load password data from json file
def load_data():
  website = website_entry.get().upper() # For case sensitivity
  # Make sure file exists
  try:
    with open("pass.json", "r") as f:
      data = json.load(f)
  except FileNotFoundError:
    messagebox.showinfo(title="ERROR!!", message=" File: pass.json does not exist.")
  else:
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]
      website_entry.delete(0,END)
      email_entry.delete(0,END)
      pass_entry.delete(0,END)
      website_entry.insert(0,website)
      email_entry.insert(0,email)
      pass_entry.insert(0,password)
    else:
      messagebox.showinfo(title="Web site not found",message="The website you have entered was never saved.")

# Clears text on UI..This includes login information
def clear_text():
  website_entry.delete(0,END)
  email_entry.delete(0,END)
  pass_entry.delete(0,END)


# Windows User Interface
root = Tk()
root.title("Password Saver")
root.geometry("590x400")
#Labels
main_lbl = Label(text="Website Login and Password", font=(MAINFONTBIG))
main_lbl.grid(row=0, column=1)
website_name_lbl = Label(text="Website Name:", font=(MAINFONTSMALL))
website_name_lbl.config(pady=20)
website_name_lbl.grid(row=1, column=0)
website_logon_email_lbl = Label(text="Logon or Email:", font=(MAINFONTSMALL))
website_logon_email_lbl.config(pady=20)
website_logon_email_lbl.grid(row=2, column=0)
website_password_lbl = Label(text="Website Password:", font=(MAINFONTSMALL))
website_password_lbl.config(pady=20)
website_password_lbl.grid(row=3, column=0)
#User Input
website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = Entry(width=30)
email_entry.insert(0, "someone@gmail.com")
email_entry.grid(row=2, column=1)
pass_entry = Entry(width=30)
pass_entry.grid(row=3, column=1)
#Buttons
btn_generate_pass = Button(text="Generate New Password.", command=create_password)
btn_generate_pass.grid(row=4, column=0, padx=20)
btn_save_pass = Button(text="Save Record.", command=save_data)
btn_save_pass.grid(row=4, column=1, padx=10)
btn_load_pass = Button(text="Load Record.", command=load_data)
btn_load_pass.grid(row=4, column=2)
btn_clear = Button(text="Clear All Text", command=clear_text)
btn_clear.grid(row=5, column=1, pady=40)


root.mainloop()

