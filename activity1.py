from tkinter import *

window = Tk()
window.title('Tkinker Sample Window')
window.geometry('300x300')

greeting = Label(text="Hello User", fg='aquamarine', bg='blue')
button = Button(text="Click me", bg='black', width=50)
entry = Entry(fg="cyan", bg="blue", width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
lable = Label(master=frame, text='Sample Frame')
lable.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()