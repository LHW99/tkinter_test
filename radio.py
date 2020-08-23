from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Buttons')

#r = IntVar()
#r.set("2")

# creating multiple radio buttons through loop instead of creating individually
# array for values
TOPPINGS =[
  ("Pepperoni", "Pepperoni"),
  ("Cheese", "Cheese"),
  ("Mushroom", "Mushroom"),
  ("Onion", "Onion")
]

# creating a variable for all options
pizza = StringVar()
pizza.set("Pepperoni")

# loop that creates radio buttons
for text, topping in TOPPINGS:
  Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

# function remembering radio values
def clicked(value):
  myLabel = Label(root, text=value)
  myLabel.pack()

# radio buttons
# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=r.get())
# myLabel.pack()

myButton = Button(root, text="click me", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()