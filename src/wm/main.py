from tkinter import Tk
from user_interface import UserInterface

def main():
    """Main function to launch the application."""
    root = Tk()
    app = UserInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
