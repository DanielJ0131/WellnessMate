"""Main module to launch the application."""
from tkinter import Tk
from ui.main_ui import MainUI


def main():
    """Launch the main application."""
    root = Tk()
    MainUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
