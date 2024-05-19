"""Main module to launch the application."""

import os
from tkinter import Tk, PhotoImage
from ui.main_ui import MainUI
from src.database import Database


def main():
    """Launch the main application."""
    db = Database()
    root = Tk()
    MainUI(root, db)
    root.iconphoto(False, PhotoImage (file='app/assets/logo.png'))
    root.mainloop()


if __name__ == "__main__":
    main()
