from tkinter import *
import sqlite3

window = Tk()
window.geometry('400x400')

# database = sqlite3.connect("gadgets.db")
# cursor = database.cursor()

# cursor.execute("create table Customers(ID auto_increment primary key, Name Text, Mobile Text, Location Text)")

# create = "CREATE TABLE signup (firstname TEXT, lastname TEXT, username TEXT, c_username TEXT, password TEXT, c_password TEXT, license TEXT)"
# cursor.execute(create)


# cursor.execute('select name from products')
# records = cursor.fetchall()

# for record in records:
#     print(record[0])
#     x = record[0]

# database.commit()
# database.close()

def SalesData():
        db = sqlite3.connect('gadgets.db')
        cursor = db.cursor()
        cursor.execute('select name from products')
        records = cursor.fetchall()
        
        global count
        count = 0
        for record in records:
            MyList.insert(END, record[0]) 
            count = count + 1

        db.commit()
        db.close()

MyList = Listbox(window, width=33, height=10)
MyList.place(x=30, y=165)

SalesData()

mainloop()

