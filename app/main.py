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
    root.iconphoto(False, PhotoImage (file='app/assets/icon.png'))

    icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'logo.ico'))

    # Check if the file exists and set the icon
    if os.path.exists(icon_path):
        try:
            root.iconbitmap(icon_path)
            print("Icon set successfully.")
        except Exception as e:
            print(f"Error setting icon: {e}")
    else:
        print(f"Error: The file {icon_path} does not exist.")
    root.mainloop()


if __name__ == "__main__":
    main()
