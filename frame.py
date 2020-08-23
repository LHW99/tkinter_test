from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frames')
img = PhotoImage(file='/home/haiduk/Desktop/prime.png')
root.tk.call('wm', 'iconphoto', root._w, img)

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here!")
b2 = Button(frame, text="Don't!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()