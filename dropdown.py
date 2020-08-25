from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('dropdown')
root.geometry("400x400")

# drop down boxes

def show():
  myLabel = Label(root, text=clicked.get()).pack()

options = [
  "Monday", 
  "Tuesday", 
  "Wednesday", 
  "Thursday", 
  "Friday"
]

clicked = StringVar()
clicked.set(options[0])

# OptionMenu is a dropdown; can use a python list for the dropdown options
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()