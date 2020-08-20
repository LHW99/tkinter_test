from tkinter import *

root = Tk()

def myClick():
  myLabel = Label(root, text="Look! I clicked a button!")
  myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="white", bg="#000000")
myButton.pack()

root.mainloop()

# padx, pady are padding