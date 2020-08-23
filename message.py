from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox

root = Tk()
root.title("Messages")

# function that makes a popup '.showinfo' is imported from messagebox
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
  # (title of popup, content of popup)
  response = messagebox.showinfo("This is my popup", "Hello World!")
  Label(root, text=response).pack()
  #if response == 1:
  #  Label(root, text="You Clicked Yes!").pack()
  #else:
  # Label(root, text="You Clicked No!").pack()

Button(root, text="Popup", command=popup).pack()



root.mainloop()