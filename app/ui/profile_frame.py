"""This module contains the ProfileFrame class representing the user profile frame in the application."""
from tkinter import Frame, Label, Button, Entry, PhotoImage, Radiobutton, IntVar, messagebox
from tkmacosx import Button
import os


class ProfileFrame(Frame):
    """Represent the user profile frame in the application."""

    def __init__(self, master, db, user_id, username, fontsize, dashboard):
        """Init method for the ProfileFrame class."""
        super().__init__(master, bg="#F3F1EB", padx=70, pady=60)
        self.master = master
        self.username = username
        self.user_id = user_id
        self.db = db
        self.selected_avatar = IntVar()
        self.avatar_images = []
        self.fontsize = fontsize
        self.dashboard = dashboard
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        welcome_label = Label(
            self,
            text="Profile",
            font=("Helvetica", self.fontsize["xl"], "bold"),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        welcome_label.grid(row=0, column=0, sticky="w", pady=30)

        self.mount_profile_info()
        self.mount_avatar_frame()

    def mount_profile_info(self):
        """Mount the profile information."""
        profile_info_frame = Frame(self, bg="#F3F1EB", pady=25, padx=35)
        profile_info_frame.grid(row=1, column=0, sticky="nsew")
        profile_info_frame.grid_columnconfigure(0, weight=1)

        label = Label(
            profile_info_frame,
            text="User Information",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        label.grid(row=0, column=0, sticky="w", pady=(0, 30))

        username_label = Label(
            profile_info_frame,
            text="Username: " + f"{self.username.capitalize()}",
            font=("Helvetica", self.fontsize["s"]),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        
        username_label.grid(row=1, column=0, sticky="w", pady=(0, 10))

        new_username_label = Label(
            profile_info_frame, 
            text="New Username:", 
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            bg="#F3F1EB", 
            fg="#2A2A28"
        )
        new_username_label.grid(row=2, column=0, sticky="w", pady=(25, 7))

        self.new_username_entry = Entry(
            profile_info_frame,
            font=("Helvetica", self.fontsize["xs"]),
            fg="#4C4A46",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
            width=50,
        )
        self.new_username_entry.grid(row=3, column=0, sticky="w")

        submit_button = Button(
            profile_info_frame, 
            text="Change Username", 
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#2A2A28",
            bg="#D7D97D",
            highlightbackground="#F3F1E0",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=5,
            pady=5,
            cursor="hand2",
            command=self.change_username
        )
        submit_button.grid(row=4, column=0, sticky="w", pady=10)

        new_password_label = Label(
            profile_info_frame, 
            text="New Password:", 
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        new_password_label.grid(row=5, column=0, sticky="w", pady=(25, 7))

        self.new_password_entry = Entry(
            profile_info_frame,
            font=("Helvetica", self.fontsize["xs"]),
            fg="#4C4A46",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
            width=50,
        )
        self.new_password_entry.grid(row=6, column=0, sticky="w")

        submit_button = Button(
            profile_info_frame, 
            text="Change Password", 
            font=("Helvetica", self.fontsize["xxs"], "bold"),
            fg="#2A2A28",
            bg="#D7D97D",
            highlightbackground="#F3F1E0",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=5,
            pady=5,
            cursor="hand2",
            command=self.change_password,
        )
        submit_button.grid(row=7, column=0, sticky="w", pady=10)

    def mount_avatar_frame(self):
         # Change Avatar Frame
        self.current_avatar = self.db.get_user_avatar(self.user_id)
        self.selected_avatar.set(self.current_avatar)

        for i in range(9):
            img_path = os.path.join("app", "assets", f"avatar{i}.png")
            self.avatar_images.append(PhotoImage(file=img_path).subsample(7,7))

        change_avatar_frame = Frame(self, bg="#F3F1EB", pady=15, padx=35)
        change_avatar_frame.grid(row=2, column=0, sticky="nsew")

        label = Label(
            change_avatar_frame,
            text="Choose Your Avatar",
            font=("Helvetica", self.fontsize["m"], "bold"),
            bg="#F3F1EB",
            fg="#2A2A28",
        )
        label.grid(row=0, column=0, columnspan=9, pady=20, sticky="w")

        for i in range(9):
            Radiobutton(
                change_avatar_frame,
                image=self.avatar_images[i],
                variable=self.selected_avatar,
                value=i,
                indicatoron=True,
                bg="#F3F1EB",
                selectcolor="#FFFFFF",
                borderwidth=0,
                highlightthickness=0,
            ).grid(row=2, column=i, padx=20, pady=20)

        Button(
            change_avatar_frame,
            text="Save Changes",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            fg="#2A2A28",
            bg="#45B9AC",
            highlightbackground="#F3F1E0",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.update_avatar
        ).grid(row=5, column=0, columnspan=3, pady=20, sticky="w")

       
    def change_username(self):
        """Change the username in the database."""
        new_username = self.new_username_entry.get()
        self.db.change_username(new_username, self.user_id)
        messagebox.showerror("Success", "Username changed successfully!")
        self.dashboard.update_dashboard_username(new_username)

    def change_password(self):
        """Change the password in the database."""
        new_password = self.new_password_entry.get()
        self.db.change_password(new_password, self.user_id)
        messagebox.showerror("Error", "Password changed successfully!")
    
    def update_avatar(self):
        """Change the password in the database."""
        new_avatar = self.selected_avatar.get()
        if new_avatar == self.current_avatar:
            messagebox.showerror("Error", "You already have that avatar selected")
        else:
            self.db.update_avatar(new_avatar, self.user_id)
            messagebox.showerror("Success", "Avatar changed successfully!")
            self.dashboard.update_dashboard_avatar(new_avatar)

    