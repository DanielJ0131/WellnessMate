"""Tkinter GUI for user dashboard."""

from tkinter import Frame, Label, Button, Toplevel, PhotoImage
from ui.my_habits_frame import MyHabits
from ui.sport_events_frame import SportEvents


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
        self.mount_my_habits()

    def create_sidebar(self):
        """Create the sidebar for the dashboard."""
        # Create main frames
        self.nav_frame = Frame(self.master, bg="#359C90", padx=50, pady=30)
        self.nav_frame.grid(row=0, column=0, sticky='nswe')
        self.content_frame = Frame(self.master, bg="#F3F1E7")
        self.content_frame.grid(row=0, column=1, sticky='nsew')

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=1)

        # Create and add buttons to the sidebar
        self.title_label = Label(self.nav_frame, text="WellnessMate", font=("Helvetica", 30, "bold"), bg="#359C90", fg="#F3F1E7")
        self.title_label.grid(row=0, column=0, sticky='w', padx=10, pady=20)

        self.subtitle_label = Label(self.nav_frame, text="General", font=("Helvetica", 14, "bold"), bg="#359C90", fg="#4C4A46")
        self.subtitle_label.grid(row=1, column=0, sticky='w', padx=10, pady=10)

        self.my_habits_button = Button(self.nav_frame, anchor="w", text="My Habits", font=("Helvetica", 16, "bold"), fg="#2A2A28", bg="#359C90", highlightbackground="#359C90", relief="flat", highlightthickness=0, borderwidth=0, pady=10, cursor="hand2", command=lambda:self.mount_my_habits())
        self.my_habits_button.grid(row=2, column=0, sticky='w', padx=10, pady=10)

        self.sport_events_button = Button(self.nav_frame, anchor="w", text="Sport Events", font=("Helvetica", 16, "bold"), fg="#2A2A28", bg="#359C90", highlightbackground="#359C90", relief="flat", highlightthickness=0, borderwidth=0, pady=10, cursor="hand2", command=lambda:self.open_sport_events)
        self.sport_events_button.grid(row=3, column=0, sticky='ew', padx=10, pady=10)

        self.discover_button = Button(self.nav_frame, anchor="w", text="Discover", font=("Helvetica", 16, "bold"), fg="#2A2A28", bg="#359C90", highlightbackground="#359C90", relief="flat", highlightthickness=0, borderwidth=0, pady=10, cursor="hand2")
        self.discover_button.grid(row=4, column=0, sticky='ew', padx=10, pady=10)

        self.profile_button = Button(self.nav_frame, anchor="w", text="Profile", font=("Helvetica", 16, "bold"), fg="#2A2A28", bg="#359C90", highlightbackground="#359C90", relief="flat", highlightthickness=0, borderwidth=0, pady=10, cursor="hand2")
        self.profile_button.grid(row=5, column=0, sticky='ew', padx=10, pady=10)
        
        self.nav_frame.grid_rowconfigure(6, weight=1)

        self.user_frame = Frame(self.nav_frame, bg="#359C90")
        self.user_frame.grid(row=7, column=0, sticky='w')
        self.user_image = PhotoImage(file="app/assets/" + "user_avatar.png").subsample(30, 30)
        self.user_image_label = Label(self.user_frame, image=self.user_image, bg="#359C90")
        self.user_image_label.grid(row=0, column=0, sticky='w', padx=10, pady=20)
        self.user_username_label = Label(self.user_frame, text=f"{self.username}", font=("Helvetica", 16, "bold"), bg="#359C90", fg="#F3F1E7")
        self.user_username_label.grid(row=0, column=1, sticky='w', padx=10, pady=20)


    def mount_my_habits(self):
        """Mount the My Habits frame on the dashboard."""

        my_habits_frame = MyHabits(self.content_frame, self.db, self.user_id, self.username)
        my_habits_frame.grid(row=1, column=1, sticky="nsew")
        self.content_frame.grid_columnconfigure(1, weight=1)


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
