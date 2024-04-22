"""Registration module for the application."""
from tkinter import Tk, Frame, Label, Entry, Checkbutton, Button, messagebox
import pymysql  # type: ignore


class Registration:
    """Registration class for the application."""

    def __init__(self):
        """Initialize the class."""
        # Window
        windows = Tk()
        windows.wm_title('WellnessMate')
        windows.geometry('540x300+200+10')
        windows.resizable(0, 0)

        # Frame
        frame = Frame(windows, width=610, height=640, bg='#1165A1', bd=8)
        frame.place(x=0, y=0)

        # Labels and Entry Fields
        heading = Label(frame, text='Account Creation', fg='#97ffff',
                        bg='#1165A1', font=('Calibre', 20, 'bold'))
        heading.place(x=150, y=3)

        # User
        user_label = Label(frame, text='Username: ', fg='#97ffff',
                           bg='#1165A1', font=('Calibre', 14))
        user_label.place(x=20, y=70)

        user_entry = Entry(frame, width=30, borderwidth=2)
        user_entry.place(x=200, y=75)

        # Pass
        pass_label = Label(frame, text='Password: ', fg='#97ffff',
                           bg='#1165A1', font=('Calibre', 14))
        pass_label.place(x=20, y=100)

        pass_entry = Entry(frame, width=30, borderwidth=2)
        pass_entry.place(x=200, y=105)

        # Confirm Pass
        confirm_pass_label = Label(frame, text='Confirm Password: ',
                                   fg='#97ffff', bg='#1165A1',
                                   font=('Calibre', 14))
        confirm_pass_label.place(x=20, y=130)
        confirm_pass_entry = Entry(frame, width=30, borderwidth=2)
        confirm_pass_entry.place(x=200, y=135)

        # Database Section
        def submit():
            """Submit the data to the database."""
            if user_entry.get() == '':
                messagebox.showerror('Error', 'Username is required!')
            elif pass_entry.get() == '':
                messagebox.showerror('Error', 'Password is required!')
            elif confirm_pass_entry.get() == '':
                messagebox.showerror('Error', 'Confirm Password is required!')
            elif pass_entry.get() != confirm_pass_entry.get():
                messagebox.showerror('Error', 'Passwords do not match!')
            else:
                db = pymysql.connect(host='localhost',
                                     user='root', password='wellnessmate1234')
                try:
                    cur = db.cursor()
                    query = 'CREATE DATABASE wm_db'
                    cur.execute(query)
                    query = 'USE wm_db'
                    cur.execute(query)
                    query = 'CREATE TABLE login(ID INT AUTO_INCREMENT ' \
                            'PRIMARY KEY NOT NULL, user VARCHAR(45), ' \
                            'pass VARCHAR(45), ' \
                            'UNIQUE KEY wellnessmate1234 (user));'
                    cur.execute(query)
                    messagebox.showinfo('Success',
                                        'Fields created successfully!')

                except Exception:
                    cur.execute('USE wm_db')
                    query = 'INSERT INTO login(user, pass) values(%s, %s)'
                    cur.execute(query, (user_entry.get(), pass_entry.get()))
                    db.commit()
                    db.close()
                    messagebox.showinfo('Success',
                                        'Account created successfully!')

        def show_pass1():
            """Show the password."""
            pass_entry.configure(show='')
            check_button_1.configure(command=hide_pass1)

        def hide_pass1():
            """Hides the password."""
            pass_entry.configure(show='*')
            check_button_1.configure(command=show_pass1)

        def show_pass2():
            """Show the confirmed password."""
            confirm_pass_entry.configure(show='')
            check_button_2.configure(command=hide_pass2)

        def hide_pass2():
            """Hides the confirm password."""
            confirm_pass_entry.configure(show='*')
            check_button_2.configure(command=show_pass2)

        pass_entry.configure(show='*')
        confirm_pass_entry.configure(show='*')
        check_button_1 = Checkbutton(frame, text='', bg='#1165A1',
                                     command=show_pass1)
        check_button_1.place(x=390, y=105)

        check_button_2 = Checkbutton(frame, text='', bg='#1165A1',
                                     command=show_pass2)
        check_button_2.place(x=390, y=135)

        submit_button = Button(frame, text='Submit', bg='white',
                               width=15, borderwidth=5, height=2,
                               command=submit)
        submit_button.place(x=200, y=200)

        # Cancel Button
        cancel_button = Button(frame, text='<<', bg='white',
                               width=2, borderwidth=5, height=1,
                               cursor='hand2')
        cancel_button.place(x=10, y=250)

        windows.mainloop()
