from tkinter import *
# to import other image types for python to read
from PIL import Image, ImageTk

root = Tk()
root.title('Image Viewer')
# creates a top corner icon. different file types might break
img = PhotoImage(file='/home/haiduk/Desktop/prime.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# adding image to widgit
my_img = ImageTk.PhotoImage(Image.open("/home/haiduk/Desktop/pom.jpg"))
my_label = Label(image=my_img)
my_label.pack()







# quit button
button_quit = Button(root, text="exit program", command=root.quit)
button_quit.pack()



root.mainloop()