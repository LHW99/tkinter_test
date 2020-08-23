from tkinter import *
from PIL import ImageTk, Image

# NOT good form to have more than 1 Tk() level, so make a TopLevel()
root = Tk()
root.title("Base Layer")

#function to open another window
def open():
  # my_img has to be declared a global variable, 
  # otherwise python will discard it
  global my_img
  top = Toplevel()
  top.title("Top Layer")
  my_img = ImageTk.PhotoImage(Image.open("/home/haiduk/Desktop/pompom.gif"))
  my_label = Label(top, image=my_img).pack()
  #button to close second window
  btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()






root.mainloop()