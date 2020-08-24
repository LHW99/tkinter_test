from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Sliders')
# sets size of window
root.geometry("400x400")


# making a slider; need an underscore for from, but not for to
vertical = Scale(root, from_=0, to=400)
vertical.pack()

def slide():
  my_label = Label(root, text=horizontal.get()).pack()
  root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

#orient HORIZONTAL for horizontal bar
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_btn = Button(root, text="click me", command=slide).pack()

root.mainloop()