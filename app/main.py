"""Main module to launch the application."""

import os
import sys
from tkinter import Tk
from ui.main_ui import MainUI
from src.database import Database


def main():
    """Launch the main application."""
    db = Database()
    root = Tk()
    MainUI(root, db)

    # Setting the icon in main window and taskbar
    if sys.platform == 'win32':
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 'assets', 'logo.ico'))
        try:
            root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Error setting icon: {e}")

    root.mainloop()


if __name__ == "__main__":
    main()
