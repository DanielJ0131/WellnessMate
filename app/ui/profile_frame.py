"""This module contains the ProfileFrame class representing the user profile frame in the application."""
from tkinter import Frame, Label, Button, Entry, PhotoImage, Radiobutton, IntVar
from tkmacosx import Button
import os


class ProfileFrame(Frame):
    """Represent the user profile frame in the application."""

    def __init__(self, master, db, user_id, username, fontsize):
        """Init method for the ProfileFrame class."""
        super().__init__(master, bg="#F3F1EB", padx=70, pady=60)
        self.master = master
        self.username = username
        self.user_id = user_id
        self.db = db
        self.selected_avatar = IntVar()
        self.avatar_images = []
        self.fontsize = fontsize
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        welcome_label = Label(
            self,
            text="Profile",
            font=("Helvetica", self.fontsize["xl"], "bold"),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        welcome_label.grid(row=0, column=0, sticky="w", padx=10, pady=30)

        self.mount_profile_info()
        self.mount_avatar_frame()

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

    def mount_avatar_frame(self):
         # Change Avatar Frame
       

        for i in range(9):
            img_path = os.path.join("app", "assets", f"avatar{i}.png")
            self.avatar_images.append(PhotoImage(file=img_path).subsample(7,7))

        change_avatar_frame = Frame(self, bg="#59B2A7", pady=15, padx=35)
        change_avatar_frame.grid(row=2, column=0, sticky="nsew")
        change_avatar_frame.grid_columnconfigure(0, weight=1)
        change_avatar_frame.grid_columnconfigure(1, weight=1)
        change_avatar_frame.grid_columnconfigure(2, weight=1)
        change_avatar_frame.grid_columnconfigure(3, weight=1)
        change_avatar_frame.grid_columnconfigure(4, weight=1)


        label = Label(
            change_avatar_frame,
            text="Choose Your Avatar",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#59B2A7",
            fg="#2A2A28",
        )
        label.grid(row=0, column=0, columnspan=9, pady=(0, 20), sticky="w")

        avatar0 = Radiobutton(
                change_avatar_frame,
                image=self.avatar_images[i],
                variable=self.selected_avatar,
                value=0,
                indicatoron=False,
                bg="blue",
                selectcolor="red",
                borderwidth=0,
                highlightthickness=0,
            )
        avatar0.grid(row=2, column=0, padx=20, pady=20)
        avatar0 = Radiobutton(
                change_avatar_frame,
                image=self.avatar_images[i],
                variable=self.selected_avatar,
                value=1,
                indicatoron=False,
                bg="blue",
                selectcolor="red",
                borderwidth=0,
                highlightthickness=0,
            )
        avatar0.grid(row=2, column=1, padx=20, pady=20)
        avatar0 = Radiobutton(
                change_avatar_frame,
                image=self.avatar_images[i],
                variable=self.selected_avatar,
                value=2,
                indicatoron=False,
                bg="blue",
                selectcolor="red",
                borderwidth=0,
                highlightthickness=0,
            )
        avatar0.grid(row=2, column=2, padx=20, pady=20)
        avatar0 = Radiobutton(
                change_avatar_frame,
                image=self.avatar_images[i],
                variable=self.selected_avatar,
                value=3,
                indicatoron=False,
                bg="blue",
                selectcolor="red",
                borderwidth=0,
                highlightthickness=0,
            )
        avatar0.grid(row=2, column=3, padx=20, pady=20)


        Button(
            change_avatar_frame,
            text="Save Changes",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#45B9AC",
            fg="#FFFFFF",
        ).grid(row=5, column=0, columnspan=3, pady=20, sticky="w")
