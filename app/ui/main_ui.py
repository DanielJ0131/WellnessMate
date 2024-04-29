"""Main UI module for WellnessMate application."""

from tkinter import Button, Frame, Label
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
        master.configure(bg="#F3F1EB")
        master.geometry(
            "{0}x{1}+0+0".format(
                master.winfo_screenwidth(), master.winfo_screenheight()
            )
        )
        self.load_app()

    def load_app(self):
        """Load the application UI."""
        # Create main frames
        self.left_frame = Frame(self.master, bg="#D8B7E3")
        self.left_frame.grid(row=0, column=0, sticky="nswe", rowspan=2)
        self.right_frame = Frame(self.master, bg="#F3F1E7")
        self.right_frame.grid(row=0, column=1, sticky="nswe", rowspan=2)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        # Left frame
        # Add WellnessMate label at the top
        wellnessmate_label = Label(
            self.left_frame, text="WellnessMate",
            font=("Helvetica", 60), bg="#D8B7E3"
        )
        wellnessmate_label.grid(row=0, column=0, padx=50, pady=80, sticky="ew")

        # Add slogan label at the bottom
        slogan_text = "Track your habits,\ntransform your life\nwith\
              WellnessMate."
        slogan_label = Label(
            self.left_frame,
            text=slogan_text,
            font=("Helvetica", 32),
            bg="#D8B7E3",
            fg="#2A2A28",
            justify="left",
        )
        slogan_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")

        self.left_frame.grid_rowconfigure(1, weight=1)

        # Right frame
        # Navigation buttons (Login and Signup)
        nav_frame = Frame(self.right_frame, pady=20, bg="#F3F1E7")
        nav_frame.grid(row=0, column=0, sticky="ew", padx=150)

        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        login_button = Button(
            nav_frame,
            text="Login",
            font=("Helvetica", 18),
            fg="#2A2A28",
            bg="#CDCBC1",
            highlightbackground="#F3F1E7",
            relief="solid",
            highlightthickness=0,
            bd="0",
            padx=20,
            pady=5,
            command=self.show_login_frame,
        )
        login_button.grid(row=0, column=0, padx=20)
        register_button = Button(
            nav_frame,
            text="Sign Up",
            font=("Helvetica", 18),
            fg="#2A2A28",
            bg="#D7D97D",
            highlightbackground="#F3F1E7",
            relief="solid",
            highlightthickness=0,
            bd="0",
            padx=20,
            pady=5,
            command=self.show_register_frame,
        )
        register_button.grid(row=0, column=1, padx=20)

        # Login/Signup Container Frame
        container_frame = Frame(self.right_frame, pady=20, bg="#F3F1E7")
        container_frame.grid(row=1, column=0, sticky="ew", padx=150)

        self.register_frame = RegisterFrame(container_frame, self, self.db)
        self.login_frame = LoginFrame(container_frame, self, self.db)
        self.login_frame.grid(row=0, column=0, sticky="nsew")

        container_frame.rowconfigure(1, weight=1)
        container_frame.columnconfigure(0, weight=1)

    def show_login_frame(self):
        """Show the login frame and hide signup frame."""
        self.register_frame.grid_remove()
        self.login_frame.grid(row=0, column=0, sticky="nsew")

    def show_register_frame(self):
        """Show the register frame and hide login frame."""
        self.login_frame.grid_remove()
        self.register_frame.grid(row=0, column=0, sticky="nsew")

    def show_dashboard_frame(self, username, user_id, db):
        """Hide initial frames and show the dashboard frame."""
        self.left_frame.grid_remove()
        self.right_frame.grid_remove()
        self.dashboard_frame = DashboardFrame(self.master, username,
                                              user_id, db)
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")
