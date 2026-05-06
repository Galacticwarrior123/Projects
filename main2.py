from tkinter import*

root = Tk()
root.title("Login app")
root.geometry("400x400")

frame = Frame(master=root,height=200,width=360,bg="lightgray")

lb1 = Label(frame, text = "Full name",bg="lightgray",fg="black",width=12)
lb2 = Label(frame, text = "Password",bg="lightgray",fg="black",width=12)
lb3 = Label(frame, text = "Email ID",bg="lightgray",fg="black",width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")
def display():
    name = name_entry.get()
    greet = "Hey! " + name
    message ="\n Congratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(text= "Create Account", command=display, bg="lightgray")

frame.place(x=20,y=0)
lb1.place(x=20,y=20)
lb2.place(x=20,y=80)
lb3.place(x=20,y=140)
name_entry.place(x=150,y=20)
email_entry.place(x=150,y=80)
pass_entry.place(x=150,y=140)
textbox.place(y=250)
btn.place(x=130,y=210)

root.mainloop()