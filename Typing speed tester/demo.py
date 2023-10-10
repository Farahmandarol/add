import tkinter as tk

window = tk.Tk()
window.title("Face Recognition System")

# Label and text field
l1 = tk.Label(window, text="Name: ", font=("Arial", 15))
l1.place(x=0, y=0)
t1 = tk.Entry(window, bd=5, width=20)
t1.place(x=180, y=0)

l2 = tk.Label(window, text="Age: ", font=("Arial", 15))
l2.place(x=0, y=60)
t2 = tk.Entry(window, bd=5, width=20, show='*')
t2.place(x=180, y=60)

l3 = tk.Label(window, text="Address: ", font=("Arial", 15))
l3.place(x=0, y=120)
t3 = tk.Entry(window, bd=5, width=20, show='*')
t3.place(x=180, y=120)

# Combobox (drop down menu)
l4 = tk.Label(window, text="Drop down menu: ", font=("Arial", 15))
l4.place(x=0, y=180)

from tkinter.ttk import *

c1 = Combobox(window)
c1['values'] = ("Nepal", "India", "Pakistan", "USA", "Bangladesh", "Australia")
c1.current(0)
c1.place(x=180, y=180)

# Check button
from tkinter import *

l5 = tk.Label(window, text="Languages: ", font=("Arial", 15))
l5.place(x=0, y=240)
var1 = IntVar()
cb1 = Checkbutton(window, text="C", font=('Arial', 10), var=var1)
cb1.place(x=180, y=240)
var2 = IntVar()
cb2 = Checkbutton(window, text="C++", font=('Arial', 10), var=var2)
cb2.place(x=280, y=240)
var3 = IntVar()
cb3 = Checkbutton(window, text="Python", font=('Arial', 10), var=var3)
cb3.place(x=180, y=280)
var4 = IntVar()
cb4 = Checkbutton(window, text="Java", font=('Arial', 10), var=var4)
cb4.place(x=280, y=280)

# Radio button
l6 = tk.Label(window, text="Sex: ", font=("Arial", 15))
l6.place(x=0, y=320)
var = IntVar()
r1 = tk.Radiobutton(window, text='Male', var=var, value=1)
r1.place(x=180, y=320)
r2 = tk.Radiobutton(window, text='Female', var=var, value=2)
r2.place(x=260, y=320)
r3 = tk.Radiobutton(window, text='Other', var=var, value=3)
r3.place(x=340, y=320)

# Scrolled text
l7 = tk.Label(window, text="Comment: ", font=("Arial", 15))
l7.place(x=0, y=380)
from tkinter import scrolledtext

txt = scrolledtext.ScrolledText(window, width=20, height=1)
txt.place(x=180, y=380)
txt.insert(tk.INSERT, 'write some comment')

# Spinbox
l8 = tk.Label(window, text="Number: ", font=("Arial", 15))
l8.place(x=0, y=440)
spin = tk.Spinbox(window, from_=0, to=10, width=5)
spin.place(x=180, y=440)

# Button
b1 = tk.Button(window, text="Submit ", font=("Arial", 10))
b1.place(x=140, y=480)

