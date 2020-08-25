from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("checkboxes")
root.geometry("400x400")

def show():
  myLabel = Label(root, text=var.get()).pack()

# declaring a variable as a string
var = StringVar()

# checkbox; can set as a variable and change on/off values
c = Checkbutton(root, text="Check", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()