from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from PIL import ImageTk, Image
import setup
import signin
import inventory



class HOME:
    def __init__(self, window):
        self.window = window
        self.window.wm_iconbitmap('Images/icon.ico')
        self.window.title('Gadgets-360 | Home')
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

# '#e5dcda'
        Set_B = Button(window, text='Set up your application', font=('roboto', 10, 'bold'), bd=0, fg='#D30E0E', bg='white', cursor='hand2', command=self.setuppage)
        Set_B.place(relx=0.5, y=20, anchor=N, width=300)

        #frame
        MF = Frame(window, width=950, height=260, bg='#D30E0E')
        MF.place(relx=0.5, y=200, anchor=N)


        img1 = PhotoImage(file='./Images/dashboard.png')
        img1.photo = img1
        ADP = Button(MF, text='Dashboard', image=img1, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        ADP.place(x=45, y=30, width=200, height=200,)

        img2 = PhotoImage(file='./Images/inventory.png')
        img2.photo = img2
        Inv = Button(MF, text='Inventory', image=img2, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2', command=self.inventorypage)
        Inv.place(x=265, y=30, width=200, height=200,)

        img3 = PhotoImage(file='./Images/sales.png')
        img3.photo = img3
        Sale = Button(MF, text='Sales', image=img3, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        Sale.place(x=485, y=30, width=200, height=200,)

        img4 = PhotoImage(file='./Images/expenses.png')
        img4.photo = img4
        Exp = Button(MF, text='Expenses', image=img4, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        Exp.place(x=705, y=30, width=200, height=200,)


        Logout_B = Button(window, text='Sign Out', font=('roboto', 13, 'bold'), bd=0, fg='#D30E0E', bg='white', cursor='hand2', command=self.signinpage)
        Logout_B.place(relx=0.5, y=590, anchor=N, width=200)

        
        

    # functions
    def setuppage(self):
        win = Toplevel()
        setup.SETUP(win)
        self.window.withdraw()
        win.deiconify()

    def signinpage(self):
        win = Toplevel()
        signin.SIGNIN(win)
        self.window.withdraw()
        win.deiconify()
    
    def inventorypage(self):
        win = Toplevel()
        inventory.INVENTORY(win)
        self.window.withdraw()
        win.deiconify()

       

def home():
    window = Tk()
    HOME(window)
    window.mainloop()


if __name__ == '__main__':
    home()




