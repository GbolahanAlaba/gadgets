from tkinter import *
from datetime import *
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from PIL import ImageTk, Image
import home



class SETUP:
    def __init__(self, window):
        self.window = window
        self.window.wm_iconbitmap('Images/icon.ico')
        self.window.title('Gadgets-360 | Set Up')
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        self.window.geometry(f'{sw}x{sh}')
        self.window.state('zoomed')
        self.window.configure(bg="white")


        # Menu Bar
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        

        # Create menu
        # File menu
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Print')
        file_menu.add_command(label='Export')
        file_menu.add_separator()

        sub_file_menu = Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label='Layout', menu=sub_file_menu)
        sub_file_menu.add_command(label='Add or remove columns')
        sub_file_menu.add_command(label='Save')
        sub_file_menu.add_separator()
        sub_file_menu.add_command(label='Restore default layout')

        file_menu.add_separator()
        file_menu.add_command(label='Log Out')
        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=self.window.destroy)

        # Show menu
        show_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Show', menu=show_menu)
        show_menu.add_command(label='Sales')
        show_menu.add_command(label='Quotation')
        show_menu.add_command(label='Customers')
        show_menu.add_command(label='Products')
        show_menu.add_command(label='Account Payable')
        show_menu.add_command(label='Register')
        show_menu.add_command(label='Users')
        show_menu.add_command(label='Statistics')
        show_menu.add_separator()
        show_menu.add_command(label='Hide Test')

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='1. Learn how to manage your POS')
        help_menu.add_separator()
        help_menu.add_command(label='2. Online Technical Suport')
        help_menu.add_separator()
        help_menu.add_command(label='3. Terms of service')
        help_menu.add_separator()
        help_menu.add_command(label='4. Update Techcified POS')
        help_menu.add_separator()
        help_menu.add_command(label='5. Renew your POS license')
        help_menu.add_separator()
        sub_help_menu = Menu(help_menu, tearoff=0)
        help_menu.add_cascade(label='6. Account', menu=sub_help_menu)
        sub_help_menu.add_command(label='Create a new account')

        # Databases
        def Branch():
            database = sqlite3.connect("gadgets.db")
            cursor = database.cursor()
            if not BrEntry.get():
                messagebox.showerror('Invalid!', 'Field cannot be empty!')
            else:
                Val = (BrEntry.get())
                cursor.execute('insert into branches (Location) Values(?)', [Val])
                messagebox.showinfo('Great!', 'Branch added successfully!')
                BrEntry.delete(0, END)      
            database.commit()
            database.close()
        
        def Vendor():
            database = sqlite3.connect("gadgets.db")
            cursor = database.cursor()
            if not VenEntry.get():
                messagebox.showerror('Invalid!', 'Field cannot be empty!')
            else:
                Val = (VenEntry.get())
                cursor.execute('insert into vendors (Name) Values(?)', [Val])
                messagebox.showinfo('Great!', 'Vendor added successfully!')
                VenEntry.delete(0, END)      
            database.commit()
            database.close()
        
        def Product():
            database = sqlite3.connect("gadgets.db")
            cursor = database.cursor()
            if not ProNameEntry.get() or not BrandCombo.get():
                messagebox.showerror('Invalid!', 'Field cannot be empty!')
            else:
                Val = (ProNameEntry.get(), BrandCombo.get())
                cursor.executemany('insert into products (Name, Brand) Values(?, ?)', [Val])
                messagebox.showinfo('Great!', 'Product added successfully!')
                ProNameEntry.delete(0, END)
                BrandCombo.delete(0, END)     
            database.commit()
            database.close()
        
        def Custom():
            database = sqlite3.connect("gadgets.db")
            cursor = database.cursor()
            if not CusNameEntry.get() or not CusMobEntry.get() or not CusLocEntry.get() :
                messagebox.showerror('Invalid!', 'Field cannot be empty!')
            else:
                Val = (CusNameEntry.get(), CusMobEntry.get(), CusLocEntry.get())
                cursor.executemany('insert into customers (Name, Mobile, Location) Values(?, ?, ?)', [Val])
                messagebox.showinfo('Great!', 'Customer added successfully!')
                CusNameEntry.delete(0, END)
                CusMobEntry.delete(0, END)
                CusLocEntry.delete(0, END)    
            database.commit()
            database.close()
        
        def Lic():
            database = sqlite3.connect("gadgets.db")
            cursor = database.cursor()
            if not LicEntry.get():
                messagebox.showerror('Invalid!', 'Field cannot be empty!')
            else:
                Val = (LicEntry.get())
                cursor.execute('insert into license (keypass) Values(?)', [Val])
                messagebox.showinfo('Great!', 'License added successfully!')
                LicEntry.delete(0, END)      
            database.commit()
            database.close()

        
        Title = Label(window, text='Application Set Up', font=('roboto', 13, 'bold'), bg='white', fg='#D30E0E')
        Title.place(relx=0.5, y=15, anchor=N)

        Home_B = Button(window, text='Back', font=('roboto', 12, 'bold'), bd=0, bg='#D30E0E', fg='white', cursor='hand2', command=self.homepage)
        Home_B.place(x=200, y=20, anchor=N, width=100)

        LBF = LabelFrame(window, text="", width=1100, height=600)
        LBF.place(x=150, y=50)

        # Add Branch
        Brlabel = Label(LBF, text='Add Branch:', font=('roboto', 12, 'bold')).place(x=10, y=30)
        Br = Label(LBF, text='Location:',  font=('Arial', 10, 'bold')).place(x=10, y=65)
        BrEntry = Entry(LBF,  font=('Arial', 10, 'bold'), bd=2, relief='groove')
        BrEntry.place(x=90, y=65)
        Brbut = Button(LBF, text='Add', font=('Arial', 10, 'bold'), bd=0, bg='green', fg='white', cursor='hand2', command=Branch).place(x=255, y=62, width=100)

        # Add Vendor
        Venlabel = Label(LBF, text='Add Vendor', font=('roboto', 12, 'bold')).place(x=10, y=100)
        Vendor = Label(LBF, text='Vendor:',  font=('Arial', 10, 'bold')).place(x=10, y=135)
        VenEntry = Entry(LBF,  font=('Arial', 10, 'bold'), bd=2, relief='groove')
        VenEntry.place(x=90, y=135)
        VendorBut = Button(LBF, text='Add', font=('Arial', 10, 'bold'), bd=0, bg='green', fg='white', cursor='hand2', command=Vendor).place(x=255, y=132, width=100)

        
        # Add Product
        List = [
            'Apple',
            'Samsung',
            'Others'

        ]
        Prolabel = Label(LBF, text='Add Product', font=('roboto', 12, 'bold')).place(x=10, y=170)
        ProductName = Label(LBF, text='Name:',  font=('Arial', 10, 'bold')).place(x=10, y=205)
        ProNameEntry = Entry(LBF,  font=('Arial', 10, 'bold'), bd=2, relief='groove')
        ProNameEntry.place(x=90, y=205)
        BrandName = Label(LBF, text='Brand:',  font=('Arial', 10, 'bold')).place(x=255, y=205)
        BrandCombo = ttk.Combobox(LBF, value=List)
        BrandCombo.current(0)
        BrandCombo.bind('<<<ComboboxSelected>>>')
        BrandCombo.place(x=330, y=205)
        ProductBut = Button(LBF, text='Add', font=('Arial', 10, 'bold'), bd=0, bg='green', fg='white', cursor='hand2', command=Product).place(x=495, y=202, width=100)

        # Add Customer
        Cuslabel = Label(LBF, text='Add Customer', font=('roboto', 12, 'bold')).place(x=10, y=240)
        Customer = Label(LBF, text='Name:',  font=('Arial', 10, 'bold')).place(x=10, y=275)
        CusNameEntry = Entry(LBF,  font=('Arial', 10, 'bold'), bd=2, relief='groove')
        CusNameEntry.place(x=70, y=275)
        CusMobile = Label(LBF, text='Mobile No.:',  font=('Arial', 10, 'bold')).place(x=235, y=275)
        CusMobEntry = Entry(LBF,  font=('Arial', 10, 'bold'), bd=2, relief='groove')
        CusMobEntry.place(x=330, y=275)
        CusLoc = Label(LBF, text='Location:',  font=('Arial', 10, 'bold')).place(x=500, y=275)
        CusLocEntry = Entry(LBF,  font=('Arial', 10, 'bold'), bd=2, relief='groove')
        CusLocEntry.place(x=580, y=275)
        CustomerBut = Button(LBF, text='Add', font=('Arial', 10, 'bold'), bd=0, bg='green', fg='white', cursor='hand2', command=Custom).place(x=750, y=272, width=100)


        License = Label(LBF, text='Create account license:',  font=('Arial', 10, 'bold')).place(x=10, y=530)
        LicEntry = Entry(LBF,  font=('Arial', 10, 'bold'), bd=2, relief='groove')
        LicEntry.place(x=180, y=530)
        LicBut = Button(LBF, text='Add', font=('Arial', 10, 'bold'), bd=0, bg='green', fg='white', cursor='hand2', command=Lic).place(x=350, y=527, width=100)

    # functions
    def homepage(self):
        win = Toplevel()
        home.HOME(win)
        self.window.withdraw()
        win.deiconify()
    


def dash():
    window = Tk()
    SETUP(window)
    window.mainloop()


if __name__ == '__main__':
    dash()




