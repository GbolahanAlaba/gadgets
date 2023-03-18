from tkinter import *
from datetime import *
from time import strftime
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from PIL import ImageTk, Image
import home



class DASHBOARD:
    def __init__(self, window):
        self.window = window
        self.window.wm_iconbitmap('Images/icon.ico')
        self.window.title('Gadgets-360 | DASHBOARD')
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        self.window.geometry(f'{sw}x{sh}')
        self.window.state('zoomed')
        self.window.configure(bg="lightgrey")


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


        MenuFrame = Frame(window,bg='#D30E0E')
        MenuFrame.place(x=0, y=0, width=sw, height=32)
        
        B1 = Button(MenuFrame, text='Home', font=('Arial', 9, 'bold'), bg='white', fg="#3C4479", bd=0, width=18, cursor='hand2')
        B1.grid(row=0, column=0, padx=5, pady=5)
        B2 = Button(MenuFrame, text='Products', font=('Arial', 9, 'bold'), bg='white', fg="#3C4479", bd=0, width=18, cursor='hand2')
        B2.grid(row=0, column=1, padx=5, pady=5)
        B3 = Button(MenuFrame, text='Sales', font=('Arial', 9, 'bold'), bg='white', fg="#3C4479", bd=0, width=18, cursor='hand2')
        B3.grid(row=0, column=2, padx=5, pady=5)
        B4 = Button(MenuFrame, text='Inventory', font=('Arial', 9, 'bold'), bg='white', fg="#3C4479", bd=0, width=18, cursor='hand2')
        B4.grid(row=0, column=3, padx=5, pady=5)
        B5 = Button(MenuFrame, text='Expenses', font=('Arial', 9, 'bold'), bg='white', fg="#3C4479", bd=0, width=18, cursor='hand2')
        B5.grid(row=0, column=4, padx=5, pady=5)
        B6 = Button(MenuFrame, text='Customers', font=('Arial', 9, 'bold'), bg='white', fg="#3C4479", bd=0, width=18, cursor='hand2')
        B6.grid(row=0, column=5, padx=5, pady=5)
        B7 = Button(MenuFrame, text='Branches', font=('Arial', 9, 'bold'), bg='white', fg="#3C4479", bd=0, width=18, cursor='hand2')
        B7.grid(row=0, column=6, padx=5, pady=5)
        B8 = Button(MenuFrame, text='Report', font=('Arial', 8, 'bold'), bg='white', fg="#3C4479", bd=0, width=18, cursor='hand2')
        B8.grid(row=0, column=7, padx=5, pady=5)


        Date = datetime.now()
        Menu10 = Label(MenuFrame, text=f"{Date:%A, %B, %d, %Y}", font=('roboto', 10, 'bold'), bg='white', fg='green')
        Menu10.grid(row=0, column=8, padx=5, pady=5)
        Time = strftime('%I:%M:%S')
        Menu11 = Label(MenuFrame, text=Time, font=('roboto', 10, 'bold'), bg='white', fg='green')
        Menu11.grid(row=0, column=9, pady=5)
        Menu11.after(1000, time)

        # ----------------------- Front Board Frames & Labels Begins---------------------------
        FR1 = Frame(window, bg='white')
        FR1.place(x=35, y=50, width=300, height=90)
        FR2 = Frame(window, bg='white')
        FR2.place(x=365, y=50, width=300, height=90)
        FR3 = Frame(window, bg='white')
        FR3.place(x=695, y=50, width=300, height=90)
        FR4 = Frame(window, bg='white')
        FR4.place(x=1025, y=50, width=300, height=90)

        img = PhotoImage(file='./Images/inf.png')
        InFimg = Label(FR1, image = img)
        InFimg.photo = img
        InFimg.place(x=220, y=15)
        Inflow = Label(FR1, text='Inflow',font=('Arial', 10, 'bold'), bg='white', fg='#D30E0E').place(x=13,y=5)
        Inflow = Label(FR1, text="₦{:,.2f}".format(1000000),font=('Arial', 15, 'bold'), bg='white').place(x=13, y=35)
        Inflow = Label(FR1, text='Gross Profit',font=('Arial', 8, 'bold'), bg='white', fg='green').place(x=13, y=70)

        img = PhotoImage(file='./Images/outflow.png')
        Outfimg = Label(FR2, image = img, bg='white')
        Outfimg.photo = img
        Outfimg.place(x=220, y=15)
        Outflow = Label(FR2, text='Outflow',font=('Arial', 10, 'bold'), bg='white', fg='#D30E0E').place(x=13,y=5)
        Outflow = Label(FR2, text="₦{:,.2f}".format(580000),font=('Arial', 15, 'bold'), bg='white').place(x=13, y=35)
        Outflow = Label(FR2, text='Capital',font=('Arial', 8, 'bold'), bg='white', fg='green').place(x=13, y=70)

        img = PhotoImage(file='./Images/expense.png')
        Expimg = Label(FR3, image = img, bg='white')
        Expimg.photo = img
        Expimg.place(x=220, y=15)
        Exp = Label(FR3, text='Expenses',font=('Arial', 10, 'bold'), bg='white', fg='#D30E0E').place(x=13,y=5)
        Exp = Label(FR3, text="₦{:,.2f}".format(120000),font=('Arial', 15, 'bold'), bg='white').place(x=13, y=35)
        Exp = Label(FR3, text='All Expense',font=('Arial', 8, 'bold'), bg='white', fg='green').place(x=13, y=70)

        img = PhotoImage(file='./Images/balance.png')
        Balimg = Label(FR4, image = img, bg='white')
        Balimg.photo = img
        Balimg.place(x=220, y=15)
        Bal = Label(FR4, text='Balance',font=('Arial', 10, 'bold'), bg='white', fg='#D30E0E').place(x=13,y=5)
        Bal = Label(FR4, text="₦{:,.2f}".format(300000),font=('Arial', 15, 'bold'), bg='white').place(x=13, y=35)
        Bal = Label(FR4, text='Available Balance',font=('Arial', 8, 'bold'), bg='white', fg='green').place(x=13, y=70)

        # -----------------------Board Frames & Labels Ends---------------------------

        # -----------------------Side Board Frames & Labels Begins-----------------------
        SFR1 = Frame(window, bg='white')
        SFR1.place(x=35, y=180, width=165, height=150)
        SFR2 = Frame(window, bg='white')
        SFR2.place(x=215, y=180, width=165, height=150)
        SFR3 = Frame(window, bg='white')
        SFR3.place(x=35, y=348, width=165, height=150)
        SFR4 = Frame(window, bg='white')
        SFR4.place(x=215, y=348, width=165, height=150)

        Prodimg = PhotoImage(file='./Images/prodicon.png')
        Prodimg.photo = Prodimg
        cm = 'This is all time inventory\nproducts summary'
        Inflow = Label(SFR1, text='Products',font=('Arial', 12, 'bold'), bg='white', fg="#3C4479").place(relx=0.5, y=15, anchor=N)
        Inflow = Label(SFR1, text=" 7784",font=('Arial', 14, 'bold'), image=Prodimg, compound=LEFT, bg='white', fg="#D30E0E").place(x=5, y=45)
        Inflow = Label(SFR1, text=cm, font=('Arial', 8, 'bold'), bg='white', fg='green').place(relx=0.5, y=110, anchor=N)

        Saleimg = PhotoImage(file='./Images/salesicon.png')
        Saleimg.photo = Saleimg
        cm = 'This is all time sales\nsummary'
        Inflow = Label(SFR2, text='Sales',font=('Arial', 12, 'bold'), bg='white', fg="#3C4479").place(relx=0.5, y=15, anchor=N)
        Inflow = Label(SFR2, text=" 6539",font=('Arial', 14, 'bold'), image=Saleimg, compound=LEFT, bg='white', fg="#D30E0E").place(x=5, y=45)
        Inflow = Label(SFR2, text=cm, font=('Arial', 8, 'bold'), bg='white', fg='green').place(relx=0.5, y=110, anchor=N)

        Cusimg = PhotoImage(file='./Images/cusicon.png')
        Cusimg.photo = Cusimg
        cm = 'This is all time customers\nsummary'
        CusLab = Label(SFR3, text='Customer',font=('Arial', 12, 'bold'), bg='white', fg="#3C4479").place(relx=0.5, y=15, anchor=N)
        CusLab = Label(SFR3, text=" 684",font=('Arial', 14, 'bold'), image=Cusimg, compound=LEFT, bg='white', fg="#D30E0E").place(x=3, y=45)
        CusLab = Label(SFR3, text=cm, font=('Arial', 8, 'bold'), bg='white', fg='green').place(relx=0.5, y=110, anchor=N)

        # Cusimg = PhotoImage(file='./Images/cusicon.png')
        # Cusimg.photo = Cusimg
        # cm = 'This is all time customers\nsummary'
        # CusLab = Label(SFR4, text='Customer',font=('Arial', 12, 'bold'), bg='white', fg="#3C4479").place(relx=0.5, y=15, anchor=N)
        # CusLab = Label(SFR4, text=" 684",font=('Arial', 14, 'bold'), image=Cusimg, compound=LEFT, bg='white', fg="#D30E0E").place(x=3, y=45)
        # CusLab = Label(SFR4, text=cm, font=('Arial', 8, 'bold'), bg='white', fg='green').place(relx=0.5, y=110, anchor=N)

        # -----------------------Side Board Frames & Labels Ends-----------------------

        # -----------------------2nd Side Board Frames & Labels Begins-----------------
        S2FR = Frame(window, bg='white')
        S2FR.place(x=400, y=180, width=180, height=318)




    def home(self):
        win = Toplevel()
        home.HOME(win)
        self.window.withdraw()
        win.deiconify()
    

def dash():
    window = Tk()
    DASHBOARD(window)
    window.mainloop()


if __name__ == '__main__':
    dash()

