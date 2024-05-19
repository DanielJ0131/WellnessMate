"""This module contains the ProfileFrame class representing the user profile frame in the application."""
from tkinter import Frame, Label, Button, Entry
from tkmacosx import Button


class ProfileFrame(Frame):
    """Represent the user profile frame in the application."""

    def __init__(self, master, db, user_id, username):
        """Init method for the ProfileFrame class."""
        super().__init__(master, bg="#F3F1EB", padx=70, pady=60)
        self.master = master
        self.username = username
        self.user_id = user_id
        self.db = db
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        welcome_label = Label(
            self,
            text="Profile",
            font=("Helvetica", 32),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        welcome_label.grid(row=0, column=0, sticky="w", padx=10, pady=30)

        self.mount_profile_info()

    def mount_profile_info(self):
        """Mount the profile information."""
        profile_info_frame = Frame(self, bg="#D8B7E3", pady=25, padx=25)
        profile_info_frame.grid(row=1, column=0, sticky="nsew")
        profile_info_frame.grid_columnconfigure(0, weight=1)

        label = Label(
            profile_info_frame,
            text="Profile Information",
            font=("Helvetica", 20),
            bg="#D8B7E3",
            fg="#2A2A28",
        )
        label.grid(row=0, column=0, sticky="w", pady=(0, 10))

        username_label = Label(
            profile_info_frame,
            text="Username: " + f"{self.username.capitalize()}",
            font=("Helvetica", 16),
            bg="#D8B7E3",
            fg="#2A2A28",
        )
        
        username_label.grid(row=1, column=0, sticky="w", pady=(0, 10))

        new_username_label = Label(profile_info_frame, text="New Username:", bg="#F3F1EB", fg="#2A2A28")
        new_username_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.new_username_entry = Entry(profile_info_frame)
        self.new_username_entry.grid(row=3, column=0, sticky="w", padx=10)

        submit_button = Button(profile_info_frame, text="Change Username", command=self.change_username)
        submit_button.grid(row=4, column=0, sticky="w", padx=10, pady=10)

        new_password_label = Label(profile_info_frame, text="New Password:", bg="#F3F1EB", fg="#2A2A28")
        new_password_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)

        self.new_password_entry = Entry(profile_info_frame)
        self.new_password_entry.grid(row=6, column=0, sticky="w", padx=10)

        submit_button = Button(profile_info_frame, text="Change Password", command=self.change_password)
        submit_button.grid(row=7, column=0, sticky="w", padx=10, pady=10)

    def change_username(self):
        """Change the username in the database."""
        new_username = self.new_username_entry.get()
        self.db.change_username(new_username, self.user_id)

    def change_password(self):
        """Change the password in the database."""
        new_password = self.new_password_entry.get()
        self.db.change_password(new_password, self.user_id)
