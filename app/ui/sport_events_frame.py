"""Sport events module."""
from tkinter import Frame, Button, Label


class SportEventsFrame(Frame):
    """Sport event class for the application."""

    def __init__(self, master):
        """Initialize the class."""
        self.master = master
        self.create_main_container()
        self.create_widgets()

    def create_main_container(self):
        """Create the main container."""
        # Set background color
        self.container = Frame(self.master, bg="#82AACF")
        # Adjust column
        self.container.grid(row=0, column=1, sticky="news")
        self.container.grid_columnconfigure(
            1, weight=1, minsize=240
        )  # Configure column weight
        self.container.grid_rowconfigure(0, weight=0, minsize=400)  # Configure row 0 weight
        self.container.grid_rowconfigure(4, weight=1, minsize=500)  # Configure row 4 weight

    def create_widgets(self):
        """Create all widgets."""
        self.create_sporting_events_label()
        self.create_open_to_everyone_button()
        self.create_national_leagues_button()
        self.create_elites_only_button()
        # self.create_return_button()

    def create_button(self, text, command):
        """Create a button."""
        button = Button(
            self.container,
            text=text,
            bg="#1165A1",
            fg="white",
            font=("Inter", 15, "bold"),
            justify="center",
            wraplength=400,
            command=command,
            cursor="hand2",
        )
        return button

    def create_label(self, text):
        """Create a label."""
        label = Label(
            self.container,
            text=text,
            bg="#82AACF",
            fg="#F3F1E7",
            font=("Helvetica", 30, "bold"),
            justify="center",
            wraplength=550,
            cursor="arrow",
        )
        return label

    def create_sporting_events_label(self):
        """Create Sporting Events label."""
        self.sporting_events_label = self.create_label("Sporting events \
                                                        in Sweden")
        self.sporting_events_label.grid(row=0, column=0, padx=580,
                                        pady=50, sticky="n")

    def create_open_to_everyone_button(self):
        """Create Open to Everyone button."""

        self.open_to_everyone_button = self.create_button(
            "Open to everyone", self.open_to_everyone
        )
        self.open_to_everyone_button.grid(
            row=1, column=0, padx=580, pady=20, sticky="ew"
        )

    def create_national_leagues_button(self):
        """Create National Leagues button."""
        self.national_leagues_button = self.create_button(
            "National leagues, cups and tours", self.national_lct_function
        )
        self.national_leagues_button.grid(
            row=2, column=0, padx=580, pady=20, sticky="ew"
        )

    def create_elites_only_button(self):
        """Create Elites Only button."""
        self.elites_only_button = self.create_button(
            "Elites only", self.elites_only_function
        )
        self.elites_only_button.grid(row=3, column=0, padx=580,
                                     pady=20, sticky="ew")

    # def create_return_button(self):
    #     """Create Return button."""
    #     self.return_button = self.create_button("Return",
    #                                             self.return_function)
    #     self.return_button.grid(row=4, column=0, padx=580, pady=150)

    def open_to_everyone(self):
        """Display specific sport events."""
        print("Open to everyone button clicked!")

    def national_lct_function(self):
        """Display sport leagues, cups and tours."""
        print("National leagues, cups and tours button clicked!")

    def elites_only_function(self):
        """Display event on elite level."""
        print("Elites only button clicked!")

    # def return_function(self):
    #     """Return to the dashboard."""
    #     self.grid_remove()
    #     # Show the DashboardFrame again
    #     self.master.show_dashboard()
