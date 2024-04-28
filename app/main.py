"""Main module to launch the application."""
from tkinter import Tk
from ui.main_ui import MainUI
from src.database import Database


def main():
    """Launch the main application."""
    db = Database()
    root = Tk()
    MainUI(root, db)
    root.mainloop()


if __name__ == "__main__":
    main()
