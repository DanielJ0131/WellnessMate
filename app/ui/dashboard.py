"""Tkinter GUI for user dashboard."""

from tkinter import Frame, Label, Button, PhotoImage
from tkmacosx import Button

from ui.my_habits_frame import MyHabits
from ui.sport_events_frame import SportEventsFrame
from ui.discover_frame import Discover
from ui.profile_frame import ProfileFrame


class DashboardFrame(Frame):
    """Represent the user dashboard in the application."""

    def __init__(self, master, username, user_id, db, main_iu):
        """Init method for the DashboardFrame class."""
        super().__init__(master, bg="#F3F1EB")
        self.master = master
        self.username = username
        self.user_id = user_id
        self.user_image = PhotoImage(file="app/assets/" +
                                     "avatar1.png").subsample(7, 7)
        self.db = db
        self.main_ui = main_iu

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
        """Create the sidebar for the dashboard with navigation buttons."""
        # Create and add buttons to the sidebar
        self.title_label = Label(
            self.nav_frame,
            text="WellnessMate",
            font=("Helvetica", 30),
            bg="#2A2A28",
            fg="#F3F1E7",
        )
        self.title_label.grid(row=0, column=0, sticky="w", pady=(20, 30))

        self.subtitle_label = Label(
            self.nav_frame,
            text="General",
            font=("Helvetica", 14, "bold"),
            bg="#2A2A28",
            fg="#CDCBC1",
        )
        self.subtitle_label.grid(row=1, column=0, sticky="w")

        self.my_habits_button = Button(
            self.nav_frame,
            anchor="w",
            text="My Habits",
            font=("Helvetica", 16, "bold"),
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
        self.my_habits_button.grid(row=2, column=0, sticky="w")

        self.sport_events_button = Button(
            self.nav_frame,
            anchor="w",
            text="Sport Events",
            font=("Helvetica", 16, "bold"),
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
            font=("Helvetica", 16, "bold"),
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
            font=("Helvetica", 14, "bold"),
            bg="#2A2A28",
            fg="#CDCBC1",
        )
        self.subtitle_label.grid(row=5, column=0, sticky="w", pady=(30, 0))

        self.profile_button = Button(
            self.nav_frame,
            anchor="w",
            text="Profile",
            font=("Helvetica", 16, "bold"),
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
            self.user_frame, image=self.user_image, bg="#2A2A28"
        )
        self.user_image_label.grid(row=0, column=0, sticky="w", padx=(0,10))

        self.username_label = Label(
            self.user_frame,
            text=f"{self.username}",
            font=("Helvetica", 16, "bold"),
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
            font=("Helvetica", 14, "bold"),
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

    def unmount_current_frame(self):
        """Unmount frame currently displayed on the dashboard."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def mount_my_habits(self):
        """Mount the My Habits frame on the dashboard."""
        self.unmount_current_frame()
        self.my_habits_frame = MyHabits(
            self.content_frame, self.db, self.user_id, self.username
        )
        self.my_habits_frame.grid(row=0, column=1, sticky="nsew")

    def mount_discover(self):
        """Mount the My Habits frame on the dashboard."""
        self.unmount_current_frame()
        self.discover_frame = Discover(
            self.content_frame, self.db, self.user_id, self.username
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
            self.content_frame, self.db, self.user_id, self.username
        )
        self.profile_frame.grid(row=0, column=1, sticky="nsew")
    

