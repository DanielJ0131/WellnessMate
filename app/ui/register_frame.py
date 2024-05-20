"""Tkinter GUI for user registration form."""

from tkinter import Frame, Label, Entry, messagebox, PhotoImage
from tkmacosx import Button


class RegisterFrame(Frame):
    """Sign up frame for the application."""

    def __init__(self, master, main_ui, db, fontsize):
        """
        Initialize the RegisterFrame.

        Parameters:
        - master: The parent widget.
        - main_ui: The main application interface.
        - db: The database connection instance.
        - fontsize: A dictionary specifying font sizes.
        """
        super().__init__(master, bg="#F3F1EB")
        self.master = master
        self.main_ui = main_ui
        self.db = db
        self.fontsize = fontsize
        self.show_pass_image = PhotoImage(
            file="app/assets/" + "show_pass.png"
        ).subsample(25, 25)
        self.hide_pass_image = PhotoImage(
            file="app/assets/" + "hide_pass.png"
        ).subsample(25, 25)
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        """Create and configure all widgets for the Register frame."""
        self.register_title = Label(
            self,
            text="Create an account",
            font=("Helvetica", self.fontsize["xl"], "bold"),
            fg="#2A2A28",
            bg="#F3F1EB",
            width=20
        )
        self.register_title.grid(row=0, column=0, pady=30, sticky="ew")

        # Username
        self.username_frame = Frame(self, bg="#F3F1EB")
        self.username_frame.grid(row=1, column=0, sticky="ew", pady=10)
        self.username_frame.grid_columnconfigure(0, weight=1)
        self.username_label = Label(
            self.username_frame,
            text="Username:",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            bg="#F3F1EB",
            fg="#4C4A46",
        )
        self.username_label.grid(row=0, column=0, sticky="w")
        self.user_entry = Entry(
            self.username_frame,
            font=("Helvetica", self.fontsize["s"]),
            fg="#4C4A46",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
        )
        self.user_entry.grid(row=1, column=0, sticky="ew", pady=5, ipady=2)

        # Password
        self.pass_frame = Frame(self, bg="#F3F1EB")
        self.pass_frame.grid(row=2, column=0, sticky="ew", pady=10)
        self.pass_frame.grid_columnconfigure(0, weight=1)
        self.pass_label = Label(
            self.pass_frame,
            text="Password:",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            bg="#F3F1EB",
            fg="#4C4A46",
        )
        self.pass_label.grid(row=0, column=0, sticky="w")
        self.pass_entry_frame = Frame(self.pass_frame, bg="#FFFFFF")
        self.pass_entry_frame.grid(row=2, column=0, sticky="ew", pady=5)
        self.pass_entry_frame.grid_columnconfigure(0, weight=1)
        self.pass_entry = Entry(
            self.pass_entry_frame,
            show="*",
            font=("Helvetica", self.fontsize["s"]),
            fg="#4C4A46",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
        )
        self.pass_entry.grid(row=0, column=0, sticky="ew", ipady=2)
        self.show_pass_button = Button(
            self.pass_entry_frame,
            image=self.show_pass_image,
            bg="#FFFFFF",
            bd=0,
            highlightbackground="#FFFFF0",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            command=self.toggle_password,
        )
        self.show_pass_button.grid(row=0, column=1, sticky="e")

        # Password confirmation
        self.pass_confirmation_frame = Frame(self, bg="#F3F1EB")
        self.pass_confirmation_frame.grid(row=3, column=0, sticky="ew",
                                          pady=10)
        self.pass_confirmation_frame.grid_columnconfigure(0, weight=1)
        self.pass_label = Label(
            self.pass_confirmation_frame,
            text="Confirm Password:",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            bg="#F3F1EB",
            fg="#4C4A46",
        )
        self.pass_label.grid(row=0, column=0, sticky="w")
        self.pass_confirmation_entry_frame = Frame(
            self.pass_confirmation_frame, bg="#FFFFFF")
        self.pass_confirmation_entry_frame.grid(row=2, column=0,
                                                sticky="ew", pady=5)
        self.pass_confirmation_entry_frame.grid_columnconfigure(0, weight=1)
        self.pass_confirmation_entry = Entry(
            self.pass_confirmation_entry_frame,
            show="*",
            font=("Helvetica", self.fontsize["s"]),
            fg="#4C4A46",
            bg="#FFFFFF",
            relief="solid",
            highlightthickness=5,
            highlightbackground="#FFFFFF",
            borderwidth=0,
            insertbackground="#4C4A46",
        )
        self.pass_confirmation_entry.grid(row=0, column=0,
                                          sticky="ew", ipady=2)
        self.show_confirm_pass_button = Button(
            self.pass_confirmation_entry_frame,
            image=self.show_pass_image,
            bg="#FFFFFF",
            bd=0,
            highlightbackground="#FFFFF0",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            command=self.toggle_confirm_password,
        )
        self.show_confirm_pass_button.grid(row=0, column=1, sticky="e")

        # Button to submit data
        self.submit_button = Button(
            self,
            text="Sign Up",
            font=("Helvetica", self.fontsize["xs"], "bold"),
            fg="#2A2A28",
            bg="#45B9AC",
            highlightbackground="#F3F1E7",
            relief="solid",
            highlightthickness=0,
            borderwidth=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.create_account,
        )
        self.submit_button.grid(row=4, column=0, sticky="w", pady=20)

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

    def toggle_confirm_password(self):
        """Toggle visibility of password in the confirm password entry."""
        pass_state = self.pass_confirmation_entry.cget("show")
        if pass_state:
            # If password is hidden, show it
            self.pass_confirmation_entry.configure(show="")
            self.show_confirm_pass_button.configure(image=self.hide_pass_image)
        else:
            # If password is shown, hide it
            self.pass_confirmation_entry.configure(show="*")
            self.show_confirm_pass_button.configure(image=self.show_pass_image)

    def create_account(self):
        """Handle the register process by validating user credentials."""
        if self.user_entry.get() == "":
            messagebox.showerror("Error", "Username is required!")
        elif self.pass_entry.get() == "":
            messagebox.showerror("Error", "Password is required!")
        elif self.pass_confirmation_entry.get() == "":
            messagebox.showerror("Error", "Confirm Password is required!")
        elif self.pass_entry.get() != self.pass_confirmation_entry.get():
            messagebox.showerror("Error", "Passwords do not match!")
        else:
            user = self.user_entry.get()
            password = self.pass_entry.get()
            user_name = self.db.check_username_uniqueness(user)
            if not user_name:
                self.db.create_account(user, password)
                messagebox.showinfo("Success", "Account created successfully!")
            else:
                messagebox.showerror("Error", "Username already exists!")
