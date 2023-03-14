from tkinter import *
import sqlite3
import ast
from tkinter import messagebox
from tkinter import Menu
from PIL import ImageTk, Image
import signin



class SIGNUP:
    def __init__(self, window):
        self.window = window
        self.window.wm_iconbitmap('Images/icon.ico')
        self.window.title('Gadgets-360 | Sign Up')
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        self.window.geometry(f'{sw}x{sh}')
        # self.window.resizable(0,0)
        self.window.state('zoomed')
        self.window.configure(bg="white")

        # db
        def signupexe():
            # for Axxount License entry
            database = sqlite3.connect("gadgets.db")
            cursor = database.cursor()

            Acct = Acct_License.get()
            cursor.execute('select * from license where keypass = "%s"'%(Acct))
            y = cursor.fetchone()

            database.commit()
            database.close()

            if not FN_Entry.get() or not LN_Entry.get() or not U_Entry.get() or not CU_Entry.get() or not P_Entry.get() or not CP_Entry.get() or not Acct_License.get():
                messagebox.showerror('Invalid!', 'Field(s) cannot\nbe empty')
            elif U_Entry.get() != CU_Entry.get():
                messagebox.showerror('Invalid!', 'Username not match!')
            elif P_Entry.get() != CP_Entry.get():
                messagebox.showerror('Invalid!', 'Password not match!')
            elif not y:
                messagebox.showerror('Invalid!', 'Account License not valid!\nContact developer for support')
            else:
                database = sqlite3.connect("gadgets.db")
                cursor = database.cursor()

                usern = U_Entry.get()
                cursor.execute('select * from signup where username = "%s"'%(usern))
                x = cursor.fetchone()               
                if x:
                    messagebox.showerror('Invalid!', 'Username is used!')
                else:
                    Val = ((FN_Entry.get()), LN_Entry.get(), U_Entry.get(), CU_Entry.get(), P_Entry.get(), CP_Entry.get(), Acct_License.get())
                    cursor.executemany('insert into signup (firstname, lastname, username, c_username, password, c_password, license) values(?, ?, ?, ?, ?, ?, ?)', [Val])
                    
                    FN_Entry.delete(0, END)
                    LN_Entry.delete(0, END)
                    U_Entry.delete(0, END)
                    CU_Entry.delete(0, END)
                    P_Entry.delete(0, END)
                    CP_Entry.delete(0, END)
                    Acct_License.delete(0, END)

                    messagebox.showinfo('Great!', 'Signed Up successfully')
                    win = Toplevel()
                    signin.SIGNIN(win)
                    self.window.withdraw()
                    win.deiconify()

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
        Welc = Label(window, text='Welcome, We are glad you join us!', font=('Arial', 20, 'bold'), fg='black',bg='white')
        Welc.place(x=60, y=120)

        Login_Text = Label(window, text="Internet access is mind-free, we'll keep you safe.", font=('roboto', 11), bg='white')
        Login_Text.place(x=60, y=170)
        
        FN_Label = Label(window, text='First Name', font=('Arial', 13), bg='white')
        FN_Label.place(x=60, y=230)
        FN_Entry = Entry(window, font=('Arial', 13), bd=2, bg='white', relief='groove')
        FN_Entry.place(x=60, y=260, width=250, height=33)

        LN_Label = Label(window, text='Last Name', font=('Arial', 13), bg='white')
        LN_Label.place(x=380, y=230)
        LN_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove')
        LN_Entry.place(x=380, y=260, width=250, height=33)

        U_Label = Label(window, text='Username', font=('Arial', 13), bg='white')
        U_Label.place(x=60, y=310)
        U_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove')
        U_Entry.place(x=60, y=340, width=250, height=33)

        CU_Label = Label(window, text='Confirm Username', font=('Arial', 13), bg='white')
        CU_Label.place(x=380, y=310)
        CU_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove')
        CU_Entry.place(x=380, y=340, width=250, height=33)

        P_Label = Label(window, text='Password', font=('Arial', 13), bg='white')
        P_Label.place(x=60, y=390)
        P_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove', show='*')
        P_Entry.place(x=60, y=420, width=250, height=33)

        CP_Label = Label(window, text='Confirm Password', font=('Arial', 13), bg='white')
        CP_Label.place(x=380, y=390)
        CP_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove', show='*')
        CP_Entry.place(x=380, y=420, width=250, height=33)

        Acct_License = Label(window, text='Account Licence', font=('Arial', 13), bg='white')
        Acct_License.place(x=60, y=470)
        Acct_License = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove', show='*')
        Acct_License.place(x=60, y=500, width=190, height=33)

        # # Buttons
        SignupButton = Button(window, text='Sign up', font=('roboto', 10, 'bold'), bd=0, bg='#D30E0E', fg='white', cursor='hand2', command=signupexe)
        SignupButton.place(x=60, y=560, width=310, height=33)

        NA_Label = Label(window, text="You have an account?", font=('roboto', 10, 'bold'), bg='white')
        NA_Label.place(x=60, y=610)

        GetAcct_Button = Button(window, text='Click here', font=('roboto', 10, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2', command=self.signinpage)
        GetAcct_Button.place(x=215, y=610)

        
    def signinpage(self):
        win = Toplevel()
        signin.SIGNIN(win)
        self.window.withdraw()
        win.deiconify()

       

def SU():
    window = Tk()
    SIGNUP(window)
    window.mainloop()


if __name__ == '__main__':
    SU()




