"""Login module for the application."""

from tkinter import Frame, Label, Tk, PhotoImage

# Window
windows = Tk()
windows.wm_title("WellnessMate")
windows.wm_iconbitmap('src/assets/wd_logo.ico')
windows.resizable(0, 0)
windows.geometry("490x240+200+200")

# Frame
frame = Frame(windows, width=700, height=400, bg='black')
frame.place(x=0, y=0)

users_image = PhotoImage(file='src/assets/users.png')
user_label = Label(frame, text="Username: ", fg='#97ffff',
                   image=users_image, compound='left', bg='black',
                   font=('Calibre', 14))
user_label.grid(row=1, column=0, padx=3, pady=20)

windows.mainloop()
