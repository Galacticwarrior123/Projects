from tkinter import *
from datetime import date

root = Tk()
root.title("getting started with widgets")
root.geometry("400x300")

lbl = Label(root, text="Hello", fg="black", bg="white", height=1, width=300)

name_lbl = Label(text="Full name", bg="blue")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "welcome to the application"
    greet = "Hello " + name + "\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=5)
btn = Button(text="Begin", command=display, height=1, bg="green", fg="white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()