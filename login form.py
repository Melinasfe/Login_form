import sqlite3
from tkinter import *
from tkinter import messagebox
import database
def sign_up():
    email=email_entry.get()
    password=pass_entry.get()
    if email and password:
        if database.email_exists(email):
            messagebox.showerror('Error','This email already taken')
        else:
            database.add_user(email,password)
            messagebox.showinfo('Success','You have successfully signed up')
    else:
        messagebox.showerror('error','Important fields are empty')

def sign_in():
    email=email_entry.get()
    password=pass_entry.get()
    if email and password:
        if database.check_user(email,password):
            messagebox.showinfo('success','Welcome back')
        else:
            messagebox.showerror('error','Invalid email or password')

    else:
        messagebox.showerror('error','Important fields are empty')

    
database.create_database()

win = Tk()
win.title('Login Form')
win.geometry('400x300')

#======================widget===================================

lbl_fname=Label(win, text='Fname:', font='garamond 13')
lbl_fname.place(x=20, y=20)
lbl_lname=Label(win, text='Lname:', font='garamond 13')
lbl_lname.place(x=20, y=60)
lbl_email=Label(win, text='*Email:', font='garamond 13')
lbl_email.place(x=20, y=100)
lbl_pass=Label(win, text='*Password', font='garamond 13')
lbl_pass.place(x=20, y=140)

fname_entry=Entry(win, font='garamond 10', width=25)
fname_entry.place(x=100, y=20)
lname_entry=Entry(win, font='garamond 10', width=25)
lname_entry.place(x=100, y=60)
email_entry=Entry(win, font='garamond 10', width=25)
email_entry.place(x=100, y=100)
pass_entry=Entry(win, font='garamond 10', width=25)
pass_entry.place(x=100, y=140)

btn_signup=Button(win, text='sign up', font='garamond 10', width=9, command=sign_up)
btn_signup.place(x=90, y=190)

btn_login=Button(win, text='sign in', font='garamond 10', width=9, command=sign_in)
btn_login.place(x=200, y=190)


win.mainloop()