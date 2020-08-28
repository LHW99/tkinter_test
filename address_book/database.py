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

# create save function for editing
def save():
  conn = sqlite3.connect('address_book.db')

  c = conn.cursor()

  record_id = select_box.get()
  #Delete a record
  # SQLite language must be in string format
  # code is saying 'update these fields according to the inputs, based on the oid'
  # triple quotes for multi-line sql code
  c.execute("""UPDATE addresses SET
    first_name = :first, 
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
  
    WHERE oid = :oid""",
    {'first': f_name_editor.get(),
    'last': l_name_editor.get(),
    'address': address_editor.get(),
    'city': city_editor.get(),
    'state': state_editor.get(),
    'zipcode': zipcode_editor.get(),

    'oid': record_id
    })

  conn.commit()

  conn.close()

  editor.destory()


# create edit function to update record
def edit():
  global editor
  editor = Tk()
  editor.title("Edit a record")
  editor.geometry("400x400")

  conn = sqlite3.connect('address_book.db')

  c = conn.cursor()

  record_id = select_box.get()
  # query the database
  # oid represents the unique id number for each entry
  c.execute("SELECT *, oid FROM addresses WHERE oid = " + record_id)
  records = c.fetchall()

  # create global variables for textbox names
  global f_name_editor
  global l_name_editor
  global address_editor
  global city_editor
  global state_editor
  global zipcode_editor

  #create textboxes
  f_name_editor = Entry(editor, width=30)
  f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

  l_name_editor = Entry(editor, width=30)
  l_name_editor.grid(row=1, column=1, padx=20)

  address_editor = Entry(editor, width=30)
  address_editor.grid(row=2, column=1, padx=20)

  city_editor = Entry(editor, width=30)
  city_editor.grid(row=3, column=1, padx=20)

  state_editor = Entry(editor, width=30)
  state_editor.grid(row=4, column=1, padx=20)

  zipcode_editor = Entry(editor, width=30)
  zipcode_editor.grid(row=5, column=1, padx=20)

  #create textbox labels
  f_name_label = Label(editor, text="First Name")
  f_name_label.grid(row=0, column=0, pady=(10, 0))

  l_name_label = Label(editor, text="Last Name")
  l_name_label.grid(row=1, column=0)

  address_label = Label(editor, text="Address")
  address_label.grid(row=2, column=0)

  city_label = Label(editor, text="City")
  city_label.grid(row=3, column=0)

  state_label = Label(editor, text="State")
  state_label.grid(row=4, column=0)

  zipcode_label = Label(editor, text="Zipcode")
  zipcode_label.grid(row=5, column=0)

  # loop through results
  for record in records: 
    f_name_editor.insert(0, record[0])
    l_name_editor.insert(0, record[1])
    address_editor.insert(0, record[2])
    city_editor.insert(0, record[3])
    state_editor.insert(0, record[4])
    zipcode_editor.insert(0, record[5])

  # Create a save button for edited record
  save_btn = Button(editor, text="Save Record", command=save)
  save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


# create function to delete a record
def delete():
  conn = sqlite3.connect('address_book.db')

  c = conn.cursor()

  #Delete a record
  # SQLite language must be in string format
  c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

  conn.commit()

  conn.close()

# create the submit function for database
def submit():
  # create a database or connect to one
  # if db doesnt exist, will create one in the file's directory
  conn = sqlite3.connect('address_book.db')

  # cursor creation, it's like a courier that gets the data we want in the dn
  c = conn.cursor()

  # insert into table
  c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
      # making a python dictionary
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

# create query function
def query():
  conn = sqlite3.connect('address_book.db')

  c = conn.cursor()

  # query the database
  # oid represents the unique id number for each entry
  c.execute("SELECT *, oid FROM addresses")
  records = c.fetchall()
  # print(records)

  # loop through results
  print_records=''
  for record in records:
    # an example if you want to print parts of each record
    print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"
    # print_records += str(record) + "\n"

  query_label = Label(root, text=print_records)
  query_label.grid(row=12, column=0, columnspan=2)

  conn.commit()

  conn.close()

#create textboxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

select_box = Entry(root, width=30)
select_box.grid(row=9, column=1, pady=5)

#create textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

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

select_box_label = Label(root, text="Select ID")
select_box_label.grid(row=9, column=0, pady=5)

# create submit button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create a query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

# create a edit button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

# Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

root.mainloop()