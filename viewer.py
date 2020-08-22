from tkinter import *
# to import other image types for python to read
from PIL import Image, ImageTk

root = Tk()
root.title('Image Viewer')

# creates a top corner icon. different file types might break
img = PhotoImage(file='/home/haiduk/Desktop/prime.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# adding image to widgit
my_img1 = ImageTk.PhotoImage(Image.open("/home/haiduk/Desktop/pom.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("/home/haiduk/Desktop/pompom.gif"))
my_img3 = ImageTk.PhotoImage(Image.open("/home/haiduk/Desktop/prime.png"))

image_list = [my_img1, my_img2, my_img3]



my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
  global my_label
  global button_forward
  global button_back

  #deletes image in label, assigned new, reassigns command for back and forward
  my_label.grid_forget()
  my_label = Label(image=image_list[image_number-1])
  button_forward = Button(root, text="->", command=lambda: forward(image_number + 1))
  button_back = Button(root, text="<-", command=lambda: back(image_number - 1))
  
  if image_number == 3:
    button_forward = Button(root, text="->", state=DISABLED)

  my_label.grid(row=0, column=0, columnspan=3)
  button_back.grid(row=1,column=0)
  button_forward.grid(row=1,column=2)

def back(image_number):
  global my_label
  global button_forward
  global button_back

  my_label.grid_forget()
  my_label = Label(image=image_list[image_number-1])
  button_forward = Button(root, text="->", command=lambda: forward(image_number + 1))
  button_back = Button(root, text="<-", command=lambda: back(image_number - 1))
  
  if image_number == 1:
    button_back = Button(root, text="<-", state=DISABLED)

  my_label.grid(row=0, column=0, columnspan=3)
  button_back.grid(row=1,column=0)
  button_forward.grid(row=1,column=2)

# quit button
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=1)

#back and forward buttons
button_back = Button(root, text="<-", command=back, state=DISABLED)
button_back.grid(row=1,column=0)
button_forward = Button(root, text="->", command=lambda: forward(2))
button_forward.grid(row=1,column=2)

root.mainloop()