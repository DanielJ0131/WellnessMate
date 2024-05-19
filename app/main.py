"""Main module to launch the application."""

import os
from tkinter import Tk, PhotoImage
from ui.main_ui import MainUI
from src.database import Database
from platform import system

def main():
    """Launch the main application."""
    db = Database()
    root = Tk()
    platformD = system()
    if platformD == 'Darwin':
        logo_image = 'logo.icns'
    else:
        logo_image = 'logo.ico'
    print(logo_image)


    MainUI(root, db)
    root.iconbitmap(logo_image)

    root.mainloop()


if __name__ == "__main__":
    main()
