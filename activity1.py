from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light  blue')
root.geometry('650x400')

upload = Image.open('game.png')
upload = upload.resize(300, 300)
label = Label(root, image=Image, bg='light blue')
label.place(x=180, y=20)

label = Label(root,
              text="Hey User! Welcome to Denomination Counter Application.",
              bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.Showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox =='ok':
        topwin()

button1 =Button(root,
                text="Let's get started:"
                command=msg,
                bg='brown'
                fg='white')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg='aquamarine')
    top.geometry("600x350+58+58")

    label = Label(top, text="Enter total amount", bg='cyan')
    entry = Entry(top)
    lbl = label(top, text="Here are the number of each denominations", bg='blue')
    
    l1 =Label(top, text="2003", bg='gold')
    l2 =Label(top, text="586", bg='red')
    l3 =Label(top, text="410", bg='light blue')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

def calculator():
    try:
        global amount
        amount = int(entry.get())
        note2000 = amount // 2000
        amount %= 2000
        note 
