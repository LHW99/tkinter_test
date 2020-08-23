from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog

root = Tk()
root.title("File")

def open():
  global my_image
  # looking for particular files
  # filetypes is for the dropdown that looks for file types
  root.filename = filedialog.askopenfilename(
  initialdir='/home/haiduk/Desktop', 
  title='Select a file', 
  filetypes=(('gif files',"*.gif"),("all files","*.*")))

  # opens the photo when selected from directory menu
  my_label = Label(root, text=root.filename).pack()
  my_image = ImageTk.PhotoImage(Image.open(root.filename))
  my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()


root.mainloop()