from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather")
root.geometry("500x500")

api_request = requests.get("")


root.mainloop()