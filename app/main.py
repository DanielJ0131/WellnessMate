from tkinter import Tk
from ui.main_ui import MainUI

def main():
    """Main function to launch the application."""
    root = Tk()
    MainUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()