from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('plot')
root.geometry("400x200")

def graph():
  # generating random collection of data
  # average price, standard deviation, number of entries
  house_prices = np.random.normal(200000, 25000, 5000)
  # hist = histogram
  plt.hist(house_prices, 50)
  plt.show()

btn = Button(root, text="Graph It!", command=graph)
btn.pack()

root.mainloop()