from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather")
root.geometry("500x500")

# create lookup function
def cityLookup():
  try:
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city.get() + "&appid={api key goes here}")
    # strip from json
    api = json.loads(api_request.content)
    name = api["name"]
    weather = api["weather"][0]["description"]
  except Exception as e:
    api = "Error..."

  # put a 0 after the index for a nested dictionary; otherwise, python won't look in the dictionary
  mylabel = Label(root, font=("Helvetica", 20), text=name + " currently " + weather)
  mylabel.grid(row=0, column=0)

city = Entry(root)
city.grid(row=1, column=0)

citybtn = Button(root, text="Look up City", command=cityLookup)
citybtn.grid(row=1, column=1)


root.mainloop()
