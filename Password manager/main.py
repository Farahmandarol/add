import random
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = random.randint(1000000, 10000000)
    passwordInfo.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = websiteName.get()
    email = emailInfo.get()
    password = passwordInfo.get()
    if len(website) < 4:
        messagebox.showwarning(title="Warning", message="Please Enter a valid Website name")
    elif len(email) < 8:
        messagebox.showwarning(title="Warning", message="Please Enter a valid Email Address ")
    elif len(password) < 4:
        messagebox.showwarning(title="Warning", message="Please Enter a valid Password at least 4 character")
    else:
        is_ok = messagebox.askokcancel(title="Save To Database",
                                       message=f"website:{website}\nEmail:{email}\nPassword:{password}")
        if is_ok:
            with open("info.text", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                websiteName.delete(0, END)
                passwordInfo.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=20, padx=20)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
website = Label(text="Website:")
website.grid(row=1, column=0)
websiteName = Entry(width=38)
websiteName.focus()
websiteName.grid(row=1, column=1, columnspan=2)
email = Label(text="Email/Username")
email.grid(row=2, column=0)
emailInfo = Entry(width=38)
emailInfo.insert(0, "farahmandarol@gmail.com")
emailInfo.grid(row=2, column=1, columnspan=2)
password = Label(text="Password:")
password.grid(row=3, column=0)
passwordInfo = Entry(width=20)
passwordInfo.grid(row=3, column=1)
generator_btn = Button(text="Generate Password", command=generate_password)
generator_btn.grid(row=3, column=2)
add = Button(text="Add", width=32, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
