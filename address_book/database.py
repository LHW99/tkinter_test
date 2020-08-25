from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("databases")
root.geometry("400x400")

# Databases

# create a database or connect to one
# if db doesnt exist, will create one in the file's directory
conn = sqlite3.connect('address_book.db')

# cursor creation, it's like a courier that gets the data we want in the dn
c = conn.cursor()

# create table
# use sqlite language in the quotes
# text, int(integer), real(numbers), null, blob(img, video, etc)
c.execute("""CREATE TABLE addresses (
  first_name text,
  last_name text,
  address text,
  city text,
  state text,
  zipcode integer
  )""")

# commits changes to database
conn.commit()

# close connection
conn.close()


root.mainloop()