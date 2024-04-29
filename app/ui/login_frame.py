"""Tkinter GUI for user login form."""

from tkinter import Frame, Label, PhotoImage, Entry, Button, messagebox


class LoginFrame(Frame):
    """Login frame for the application."""

    def __init__(self, master, main_ui, db):
        """Init method for the LoginFrame class."""
        super().__init__(master, bg="#F3F1EB")
        self.master = master
        self.main_ui = main_ui
        self.db = db
        self.show_pass_image = PhotoImage(
            file="app/assets/" + "show_pass.png"
        ).subsample(25, 25)
        self.hide_pass_image = PhotoImage(
            file="app/assets/" + "hide_pass.png"
        ).subsample(25, 25)
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the login frame."""
        self.login_title = Label(
            self,
            text="Welcome back!",
            font=("Helvetica", 30, "bold"),
            fg="#2A2A28",
            bg="#F3F1EB",
        )
        self.login_title.grid(row=0, column=0, pady=30, sticky="w")

        # Create a frame to input the username
        self.username_frame = Frame(self, bg="#F3F1EB")
        self.username_frame.grid(row=1, column=0, sticky="ew", pady=10)
        self.username_label = Label(
            self.username_frame,
            text="Username:",
            font=("Helvetica", 14, "bold"),
            bg="#F3F1EB",
            fg="#4C4A46",
        )
        self.username_label.grid(row=0, column=0, sticky="w")
        self.user_entry = Entry(
            self.username_frame,
            width=50,
            font=("Helvetica", 16),
            fg="#4C4A46",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
        )
        self.user_entry.grid(row=1, column=0, sticky="ew", pady=5)

        # Create a frame to input the password and
        # a button to toggle password visibility
        self.pass_frame = Frame(self, bg="#F3F1EB")
        self.pass_frame.grid(row=2, column=0, sticky="ew", pady=10)
        self.pass_label = Label(
            self.pass_frame,
            text="Password:",
            font=("Helvetica", 14, "bold"),
            bg="#F3F1EB",
            fg="#4C4A46",
        )
        self.pass_label.grid(row=0, column=0, sticky="w")
        self.pass_entry = Entry(
            self.pass_frame,
            width=50,
            show="*",
            font=("Helvetica", 16),
            fg="#4C4A46",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
        )
        self.pass_entry.grid(row=1, column=0, sticky="ew", pady=5)
        self.show_pass_button = Button(
            self.pass_frame,
            image=self.show_pass_image,
            bg="#D8B7E3",
            bd=0,
            highlightbackground="#F3F1E7",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            command=self.toggle_password,
        )
        self.show_pass_button.grid(row=1, column=1, sticky="ew", padx=5)

        # Create a button to submit data
        self.submit_button = Button(
            self,
            text="Login",
            font=("Helvetica", 16, "bold"),
            fg="#2A2A28",
            bg="#45B9AC",
            highlightbackground="#F3F1E7",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.login,
        )
        self.submit_button.grid(row=3, column=0, sticky="w", pady=20)

    def toggle_password(self):
        """Toggle visibility of password in the password entry."""
        pass_state = self.pass_entry.cget("show")
        if pass_state:
            # If password is hidden, show it
            self.pass_entry.configure(show="")
            self.show_pass_button.configure(image=self.hide_pass_image)
        else:
            # If password is shown, hide it
            self.pass_entry.configure(show="*")
            self.show_pass_button.configure(image=self.show_pass_image)

    def login(self):
        """Submit the data to the database."""
        username = self.user_entry.get()
        password = self.pass_entry.get()

        # Validate input data
        if self.user_entry.get() == "":
            messagebox.showerror("Error", "Username is required!")
        elif self.pass_entry.get() == "":
            messagebox.showerror("Error", "Password is required!")
        else:
            # Check if user exists in the database
            user_exists = self.db.check_user_existance(username, password)
            if user_exists:
                user_id = self.db.get_user_id(username)
                self.main_ui.show_dashboard_frame(username, user_id, self.db)
            else:
                messagebox.showerror("Error", "Invalid username or password")
