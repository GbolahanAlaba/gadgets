from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import Menu
from PIL import ImageTk, Image
import home
import home2
import signup


class SIGNIN:
    def __init__(self, window):
        self.window = window
        self.window.wm_iconbitmap('Images/icon.ico')
        self.window.title('Gadgets-360 | Sign In')
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        self.window.geometry(f'{sw}x{sh}')
        # self.window.resizable(0,0)
        self.window.state('zoomed')
        self.window.configure(bg="white")

        # Database
        
        def sign():
            uname = User_Entry.get()
            pwd = Pass_Entry.get()
            ALic = 'accessadmin1'

            database = sqlite3.connect("gadgets.db")
            cursor = database.cursor()
            cursor.execute('select * from signup where username = "%s" and password = "%s" and license = "%s"'%(uname, pwd, ALic))
            x = cursor.fetchone()

            cursor.execute('select * from signup where username = "%s" and password = "%s" and license != "%s"'%(uname, pwd, ALic))
            y = cursor.fetchone()

            if not uname or not pwd:
                messagebox.showerror('Invalid!', 'Username or Password cannot be empty')
        
            else:
                if x:
                    win = Toplevel()
                    home.HOME(win)
                    self.window.withdraw()
                    win.deiconify()
                    
                elif y:
                    win = Toplevel()
                    home2.HOME2(win)
                    self.window.withdraw()
                    win.deiconify()

                else:
                    messagebox.showerror('Invalid!', 'Incorrect Username or Password!')

            database.commit()
            database.close()

        #  Logo
        img = PhotoImage(file='./Images/logo.png')
        Logo = Label(window, image = img)
        Logo.photo = img
        Logo.place(x=45, y=10)
        Logo_Label = Label(window, text='Gadgets-360', font=('roboto', 15, 'bold'), bg='white', fg='#BC0404')
        Logo_Label.place(x=140, y=30)

        # Welcome Text
        Welc = Label(window, text='Hi, Welcome Back To Work!', font=('Arial', 20, 'bold'), fg='black',bg='white')
        Welc.place(x=60, y=120)
        
        Login_Text = Label(window, text="Internet access is mind-free, we'll keep you safe.", font=('roboto', 11), bg='white')
        Login_Text.place(x=60, y=170)
        
        User_Label = Label(window, text='Username', font=('Arial', 13), bg='white')
        User_Label.place(x=60, y=240)
        User_Entry = Entry(window, font=('Arial', 13), bd=2, bg='white', relief='groove')
        User_Entry.place(x=60, y=270, width=310, height=33)

        Pass_Label = Label(window, text='Password', font=('Arial', 13), bg='white')
        Pass_Label.place(x=60, y=313)
        Pass_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove', show='*')
        Pass_Entry.place(x=60, y=343, width=310, height=33)


        # # Buttons
        ChkButton = Checkbutton(window, text='Remember Me', cursor='hand2', bg='white')
        ChkButton.place(x=60, y=390)

        SigninButton = Button(window, text='Sign in', font=('roboto', 10, 'bold'), bd=0, bg='#D30E0E', fg='white', cursor='hand2', command=sign)
        SigninButton.place(x=60, y=440, width=310, height=33)

        NA_Label = Label(window, text="Don't have an account?", font=('roboto', 10, 'bold'), bg='white')
        NA_Label.place(x=60, y=500)

        NA_Button = Button(window, text='Click here', font=('roboto', 10, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2', command=self.signuppage)
        NA_Button.place(x=215, y=500)

        imgg = PhotoImage(file='./Images/osd.png')
        pic = Label(window, image = imgg)
        pic.photo = imgg
        pic.place(x=600, y=240)
       

        # functions   
    def signuppage(self):
        win = Toplevel()
        signup.SIGNUP(win)
        self.window.withdraw()
        win.deiconify()
    
def SI():
    window = Tk()
    SIGNIN(window)
    window.mainloop()


if __name__ == '__main__':
    SI()




