from tkinter import *
from tkinter import ttk

capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "`", "~", ";", ":", ",", "<", ".", ">",
           "/", "?", "'", "", "[", "]", "{", "}", "|"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def split(word):
    return [char for char in word]

def checkPass():
    has_symbol = False
    has_number = False
    has_capital = False
    is_long = False
    is_medium = False
    is_short = False
    pass_text = password.get()
    pass_split = split(pass_text)
    for letter in pass_split:
        if letter in symbols:
            has_symbol = True
        elif letter in numbers:
            has_number = True
        elif letter in capitals:
            has_capital = True
    if len(pass_text) >= 12:
        is_long = True
    elif len(pass_text) >= 8:
        is_medium = True
    elif len(pass_text) >= 4:
        is_short = True

    if is_long and has_number and has_symbol and has_capital:
        password_indicator["text"] = "Your Password is strong!"
    elif is_long and has_number and has_symbol and has_capital == False:
        password_indicator["text"] = "Your Password is good, but it could use a capital letter."
    elif is_long and has_number and has_symbol == False and has_capital:
        password_indicator["text"] = "Your Password is good, but it could use a symbol."
    elif is_long and has_number == False and has_symbol and has_capital:
        password_indicator["text"] = "Your Password is good, but it could use a number."
    elif is_long == False:
        password_indicator["text"] = "Your Password needs to be longer."
    else:
        password_indicator["text"] = "Your Password is not strong."

window = Tk()
window.title("Password Checker")

mainframe = ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

password = StringVar()
password_entry = ttk.Entry(mainframe, width=10, textvariable=password)
password_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Check", command=checkPass).grid(column=2, row=2, sticky=W)

password_indicator = ttk.Label(mainframe, text="Your Password Strength")
password_indicator.grid(column=3, row=1, sticky=W)

window.mainloop()
