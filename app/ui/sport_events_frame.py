"""Sport events module."""
from tkinter import Frame, Button, Label
import tkinter as tk
import webbrowser


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
            1, weight=1, minsize=300
        )  # Configure column weight
        self.container.grid_rowconfigure(0, weight=0, minsize=400)
        self.container.grid_rowconfigure(4, weight=1, minsize=500)

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
            wraplength=500,
            command=command,
            cursor="hand2",
            width=35
        )
        return button

    def create_label(self, text):
        """Create a label."""
        label = Label(
            self.container,
            text=text,
            bg="#82AACF",
            fg="#F3F1E7",
            font=("Helvetica", 25, "bold"),
            justify="center",
            wraplength=550,
            cursor="arrow",
        )
        return label

    def create_sporting_events_label(self):
        """Create Sporting Events label."""
        self.sporting_events_label = self.create_label("Sporting Events \
                                                        in Sweden")
        self.sporting_events_label.grid(row=0, column=0, padx=480,
                                        pady=50, sticky="n")

    def create_open_to_everyone_button(self):
        """Create Open to Everyone button."""
        self.open_to_everyone_button = self.create_button(
            "Open to everyone", self.open_to_everyone
        )
        self.open_to_everyone_button.grid(
            row=1, column=0, padx=512, pady=20, sticky="ew"
        )

    def create_national_leagues_button(self):
        """Create National Leagues button."""
        self.national_leagues_button = self.create_button(
            "National leagues, cups and tours", self.national_lct_function
        )
        self.national_leagues_button.grid(
            row=2, column=0, padx=512, pady=20, sticky="ew"
        )

    def create_elites_only_button(self):
        """Create Elites Only button."""
        self.elites_only_button = self.create_button(
            "Elites only", self.elites_only_function
        )
        self.elites_only_button.grid(row=3, column=0, padx=512,
                                     pady=20, sticky="ew")

    # def create_return_button(self):
    #     """Create Return button."""
    #     self.return_button = self.create_button("Return",
    #                                             self.return_function)
    #     self.return_button.grid(row=4, column=0, padx=580, pady=150)

    def open_url(self, url):
        """Open URL in a web browser."""
        webbrowser.open_new(url)

    def on_enter(self, event, idx, labels):
        """Event handler for mouse entering."""
        labels[idx].config(
            fg="white",
            cursor="hand2",
            font=("Helvetica", 12, "bold"))

    def on_leave(self, event, idx, labels):
        """Event handler for mouse leaving."""
        labels[idx].config(
            fg="black",
            font=("Helvetica", 10, "normal"))

    def create_event_labels(
            self, window, events, on_enter, on_leave, open_url
            ):
        """Create labels to display the event info."""
        labels = []
        for idx, (event_text, url) in enumerate(events):
            label = tk.Label(window, text=event_text, bg="#82AACF")
            label.pack(padx=10, pady=5)
            label.bind("<Enter>", lambda e,
                       idx=idx: on_enter(e, idx, labels))
            label.bind("<Leave>", lambda e,
                       idx=idx: on_leave(e, idx, labels))
            label.bind("<Button-1>", lambda e,
                       url=url: open_url(url))
            labels.append(label)

        return labels

    def create_event_window(self, events, category):
        """Create and display the event window."""
        # Toplevel window
        event_window = tk.Toplevel(self.master)
        event_window.title(category)
        event_window.geometry("800x300")
        event_window.configure(bg="#82AACF")

        # Create labels for event info
        self.create_event_labels(
            event_window,
            events,
            self.on_enter,
            self.on_leave,
            self.open_url)

        # Run the Tkinter event loop for the new window
        event_window.mainloop()

    def open_to_everyone(self):
        """Display specific sport events."""
        events = [
            ("Alliansloppet - 16, 32 & 48km roller skiing event in " +
             "Trollhättan " +
             "World biggest rollerski race",
             "https://www.alliansloppet.se/"),

            ("Broloppet - Swedish/Danish road running (half marathon) event " +
             "across the Oresund Bridge",
             "https://broloppet2025.se/"),

            ("Convinistafetten - A relay race for corporate teams around " +
             "Laduviken",
             "https://stafetten.com/"),

            ("Engelbrektsloppet - 60 km cross-country skiing event in " +
             "Västmanland",
             "https://www.engelbrektsloppet.se/"),

            ("Gothia Cup - youth football tournament in Gothenburg",
             "https://gothiacup.se/sv"),

            ("Stockholm Marathon - marathon in Stockholm",
             "https://www.stockholmmarathon.se/"),

            ("Göteborgsvarvet - road running (half marathon) event in " +
             "Gothenburg",
             "https://www.goteborgsvarvet.se/"),

            ("Tjejmilen - 10 km cross country running event for women in " +
             "Djurgården, open for girls and women only" +
             "https://tjejmilen.se/"),
        ]
        print("Open to everyone button clicked!")

        # Create and display the event window
        self.create_event_window(events, category="Open sport events")

    def national_lct_function(self):
        """Display sport leagues, cups and tours."""
        events = [("Test", "https://youtu.be/dQw4w9WgXcQ?si=OFNBRuTy6UWem927"),
                  ]
        print("National leagues, cups and tours button clicked!")
        # messagebox.showinfo("National leagues, cups and tours", "test")
        # Create and display the event window
        self.create_event_window(
            events,
            category="Sport leagues, cups and tours")

    def elites_only_function(self):
        """Display event on elite level."""
        events = [("Test", "https://youtu.be/V1bFr2SWP1I?si=DBN6NGpGsXc-qcZK"),
                  ]
        print("Elites only button clicked!")
        # messagebox.showinfo("Elite Events", "test")
        # Create and display the event window
        self.create_event_window(events, category="Elite Sport Event")