window.geometry("400x550")
window.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk  # install pillow with pip: pip install pillow
#
#
# class FirstPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#
#         load = Image.open("img1.jpg")
#         photo = ImageTk.PhotoImage(load)
#         label = tk.Label(self, image=photo)
#         label.image = photo
#         label.place(x=0, y=0)
#
#         border = tk.LabelFrame(
#             self, text='Login', bg='ivory', bd=10, font=("Arial", 20))
#         border.pack(fill="both", expand="yes", padx=150, pady=150)
#
#         Label1 = tk.Label(border, text="Username",
#                           font=("Arial Bold", 15), bg='ivory')
#         Label1.place(x=50, y=20)
#         Txt1 = tk.Entry(border, width=30, bd=5)
#         Txt1.place(x=180, y=20)
#
#         Label2 = tk.Label(border, text="Password",
#                           font=("Arial Bold", 15), bg='ivory')
#         Label2.place(x=50, y=80)
#         TXT2 = tk.Entry(border, width=30, show='*', bd=5)
#         TXT2.place(x=180, y=80)
#
#         def verify():
#             try:
#                 with open("credential.txt", "r") as f:
#                     info = f.readlines()
#                     i = 0
#                     for e in info:
#                         u, p = e.split(",")
#                         if u.strip() == Txt1.get() and p.strip() == TXT2.get():
#                             controller.show_frame(SecondPage)
#                             i = 1
#                             break
#                     if i == 0:
#                         messagebox.showinfo(
#                             "Error", "Please provide correct username and password!!")
#             except:
#                 messagebox.showinfo(
#                     "Error", "Please provide correct username and password!!")
#
#         BTN1 = tk.Button(border, text="Submit",
#                          font=("Arial", 15), command=verify)
#         BTN1.place(x=320, y=115)
#
#         def register():
#             window = tk.Tk()
#             window.resizable(0, 0)
#             window.configure(bg="deep sky blue")
#             window.title("Register")
#             Label1 = tk.Label(window, text="Username:", font=(
#                 "Arial", 15), bg="deep sky blue")
#             Label1.place(x=10, y=10)
#             txt1 = tk.Entry(window, width=30, bd=5)
#             txt1.place(x=200, y=10)
#
#             lbl2 = tk.Label(window, text="Password:", font=(
#                 "Arial", 15), bg="deep sky blue")
#             lbl2.place(x=10, y=60)
#             txt2 = tk.Entry(window, width=30, show="*", bd=5)
#             txt2.place(x=200, y=60)
#
#             lbl3 = tk.Label(window, text="Confirm Password:",
#                             font=("Arial", 15), bg="deep sky blue")
#             lbl3.place(x=10, y=110)
#             txt3 = tk.Entry(window, width=30, show="*", bd=5)
#             txt3.place(x=200, y=110)
#
#             def check():
#                 if txt1.get() != "" or txt2.get() != "" or txt3.get() != "":
#                     if txt2.get() == txt3.get():
#                         with open("credential.txt", "a") as f:
#                             f.write(txt1.get() + "," + txt2.get() + "\n")
#                             messagebox.showinfo(
#                                 "Welcome", "You are registered successfully!!")
#                     else:
#                         messagebox.showinfo(
#                             "Error", "Your password didn't get match!!")
#                 else:
#                     messagebox.showinfo(
#                         "Error", "Please fill the complete field!!")
#
#             btn1 = tk.Button(window, text="Sign in", font=(
#                 "Arial", 15), bg="#ffc22a", command=check)
#             btn1.place(x=170, y=150)
#
#             window.geometry("470x220")
#             window.mainloop()
#
#         BTN2 = tk.Button(self, text="Register", bg="dark orange",
#                          font=("Arial", 15), command=register)
#         BTN2.place(x=650, y=20)
#
#
# class SecondPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#
#         load = Image.open("img2.jpg")
#         photo = ImageTk.PhotoImage(load)
#         label = tk.Label(self, image=photo)
#         label.image = photo
#         label.place(x=0, y=0)
#
#         Button = tk.Button(self, text="Next", font=(
#             "Arial", 15), command=lambda: controller.show_frame(ThirdPage))
#         Button.place(x=650, y=450)
#
#         Button = tk.Button(self, text="Back", font=(
#             "Arial", 15), command=lambda: controller.show_frame(FirstPage))
#         Button.place(x=100, y=450)
#
#
# class ThirdPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#
#         self.configure(bg='Tomato')
#
#         Label = tk.Label(self,
#                          text="Store some content related to your \n project or what your application made for. \n All the best!!",
#                          bg="orange", font=("Arial Bold", 25))
#         Label.place(x=40, y=150)
#
#         Button = tk.Button(self, text="Home", font=(
#             "Arial", 15), command=lambda: controller.show_frame(FirstPage))
#         Button.place(x=650, y=450)
#
#         Button = tk.Button(self, text="Back", font=(
#             "Arial", 15), command=lambda: controller.show_frame(SecondPage))
#         Button.place(x=100, y=450)
#
#
# class Application(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#
#         # creating a window
#         window = tk.Frame(self)
#         window.pack()
#
#         window.grid_rowconfigure(0, minsize=500)
#         window.grid_columnconfigure(0, minsize=800)
#
#         self.frames = {}
#         for F in (FirstPage, SecondPage, ThirdPage):
#             frame = F(window, self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame(FirstPage)
#
#     def show_frame(self, page):
#         frame = self.frames[page]
#         frame.tkraise()
#         self.title("Application")
#
#
# app = Application()
# app.maxsize(800, 500)
# app.mainloop()
