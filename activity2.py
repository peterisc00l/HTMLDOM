from tkinter import *
from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry as well
root = Tk()
root.title('image')
root.geometry('400x400')

# Now use Image.open to open and identify the given image file.
upload = Image.open("My roblox avatar.png")

image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Lable
lable = Label(root, image=image, height=350, width=300)
lable.place(x=50, y=0)
lable2 = Label(root, text="This is how you add image in Tkinter Window")
lable2.place(x=40, y=360)

root.mainloop()