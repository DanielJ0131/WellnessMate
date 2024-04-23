"""
Tkinter GUI for user dashboard.
"""

from tkinter import Frame, Label, Button

class DashboardFrame(Frame):
    def __init__(self, master, user_info):
        super().__init__(master)
        self.master = master
        self.user_info = user_info
        self.create_sidebar()

    def create_sidebar(self):
        # Create the sidebar frame
        sidebar_frame = Frame(self, bg="green")
        sidebar_frame.grid(row=0, column=0, sticky='ns')

        # Create and add buttons to the sidebar
        self.profile_button = Button(sidebar_frame, text="Profile", bg="#444444", bd=0)
        self.profile_button.grid(row=0, column=0, sticky='ew', padx=10, pady=10)
        
        self.tasks_button = Button(sidebar_frame, text="My Habits", bg="#444444", bd=0)
        self.tasks_button.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
        
        self.sport_events_button = Button(sidebar_frame, text="Sport Events", bg="#444444", bd=0)
        self.sport_events_button.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
        
        self.discover_button = Button(sidebar_frame, text="Discover", bg="#444444", bd=0)
        self.discover_button.grid(row=3, column=0, sticky='ew', padx=10, pady=10)

        # Display user information on the right side
        welcome_label = Label(self, text=f"Welcome, {self.user_info['username']}", font=("Helvetica", 26))
        welcome_label.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        # Configure grid column weights to make the welcome message expand
        self.grid_columnconfigure(1, weight=1)

        # Configure grid row weights to make the sidebar expand vertically
        self.grid_rowconfigure(0, weight=1)
