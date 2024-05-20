"""Sport events module."""
# flake8: noqa E501
# Disables the "Line too Long" error for our URLs.
from tkinter import Frame, Button, Label
import tkinter as tk
import webbrowser


class SportEventsFrame(Frame):
    """Sport event class for the application."""

    def __init__(self, master):
        """Initialize the class."""
        super().__init__(master)
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
            1, weight=1, minsize=200
        )  # Configure column weight
        self.container.grid_rowconfigure(0, weight=0, minsize=300)

    def create_widgets(self):
        """Create all widgets."""
        self.create_sporting_events_label()
        self.open_to_everyone()

    def create_label(self, text):
        """Create a label."""
        label = Label(
            self.container,
            text=text,
            bg="#82AACF",
            fg="#2A2A28",
            font=("Helvetica", 25, "bold"),
            justify="center",
            wraplength=550,
        )
        return label

    def create_sporting_events_label(self):
        """Create Sporting Events label."""
        self.sporting_events_label = self.create_label(
            "Sporting Events in Sweden")
        self.sporting_events_label.grid(row=0, column=0, padx=480,
                                        pady=50, sticky="nes")

    def open_url(self, url):
        """Open URL in a web browser."""
        webbrowser.open_new(url)

    def on_enter(self, event, idx, labels):
        """Event handler for mouse entering."""
        labels[idx].config(
            fg="#F3E5AB",
            cursor="hand2",
            font=("Helvetica", 16, "bold"))

    def on_leave(self, event, idx, labels):
        """Event handler for mouse leaving."""
        labels[idx].config(
            fg="black",
            font=("Helvetica", 14, "normal"))

    def create_event_labels(
            self, events, on_enter, on_leave, open_url
            ):
        """Create labels to display the event info."""
        labels = []
        for idx, (event_text, url) in enumerate(events):
            label = tk.Label(self.container, text=event_text, bg="#82AACF",
                             font=("Helvetica", 14, "normal"))
            # label.pack(padx=10, pady=5)
            label.grid(row=idx+1, column=0, padx=2, pady=10, sticky="ew")

            label.bind("<Enter>", lambda e,
                       idx=idx: on_enter(e, idx, labels))
            label.bind("<Leave>", lambda e,
                       idx=idx: on_leave(e, idx, labels))
            label.bind("<Button-1>", lambda e,
                       url=url: open_url(url))
            labels.append(label)

        return labels

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
             "Djurgården, open for girls and women only",
             "https://tjejmilen.se/"),
        ]
        # Create and display the event window
        self.create_event_labels(
            events, self.on_enter, self.on_leave, self.open_url)
