"""Login module for the application."""

from tkinter import Frame, Label, Tk, PhotoImage

# Window
windows = Tk()
windows.title("WellnessMate")
windows.resizable(0, 0)
windows.geometry("490x240+200+200")

# Frame
frame = Frame(windows, width=700, height=400, bg='black')
frame.place(x=0, y=0)

logo_image = PhotoImage(file='src/assets/logo.png')
user_label = Label(frame, text="Username", fg='white', bg='white')

windows.mainloop()
