from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather")
root.geometry("500x500")


try:
  api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=vancouver&appid=82ccd7079a318bf163422706a0f39c8b")
  # strip from json
  api = json.loads(api_request.content)
  name = api["name"]
  weather = api["weather"]
except Exception as e:
  api = "Error..."

# put a 0 after the index for a nested dictionary; otherwise, python won't look in the dictionary
mylabel = Label(root, font=("Helvetica", 20), text=api["name"] + " currently " + api["weather"][0]["description"])
mylabel.pack()

root.mainloop()