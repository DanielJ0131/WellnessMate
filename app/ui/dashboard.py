"""Tkinter GUI for user dashboard."""

from tkinter import Frame, Label, Button, Toplevel
from ui.my_habits_frame import MyHabits
from ui.sport_events_frame import SportEvents


class DashboardFrame(Frame):
    """Represent the user dashboard in the application."""

    def __init__(self, master, user_info):
        """Init method for the DashboardFrame class."""
        super().__init__(master)
        self.master = master
        self.user_info = user_info
        self.create_sidebar()
        self.mount_my_habits()

        # Configure grid column weights to make the right section
        # expand horizontally
        self.grid_columnconfigure(1, weight=1)

        # Configure grid row weights to make the sidebar expand vertically
        self.grid_rowconfigure(0, weight=1)

    def create_sidebar(self):
        """Create the sidebar for the dashboard."""
        # Create the sidebar frame
        sidebar_frame = Frame(self, bg="#111D4A")
        sidebar_frame.grid(row=0, column=0, sticky='nswe', rowspan=2)

        # Create and add buttons to the sidebar
        self.profile_button = Button(sidebar_frame, text="Profile",
                                     bg="#111D4A", bd=0)
        self.profile_button.grid(row=0, column=0, sticky='ew',
                                 padx=10, pady=10)

        self.tasks_button = Button(sidebar_frame, text="My Habits",
                                   bg="#111D4A", bd=0)
        self.tasks_button.grid(row=1, column=0, sticky='ew', padx=10, pady=10)

        self.sport_events_button = Button(sidebar_frame, text="Sport Events",
                                          bg="#111D4A", bd=0,
                                          command=self.open_sport_events)
        self.sport_events_button.grid(row=2, column=0, sticky='ew',
                                      padx=10, pady=10)

        self.discover_button = Button(sidebar_frame, text="Discover",
                                      bg="#111D4A", bd=0)
        self.discover_button.grid(row=3, column=0, sticky='ew',
                                  padx=10, pady=10)

    def mount_my_habits(self):
        """Mount the My Habits frame on the dashboard."""
        # Display user information on the right side
        welcome_label = Label(self, text="Welcome, " +
                              f"{self.user_info['username']}",
                              font=("Helvetica", 26))
        welcome_label.grid(row=0, column=1, sticky='ew', padx=10, pady=10)

        my_habits_frame = MyHabits(self)
        my_habits_frame.grid(row=1, column=1, sticky="ew")

    def open_sport_events(self):
        """Open the Sport Events window."""
        # Create a new window for Sport Events using Toplevel
        sport_events_window = Toplevel(self)
        sport_events_window.title("Sport Events")
        sport_events_window.geometry("490x300")
        # Instantiate the SportEvents class in the new window
        SportEvents(sport_events_window)

        # Main loop for the new window
        SportEvents.mainloop()
