from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("databases")
root.geometry("400x400")

# Databases



# create table
# use sqlite language in the quotes
# text, int(integer), real(numbers), null, blob(img, video, etc)
'''
c.execute("""CREATE TABLE addresses (
  first_name text,
  last_name text,
  address text,
  city text,
  state text,
  zipcode integer
  )""")
'''

# create the submit function for database
def submit():
  # create a database or connect to one
  # if db doesnt exist, will create one in the file's directory
  conn = sqlite3.connect('address_book.db')

  # cursor creation, it's like a courier that gets the data we want in the dn
  c = conn.cursor()

  # insert into table
  c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
      {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()
      }  
  
  )

  # commits changes to database
  conn.commit()

  # close connection
  conn.close()


  # clear the text boxes
  f_name.delete(0, END)
  l_name.delete(0, END)
  address.delete(0, END)
  city.delete(0, END)
  state.delete(0, END)
  zipcode.delete(0, END)


#create textboxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=0, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=0, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=0, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=0, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=0, padx=20)

#create textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

# create submit button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)




root.mainloop()