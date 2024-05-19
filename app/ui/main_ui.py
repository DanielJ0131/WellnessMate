"""Main UI module for WellnessMate application."""

from tkinter import Button, Frame, Label
from tkmacosx import Button

from ui.login_frame import LoginFrame
from ui.register_frame import RegisterFrame
from ui.dashboard import DashboardFrame


class MainUI:
    """Main UI class for the WellnessMate application."""

    def __init__(self, master, db):
        """
        Initialize the main UI for the WellnessMate application.

        Parameters:
        - master: The root window or parent widget.
        - db: The database connection instance.
        """
        self.master = master
        self.db = db
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        self.font_size = {
            'xxs': int(self.screen_width / -110),
            'xs': int(self.screen_width / -100),
            's': int(self.screen_width / -90),
            'm': int(self.screen_width / -75),
            'l': int(self.screen_width / -60),
            'xl': int(self.screen_width / -50),
            'xxl': int(self.screen_width / -30),
        }
        master.title("WellnessMate")
        master.configure(bg="#F3F1EB")
        master.geometry(
            "{0}x{1}+0+0".format(
                self.screen_width, self.screen_height
            )
        )
        master.state('zoomed')
        self.load_app()

    def load_app(self):
        """
        Load the application UI.

        This method sets up the main frames, labels, and buttons for the
        WellnessMate application's initial interface.
        """
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
            font=("Helvetica", self.font_size['xl']),
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
            font=("Helvetica", self.font_size["xs"]),
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
            font=("Helvetica", self.font_size["xs"]),
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
        container_frame = Frame(self.right_frame, pady=20,
                                bg="#F3F1EB", padx=200)
        container_frame.grid(row=1, column=0, sticky="ew", padx=0)

        self.register_frame = RegisterFrame(container_frame, self, self.db,
                                            self.font_size)
        self.login_frame = LoginFrame(container_frame, self, self.db,
                                      self.font_size)
        self.login_frame.grid(row=0, column=0, sticky="nsew")

        container_frame.rowconfigure(1, weight=1)
        container_frame.columnconfigure(0, weight=1)

    def show_login_frame(self):
        """Display the login frame and hide register frame."""
        self.register_frame.grid_remove()
        self.login_frame.grid(row=0, column=0, sticky="nsew")

    def show_register_frame(self):
        """Dislay the register frame and hide login frame."""
        self.login_frame.grid_remove()
        self.register_frame.grid(row=0, column=0, sticky="nsew")

    def show_dashboard_frame(self, username, user_id, db):
        """
        Display the dashboard frame and hide the initial frames.

        Parameters:
        - username: The username of the logged-in user.
        - user_id: The user ID of the logged-in user.
        - db: The database connection instance.
        """
        self.left_frame.grid_remove()
        self.right_frame.grid_remove()
        self.dashboard_frame = DashboardFrame(self.master, username,
                                              user_id, db, self,
                                              self.font_size)
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")

    def logout(self):
        """Log out the user and show the login and register frames."""
        for widget in self.master.winfo_children():
            widget.destroy()
        self.load_app()
