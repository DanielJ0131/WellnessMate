"""Main UI module for WellnessMate application."""
from tkinter import Button, Frame
from ui.login_frame import LoginFrame
from ui.register_frame import RegisterFrame
from ui.dashboard import DashboardFrame


class MainUI:
    """Main UI class for the WellnessMate application."""

    def __init__(self, master, db):
        """Initialize the main UI for the application."""
        self.master = master
        self.db = db
        master.title("WellnessMate")
        master.geometry("1024x700")
        self.load_app()

    def load_app(self):
        """Load the application UI."""
        # Create a frame to contain the navigation buttons
        self.nav_frame = Frame(self.master, pady=20)
        self.nav_frame.grid(row=0, column=0, columnspan=2)

        # Create navigation buttons
        login_button = Button(
            self.nav_frame, text="Login", command=self.show_login_frame
        )
        login_button.grid(row=0, column=0, padx=10, sticky="ew")
        register_button = Button(
            self.nav_frame, text="Register", command=self.show_register_frame
        )
        register_button.grid(row=0, column=1, padx=10)

        # Create frames for login, register, and dashboard
        self.login_frame = LoginFrame(self.master, self, self.db)
        self.register_frame = RegisterFrame(self.master, self)

        # Configure column 0 to expand horizontally
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)

        # Initially show login frame
        self.show_login_frame()

    def show_login_frame(self):
        """Show the login frame."""
        # Show login frame and hide signup frame
        self.register_frame.grid_remove()
        self.login_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def show_register_frame(self):
        """Show the register frame."""
        # Show register frame and hide login frame
        self.login_frame.grid_remove()
        self.register_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def show_dashboard_frame(self, user_info):
        """Show the dashboard frame."""
        # Hide login and register frames
        self.login_frame.grid_remove()
        self.register_frame.grid_remove()
        self.nav_frame.grid_remove()

        # Show dashboard frame with user_info
        self.dashboard_frame = DashboardFrame(self.master, user_info)
        self.dashboard_frame.grid(row=0, column=0, columnspan=2, rowspan=2,
                                  sticky="nsew")
