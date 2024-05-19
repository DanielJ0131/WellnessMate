"""Tkinter GUI for user dashboard."""

from tkinter import Frame, Label, Button, PhotoImage
from tkmacosx import Button
import os

from ui.my_habits_frame import MyHabits
from ui.sport_events_frame import SportEventsFrame
from ui.discover_frame import Discover
from ui.profile_frame import ProfileFrame


class DashboardFrame(Frame):
    """Represent the user dashboard in the application.

    Handles the main dashboard layout, including the sidebar navigation and
    content display for various sections like
    My Habits, Sport Events, Discover, and Profile.
    """

    def __init__(self, master, username, user_id, db, main_iu, fontsize):
        """Initialize the DashboardFrame class.

        Args:
            master (Tk): The root Tkinter window.
            username (str): The username of the logged-in user.
            user_id (int): The user ID of the logged-in user.
            db (Database): The database connection object.
            main_ui (MainUI): The main UI controller for handling logout.
            fontsize (dict): A dictionary of font sizes UI elements.
        """
        super().__init__(master, bg="#F3F1EB")
        self.master = master
        self.username = username
        self.user_id = user_id
        self.fontsize = fontsize
        self.db = db
        self.main_ui = main_iu
        img_path = os.path.join("app", "assets",
                                f"avatar{db.get_user_avatar(user_id)}.png")
        self.user_image = PhotoImage(file=img_path).subsample(7, 7)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=1)

        # Create main frames
        self.nav_frame = Frame(self.master, bg="#2A2A28", padx=50, pady=30)
        self.nav_frame.grid(row=0, column=0, sticky="nswe")
        self.content_frame = Frame(self.master, bg="#F3F1E7")
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        self.create_nav()
        self.mount_my_habits()

    def create_nav(self):
        """Create the sidebar navigation with buttons for different sections.

        This method sets up the navigation sidebar with buttons for
        "My Habits", "Sport Events",
        "Discover", and "Profile".
        It also includes the application title and user info section.
        """
        # Create and add buttons to the sidebar
        self.title_label = Label(
            self.nav_frame,
            text="WellnessMate",
            font=("Helvetica", self.fontsize["xl"]),
            bg="#2A2A28",
            fg="#F3F1E7",
        )
        self.title_label.grid(row=0, column=0, sticky="w", pady=(20, 30))

        self.subtitle_label = Label(
            self.nav_frame,
            text="General",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            bg="#2A2A28",
            fg="#CDCBC1",
        )
        self.subtitle_label.grid(row=1, column=0, sticky="w")

        self.my_habits_button = Button(
            self.nav_frame,
            anchor="w",
            text="My Habits",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            fg="#F3F1E7",
            bg="#2A2A28",
            highlightbackground="#2A2A29",
            relief="flat",
            highlightthickness=0,
            borderwidth=0,
            pady=10,
            cursor="hand2",
            command=lambda: self.mount_my_habits(),
        )
        self.my_habits_button.grid(row=2, column=0, sticky="ew")

        self.sport_events_button = Button(
            self.nav_frame,
            anchor="w",
            text="Sport Events",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            fg="#F3F1E7",
            bg="#2A2A28",
            borderless=1,
            highlightbackground="#2A2A29",
            relief="flat",
            highlightthickness=0,
            borderwidth=0,
            pady=10,
            cursor="hand2",
            command=lambda: self.mount_sport_events(),
        )
        self.sport_events_button.grid(row=3, column=0, sticky="ew")

        self.discover_button = Button(
            self.nav_frame,
            anchor="w",
            text="Discover",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            fg="#F3F1E7",
            bg="#2A2A28",
            highlightbackground="#2A2A29",
            relief="flat",
            highlightthickness=0,
            borderwidth=0,
            pady=10,
            cursor="hand2",
            command=lambda: self.mount_discover(),
        )
        self.discover_button.grid(row=4, column=0, sticky="ew")

        self.subtitle_label = Label(
            self.nav_frame,
            text="Settings",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            bg="#2A2A28",
            fg="#CDCBC1",
        )
        self.subtitle_label.grid(row=5, column=0, sticky="w", pady=(30, 0))

        self.profile_button = Button(
            self.nav_frame,
            anchor="w",
            text="Profile",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            fg="#F3F1E7",
            bg="#2A2A28",
            highlightbackground="#2A2A29",
            relief="flat",
            highlightthickness=0,
            borderwidth=0,
            pady=10,
            cursor="hand2",
            command=lambda: self.mount_profile()
        )
        self.profile_button.grid(row=6, column=0, sticky="ew")

        self.nav_frame.grid_rowconfigure(7, weight=1)

        self.user_frame = Frame(self.nav_frame, bg="#2A2A28")
        self.user_frame.grid(row=8, column=0, sticky="ew")

        self.user_image_label = Label(
            self.user_frame,
            image=self.user_image,
            bg="#2A2A28"
        )
        self.user_image_label.grid(row=0, column=0, sticky="w", padx=(0, 10))

        self.username_label = Label(
            self.user_frame,
            text=f"{self.username}",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            bg="#2A2A28",
            fg="#F3F1E7",
            anchor="w"
        )
        self.username_label.grid(row=0, column=1, sticky="ew")

        self.user_frame.grid_columnconfigure(0, weight=0)
        self.user_frame.grid_columnconfigure(1, weight=1)

        self.logout_button = Button(
            self.user_frame,
            anchor="w",
            text="Log out",
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#F3F1E7",
            bg="#2A2A28",
            highlightbackground="#2A2A29",
            relief="flat",
            highlightthickness=0,
            borderwidth=0,
            pady=10,
            cursor="hand2",
            command=lambda: self.main_ui.logout(),
        )
        self.logout_button.grid(row=1, column=0, sticky="ew", columnspan=2)

    def update_dashboard_avatar(self, new_avatar):
        """Update the user's avatar on the dashboard.

        Args:
            new_avatar (int): The avatar number to update to.
        """
        img_path = os.path.join("app", "assets", f"avatar{new_avatar}.png")
        self.user_image = PhotoImage(file=img_path).subsample(7, 7)
        self.user_image_label.config(image=self.user_image)

    def update_dashboard_username(self, new_username):
        """Update the username label on the dashboard.

        Args:
            new_username (str): The new username to display.
        """
        self.username_label.config(text=new_username)
        self.username = new_username

    def unmount_current_frame(self):
        """Unmount frame currently displayed on the dashboard."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def mount_my_habits(self):
        """Mount the My Habits frame on the dashboard."""
        self.unmount_current_frame()
        self.my_habits_frame = MyHabits(
            self.content_frame, self.db, self.user_id,
            self.username, self.fontsize
        )
        self.my_habits_frame.grid(row=0, column=1, sticky="nsew")

    def mount_discover(self):
        """Mount the My Habits frame on the dashboard."""
        self.unmount_current_frame()
        self.discover_frame = Discover(
            self.content_frame, self.db, self.user_id,
            self.username, self.fontsize
        )
        self.discover_frame.grid(row=0, column=1, sticky="nsew")

    def mount_sport_events(self):
        """Mount the Sport Events frame on the dashboard."""
        self.unmount_current_frame()
        self.sport_events_frame = SportEventsFrame(self.content_frame)
        self.sport_events_frame.grid(row=1, column=1, sticky="nsew")

    def mount_profile(self):
        """Mount the Profile frame on the dashboard."""
        self.unmount_current_frame()
        self.profile_frame = ProfileFrame(
            self.content_frame, self.db, self.user_id, self.username,
            self.fontsize, self
        )
        self.profile_frame.grid(row=0, column=1, sticky="nsew")
