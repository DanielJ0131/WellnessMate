"""Registration module for the application."""
from tkinter import Tk, Frame, Label, Entry, Checkbutton, Button


class Registration:
    """Registration class for the application."""
    def __init__(self):
        """Initializes the class."""
        # Window
        windows = Tk()
        windows.wm_title('WellnessMate')
        windows.geometry('540x300+200+10')
        windows.resizable(0, 0)

        # Frame
        frame = Frame(windows, width=610, height=640, bg='black', bd=8)
        frame.place(x=0, y=0)

        # Labels and Entry Fields
        heading = Label(frame, text='Account Creation', fg='#97ffff',
                        bg='black', font=('Calibre', 20, 'bold'))
        heading.place(x=150, y=3)

        # User
        user_label = Label(frame, text='Username: ', fg='#97ffff',
                           bg='black', font=('Calibre', 14))
        user_label.place(x=20, y=70)

        user_entry = Entry(frame, width=30, borderwidth=2)
        user_entry.place(x=200, y=75)

        # Pass
        pass_label = Label(frame, text='Password: ', fg='#97ffff',
                           bg='black', font=('Calibre', 14))
        pass_label.place(x=20, y=100)

        pass_entry = Entry(frame, width=30, borderwidth=2)
        pass_entry.place(x=200, y=105)

        # Confirm Pass
        confirm_pass_label = Label(frame, text='Confirm Password: ',
                                   fg='#97ffff', bg='black',
                                   font=('Calibre', 14))
        confirm_pass_label.place(x=20, y=130)
        confirm_pass_entry = Entry(frame, width=30, borderwidth=2)
        confirm_pass_entry.place(x=200, y=135)

        def show_pass1():
            """Shows the password."""
            pass_entry.configure(show='')
            check_button_1.configure(command=hide_pass1)

        def hide_pass1():
            """Hides the password."""
            pass_entry.configure(show='*')
            check_button_1.configure(command=show_pass1)

        def show_pass2():
            """Shows the confirm password."""
            confirm_pass_entry.configure(show='')
            check_button_2.configure(command=hide_pass2)

        def hide_pass2():
            """Hides the confirm password."""
            confirm_pass_entry.configure(show='*')
            check_button_2.configure(command=show_pass2)

        pass_entry.configure(show='*')
        confirm_pass_entry.configure(show='*')
        check_button_1 = Checkbutton(frame, text='', bg='black',
                                     command=show_pass1)
        check_button_1.place(x=390, y=105)

        check_button_2 = Checkbutton(frame, text='', bg='black',
                                     command=show_pass2)
        check_button_2.place(x=390, y=135)

        # Submit Button
        submit_button = Button(frame, text='Submit', bg='#7f7fff',
                               width=15, borderwidth=5, height=2)
        submit_button.place(x=200, y=200)

        # Cancel Button
        cancel_button = Button(frame, text='<<', bg='white',
                               width=2, borderwidth=5, height=1,
                               cursor='hand2')
        cancel_button.place(x=10, y=250)

        windows.mainloop()
