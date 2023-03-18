from tkinter import *
from datetime import *
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from PIL import ImageTk, Image
import home



class INVENTORY:
    def __init__(self, window):
        self.window = window
        self.window.wm_iconbitmap('Images/icon.ico')
        self.window.title('Gadgets-360 | Add New Stock')
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

        
        Title = Label(window, text='Add New | Inventory', font=('roboto', 13, 'bold'), bg='white', fg='#D30E0E')
        Title.place(x=220, y=15)

        Home_B = Button(window, text='Back', font=('roboto', 12, 'bold'), bd=0, bg='#D30E0E', fg='white', cursor='hand2', command=self.homepage)
        Home_B.place(x=1270, y=20, anchor=N, width=100)

        LBF = LabelFrame(window, text="", width=1100, height=600)
        LBF.place(x=220, y=50)

        SideMenu = Frame(window, bg="#3C4479")
        SideMenu.place(x=0, y=0, width=200, height=720)
        
        img1 = PhotoImage(file='./Images/plus.png')
        img1.photo = img1
        Add_New = Button(SideMenu, text='  Add New Product', image=img1, compound=LEFT, font=('roboto', 10, 'bold'), bg="#3C4479", fg="white", bd=0, cursor='hand2')
        Add_New.place(x=10, y=30)

        img2 = PhotoImage(file='./Images/products.png')
        img2.photo = img2
        All_Prod = Button(SideMenu, text='  All Products', image=img2, compound=LEFT, font=('roboto', 10, 'bold'), bg="#3C4479", fg="white", bd=0, cursor='hand2')
        All_Prod.place(x=10, y=80)

        img3 = PhotoImage(file='./Images/apple.png')
        img3.photo = img3
        Iphones = Button(SideMenu, text='  Iphones', image=img3, compound=LEFT, font=('roboto', 10, 'bold'), bg="#3C4479", fg="white", bd=0, cursor='hand2')
        Iphones.place(x=10, y=130)

        img4 = PhotoImage(file='./Images/samsung.png')
        img4.photo = img4
        Samsung = Button(SideMenu, text='  Samsung', image=img4, compound=LEFT, font=('roboto', 10, 'bold'), bg="#3C4479", fg="white", bd=0, cursor='hand2')
        Samsung.place(x=10, y=180)

        img5 = PhotoImage(file='./Images/gadgets.png')
        img5.photo = img5
        Gadgets = Button(SideMenu, text='  Gadgets', image=img5, compound=LEFT, font=('roboto', 10, 'bold'), bg="#3C4479", fg="white", bd=0, cursor='hand2')
        Gadgets.place(x=10, y=230)

        img6 = PhotoImage(file='./Images/damage.png')
        img6.photo = img6
        Damages = Button(SideMenu, text='  Damages', image=img6, compound=LEFT, font=('roboto', 10, 'bold'), bg="#3C4479", fg="white", bd=0, cursor='hand2')
        Damages.place(x=10, y=280)

        List = [
            'None',
            'Samsung',
            'Apple',
            'Others'
        ]
            

        BrandCat = Label(LBF, text='Product Brand', font=('Arial', 11, 'bold'))
        BrandCat.place(x=30, y=30)

        BCatCombo = ttk.Combobox(LBF, value=List)
        BCatCombo.current(0)
        BCatCombo.bind('<<<ComboboxSelected>>>')
        BCatCombo.place(x=180, y=32)

        List2 = [
            'None',
            'New',
            'Used',
            'Returned']

        Condition = Label(LBF, text='Product Condition', font=('Arial', 11, 'bold'))
        Condition.place(x=370, y=30)

        CatCombo = ttk.Combobox(LBF, value=List2)
        CatCombo.current(0)
        CatCombo.bind('<<<ComboboxSelected>>>')
        CatCombo.place(x=530, y=32)

        List3 = [
            'None',
            'China',
            'Dubai']

        Region = Label(LBF, text='Region', font=('Arial', 11, 'bold'))
        Region.place(x=710, y=30)

        RegCombo = ttk.Combobox(LBF, value=List3)
        RegCombo.current(0)
        RegCombo.bind('<<<ComboboxSelected>>>')
        RegCombo.place(x=790, y=32)


        def updatelist(data):
            MyList.delete(0, END)
            for item in data:
                MyList.insert(END, item)

        def fillout(event):
            Item_Entry.delete(0, END)
            Item_Entry.insert(0, MyList.get(ACTIVE))

        def check(event):
            typed = Item_Entry.get()
            if typed == '':
                data = ML
            
            else:
                data = []
                for item in ML:
                    if typed.lower() in item.lower():
                        data.append(item)

            
            updatelist(data)


        Item = Label(LBF, text='Item', font=('Arial', 11, 'bold'))
        Item.place(x=30, y=95)
        Item_Entry = Entry(LBF, font=('roboto', 11), bd=2, relief='groove')
        Item_Entry.place(x=30, y=125, width=200, height=27)

        MyList = Listbox(LBF, width=33, height=10)
        MyList.place(x=30, y=165)

        ML = [
            'Samsung S8',
            'Samsung S8+',
            'Samsung S9',
            'Samsung S9+',
            'Samsung S10',
            'Samsung S10+',
            'Samsung Note 8',
            'Samsung Note 9']

        updatelist(ML)
        MyList.bind("<<ListboxSelect>>", fillout)
        Item_Entry.bind("<KeyRelease>", check)


        IMEI = Label(LBF, text='IMEI Number', font=('Arial', 11, 'bold'))
        IMEI.place(x=265, y=95)
        IMEI_Entry = Entry(LBF, font=('roboto', 11), bd=2, relief='groove')
        IMEI_Entry.place(x=265, y=125, width=200, height=27)

        UnitPri = Label(LBF, text='Unit Price', font=('Arial', 11, 'bold'))
        UnitPri.place(x=500, y=95)
        UnitPri_Entry = Entry(LBF, font=('roboto', 11, 'bold'), bd=2, relief='groove')
        UnitPri_Entry.place(x=500, y=125, width=100, height=27)

        Date = Label(LBF, text='Date', font=('roboto', 11, 'bold'))
        Date.place(x=640, y=95)
        Date_Entry = DateEntry(LBF, selectmode='month')
        Date_Entry.place(x=640, y=125)

        Butt = Button(LBF, text='Add New Stock', font=('Arial', 11, 'bold'), bd=0, bg='#D30E0E', fg='white', cursor='hand2')
        Butt.place(x=575, y=249, width=130, height=23)



    def homepage(self):
        win = Toplevel()
        home.HOME(win)
        self.window.withdraw()
        win.deiconify()
    
       

def dash():
    window = Tk()
    INVENTORY(window)
    window.mainloop()


if __name__ == '__main__':
    dash()





