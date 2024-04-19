"""Login module for the application."""

from tkinter import Frame, Label, Tk, PhotoImage, Entry, Button

# Window
windows = Tk()
windows.wm_title("WellnessMate")
windows.wm_iconbitmap('src/assets/wd_logo.ico')
windows.resizable(0, 0)
windows.geometry("490x300")

# Frame
frame = Frame(windows, width=700, height=400, bg='black')
frame.place(x=0, y=0)

# Username
user_image = PhotoImage(file='src/assets/user.png')
user_label = Label(frame, text="Username: ", fg='#97ffff',
                   image=user_image, compound='left', bg='black',
                   font=('Calibre', 14))
user_label.grid(row=1, column=0, padx=3, pady=20)

# Password
password_image = PhotoImage(file='src/assets/password.png')
password_label = Label(frame, text="Password: ", fg='#97ffff',
                       image=password_image, compound='left', bg='black',
                       font=('Calibre', 14))
password_label.grid(row=2, column=0, padx=3, pady=20)

# Entries
user_entry = Entry(frame, width=39, bd=3)
user_entry.grid(row=1, column=2, columnspan=2, padx=57)

password_entry = Entry(frame, width=39, bd=3, show='*')
password_entry.grid(row=2, column=2, columnspan=2)

# Login
login_button = Button(frame, text="LOGIN", bg='#7f7fff', pady=10, width=23,
                      fg='white', font=('Calibre', 14),
                      cursor='hand2', border=0, borderwidth=5)
login_button.grid(row=9, columnspan=5, pady=30)

# Create Account
noaccount_label = Label(frame, text="No account?",
                        fg='#97ffff', bg='black', font=('Calibre', 10),
                        padx=4)
noaccount_label.place(x=0, y=230)

create_button = Button(frame, text="Create Account", bg='white',
                       font=('Calibre', 8), width=15,
                       cursor='hand2', border=0)
create_button.place(x=0, y=260)

windows.mainloop()
