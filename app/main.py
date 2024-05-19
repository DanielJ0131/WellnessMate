"""Main module to launch the application."""

import os
import sys
import ctypes
from tkinter import Tk
from ui.main_ui import MainUI
from src.database import Database


def main():
    """Launch the main application."""
    db = Database()
    root = Tk()
    MainUI(root, db)

    # Setting the icon in main window and taskbar
    icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'assets', 'logo.ico'))
    if os.path.exists(icon_path):
        try:
            root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Error setting icon: {e}")
    else:
        print(f"Error: The file {icon_path} does not exist.")
    set_taskbar_icon(root, icon_path)

    root.mainloop()

def set_taskbar_icon(root, icon_path):
    """Set the taskbar icon for Windows using ctypes."""
    if sys.platform == 'win32':
        try:
            import ctypes
            icon_path = os.path.abspath(icon_path)
            if os.path.exists(icon_path):
                icon = ctypes.windll.shell32.ExtractIconW(0, icon_path, 0)
                ctypes.windll.user32.SendMessageW(root.winfo_id(), 0x80, 0, icon)
            else:
                print(f"Error: The file {icon_path} does not exist.")
        except AttributeError as e:
            print(f"Error setting taskbar icon: {e}")
    else:
        print("Taskbar icon setting is only supported on Windows.")


if __name__ == "__main__":
    main()
