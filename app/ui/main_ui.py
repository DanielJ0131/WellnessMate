"""Main UI module for WellnessMate application."""

from tkinter import Button, Frame, Label
from tkmacosx import Button

from ui.login_frame import LoginFrame
from ui.register_frame import RegisterFrame
from ui.dashboard import DashboardFrame


class MainUI:
    """Main UI class for the WellnessMate application."""

    def __init__(self, master, db):
        """Initialize the main UI for the application."""
        self.master = master
        self.db = db
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        self.font_size = {
            'xxs': int(self.screen_width / -95),
            'xs': int(self.screen_width / -85),
            's': int(self.screen_width / -75),
            'm': int(self.screen_width / -65),
            'l': int(self.screen_width / -55),
            'xl': int(self.screen_width / -40),
            'xxl': int(self.screen_width / -30),
        }
        master.title("WellnessMate")
        master.configure(bg="#F3F1EB")
        master.geometry(
            "{0}x{1}+0+0".format(
                self.screen_width, self.screen_height
            )
        )
        self.load_app()

    def load_app(self):
        """Load the application UI."""
        # Create main frames
        self.left_frame = Frame(self.master, bg="#59B2A7")
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
            font=("Helvetica", self.font_size['xxl']), bg="#59B2A7"
        )
        wellnessmate_label.grid(row=0, column=0, padx=80, pady=80, sticky="nw")

        # Add slogan label at the bottom
        slogan_text = "Track your habits,\n" \
                      "transform your life\n" \
                      "with WellnessMate."
        slogan_label = Label(
            self.left_frame,
            text=slogan_text,
            font=("Helvetica", self.font_size['m']),
            bg="#59B2A7",
            fg="#2A2A28",
            justify="left",
        )
        slogan_label.grid(row=1, column=0, padx=80, pady=150, sticky="sw")

        self.left_frame.grid_rowconfigure(1, weight=1)

        # Right frame
        # Navigation buttons (Login and Signup)
        nav_frame = Frame(self.right_frame, pady=20, bg="#F3F1EB")
        nav_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=80)

        self.right_frame.grid_columnconfigure(0, weight=1)
        nav_frame.grid_rowconfigure(1, weight=1)
        nav_frame.grid_columnconfigure(0, weight=1)
        nav_frame.grid_columnconfigure(1, weight=1)

        login_button = Button(
            nav_frame,
            text="Login",
            font=("Helvetica", self.font_size["xxs"]),
            fg="#2A2A28",
            bg="#CDCBC1",
            borderless=0,
            highlightbackground="#F3F1E6",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.show_login_frame,
        )
        login_button.grid(row=0, column=0, padx=40, sticky="e")
        register_button = Button(
            nav_frame,
            text="Sign Up",
            font=("Helvetica", self.font_size["xxs"]),
            fg="#2A2A28",
            bg="#D7D97D",
            highlightbackground="#F3F1E6",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=20,
            pady=10,
            command=self.show_register_frame,
        )
        register_button.grid(row=0, column=1, padx=40, sticky="w")

        # Login/Signup Container Frame
        container_frame = Frame(self.right_frame, pady=20, bg="#F3F1EB", padx=200)
        container_frame.grid(row=1, column=0, sticky="ew", padx=0)

        self.register_frame = RegisterFrame(container_frame, self, self.db, self.font_size)
        self.login_frame = LoginFrame(container_frame, self, self.db, self.font_size)
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
                                              user_id, db, self)
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")

    def logout(self):
        """Log out the user and show the initial frames."""
        for widget in self.master.winfo_children():
            widget.destroy()
        self.load_app()
