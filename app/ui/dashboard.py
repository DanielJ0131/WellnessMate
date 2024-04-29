"""Tkinter GUI for user dashboard."""

from tkinter import Frame, Label, Button
from ui.my_habits_frame import MyHabits
from ui.sport_events_frame import SportEventsFrame


class DashboardFrame(Frame):
    """Represent the user dashboard in the application."""

    def __init__(self, master, username, user_id, db):
        """Init method for the DashboardFrame class."""
        super().__init__(master, bg="#F3F1EB")
        self.master = master
        self.username = username
        self.user_id = user_id
        self.db = db
        self.create_sidebar()
        print("sidebar created")
        self.mount_my_habits()

        # Configure grid column weights to make the right section
        # expand horizontally
        #self.grid_columnconfigure(0, weight=1)  # Sidebar
        #self.grid_columnconfigure(1, weight=2)  # DashBoard
        #self.grid_columnconfigure(1, weight=1)

        # Configure grid row weights to make the sidebar expand vertically
        #self.grid_rowconfigure(0, weight=1)

    def show_dashboard(self):
        """Show the dashboard frame again."""
        # Remove the sport events frame
        self.sport_events_frame.grid_remove()
        
        # Show the dashboard frame
        self.master.grid()

    def create_sidebar(self):
        """Create the sidebar for the dashboard."""
        # Create main frames
        self.nav_frame = Frame(self.master, bg="#D8B7E3")
        self.nav_frame.grid(row=0, column=0, sticky='nswe', rowspan=2)
        self.content_frame = Frame(self.master, bg="#F3F1E7")
        self.content_frame.grid(row=0, column=1, sticky='nswe', rowspan=2)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=1)

        # Create and add buttons to the sidebar

        self.my_habits_button = Button(self.nav_frame, text="My Habits", bg="#111D4A", bd=0, command=lambda:self.mount_my_habits(), cursor="hand2",
                                     fg="#CCCCCC")
        self.my_habits_button.grid(row=1, column=0, sticky='ew', padx=10, pady=10)

        self.sport_events_button = Button(self.nav_frame, text="Sport Events", bg="#111D4A", bd=0, command=lambda:self.open_sport_events, cursor="hand2",
                                     fg="#CCCCCC")
        self.sport_events_button.grid(row=2, column=0, sticky='ew', padx=10, pady=10)

        self.discover_button = Button(self.nav_frame, text="Discover", bg="#111D4A", bd=0, cursor="hand2",
                                     fg="#CCCCCC")
        self.discover_button.grid(row=3, column=0, sticky='ew', padx=10, pady=10)

        self.profile_button = Button(self.nav_frame, text="Profile", bg="#111D4A", bd=0, cursor="hand2",
                                     fg="#CCCCCC")
        self.profile_button.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

    def mount_my_habits(self):
        """Mount the My Habits frame on the dashboard."""
        # Display user information on the right side
        print("mounting habits...")
        welcome_label = Label(self.content_frame, text="Welcome, " +
                              f"{self.username}",
                              font=("Helvetica", 26))
        welcome_label.grid(row=0, column=1, sticky='ew', padx=512, pady=10)
        my_habits_frame = MyHabits(self.content_frame, self.db, self.user_id)
        my_habits_frame.grid(row=1, column=1, sticky="ew")

    def open_sport_events(self):
        """Open the Sport Events frame."""
        # Remove the dashboard frame
        self.grid_remove()

        # Instantiate the SportEventsFrame class
        self.sport_events_frame = SportEventsFrame(self.master)
                                                                     
        # Configure row and column weights of the main window
        #self.master.grid_rowconfigure(0, weight=200)

        