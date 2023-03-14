from tkinter import *
import sqlite3

window = Tk()
window.geometry('400x400')

database = sqlite3.connect("gadgets.db")
cursor = database.cursor()

# cursor.execute("create table Customers(ID auto_increment primary key, Name Text, Mobile Text, Location Text)")

# create = "CREATE TABLE signup (firstname TEXT, lastname TEXT, username TEXT, c_username TEXT, password TEXT, c_password TEXT, license TEXT)"
# cursor.execute(create)


cursor.execute('select name from products')
records = cursor.fetchall()

for record in records:
    print(record[0])


database.commit()
database.close()



mainloop()

