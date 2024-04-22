from tkinter import Tk, Button, Frame
from ui.login_frame import LoginFrame
from ui.signup_frame import SignupFrame


class UserInterface:
    def __init__(self, master):
        self.master = master
        master.title("WellnessMate")
        master.geometry("1024x700")

        # Create a frame to contain the navigation buttons
        self.nav_frame = Frame(master, pady=20)
        self.nav_frame.grid(row=0, column=0, columnspan=2)

        # Create navigation buttons
        self.login_button = Button(
            self.nav_frame, text="Login", command=self.show_login_frame
        )
        self.login_button.grid(row=0, column=0, padx=10, sticky="ew")
        self.signup_button = Button(
            self.nav_frame, text="Signup", command=self.show_signup_frame
        )
        self.signup_button.grid(row=0, column=1, padx=10)

        # Create frames for login and signup
        self.login_frame = LoginFrame(master)
        self.signup_frame = SignupFrame(master)

        # Configure column 0 to expand horizontally
        master.rowconfigure(1, weight=1)
        master.columnconfigure(0, weight=1)

        # Initially show login frame
        self.show_login_frame()

    def show_login_frame(self):
        # Show login frame and hide signup frame
        self.signup_frame.grid_remove()
        self.login_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def show_signup_frame(self):
        # Show signup frame and hide login frame
        self.login_frame.grid_remove()
        self.signup_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")


if __name__ == "__main__":
    root = Tk()
    app = UserInterface(root)
    root.mainloop()
