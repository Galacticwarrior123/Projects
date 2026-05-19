from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.geometry("600x400")
root.config(bg="blue")


Label(
    root,
    text = "Welcome to Denomination Counter",
    bg = "blue",
    font=("Arial",14)
).pack()

def topwin():
    top = Toplevel()
    top.title("Calculator")
    top.geometry("400x300")
    top.config(bg="blue")

    Label(top,text="Enter the amount:", bg="blue").pack(pady=5)

    entry = Entry(top)
    entry.pack()

    e1= Entry(top)
    e2= Entry(top)
    e3= Entry(top)

    def calc():
        amt=int(entry.get())
        n2000 = amt // 2000
        amt = amt % 2000
        
        n500 = amt // 500
        amt = amt % 500
     
        n100 = amt // 100
    
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

        e1.insert(0,n2000)
        e2.insert(0,n500)
        e3.insert(0,n100)

    Button(top,text="Calculate", command=calc, bg="white").pack(pady=10)

    Label(top,text=" 2000 notes:", bg="black").pack()
    e1.pack()

    Label(top,text=" 500 notes:", bg="black").pack()
    e2.pack()

    Label(top,text=" 100 notes:", bg="black").pack()
    e3.pack()

    Button(
        root,
        text="Start",
        command=topwin,
        bg="blue",
        fg="white"
    ).pack(pady=20)

root.mainloop()
