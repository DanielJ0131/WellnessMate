"""Tkinter GUI for user registration form."""

from tkinter import Frame, Label, Entry, Button, messagebox, PhotoImage
import pymysql


class RegisterFrame(Frame):
    """Sign up frame for the application."""

    def __init__(self, master, main_ui, db):
        """Init method for the RegisterFrame class."""
        super().__init__(master, bg="#82AACF")
        self.master = master
        self.main_ui = main_ui
        self.db = db
        self.show_pass_image = PhotoImage(file="app/assets/" +
                                          "show_pass.png").subsample(
            25, 25
        )
        self.hide_pass_image = PhotoImage(file="app/assets/" +
                                          "hide_pass.png").subsample(
            25, 25
        )
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the sign up frame."""
        Label(self, text="Sign Up", font=("Helvetica", 26),
              bg="#82AACF").pack(pady=20)

        # Create a frame to input the username
        self.username_frame = Frame(self, bg="#82AACF")
        self.username_frame.pack(pady=20, padx=10)

        Label(self.username_frame, text="Username:",
              bg="#82AACF").pack(side="left")
        self.user_entry = Entry(self.username_frame, width=30)
        self.user_entry.pack(side="left", padx=10)

        # Create a frame to input the password
        self.pass_frame = Frame(self, bg="#82AACF")
        self.pass_frame.pack(pady=5, padx=10)

        Label(self.pass_frame, text="Password:",
              bg="#82AACF").pack(side="left")
        self.pass_entry = Entry(self.pass_frame, width=30, show="*")
        self.pass_entry.pack(side="left", padx=10)

        # Create a button to toggle password visibility
        self.show_pass_button = Button(
            self.pass_frame,
            image=self.show_pass_image,
            bg="#82AACF",
            bd=0,
            command=self.toggle_password,
        )
        self.show_pass_button.pack(side="left", padx=5)

        # Create a frame to input the confirmed password
        self.confirm_pass_frame = Frame(self, bg="#82AACF")
        self.confirm_pass_frame.pack(pady=20, padx=10)

        Label(self.confirm_pass_frame,
              text="Confirm Password:", bg="#82AACF").pack(
            side="left"
        )
        self.confirm_pass_entry = Entry(self.confirm_pass_frame,
                                        width=30, show="*")
        self.confirm_pass_entry.pack(side="left", padx=10)

        # Create a button to toggle password visibility
        self.show_confirm_pass_button = Button(
            self.confirm_pass_frame,
            image=self.show_pass_image,
            bg="#82AACF",
            bd=0,
            command=self.toggle_confirm_password,
        )
        self.show_confirm_pass_button.pack(side="left", padx=5)

        # Create a button to submit data
        self.submit_button = Button(
            self,
            text="Submit",
            bg="white",
            width=15,
            borderwidth=1,
            height=2,
            command=self.create_account,
        )
        self.submit_button.pack(pady=10)

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
        pass_state = self.confirm_pass_entry.cget("show")
        if pass_state:
            # If password is hidden, show it
            self.confirm_pass_entry.configure(show="")
            self.show_confirm_pass_button.configure(image=self.hide_pass_image)
        else:
            # If password is shown, hide it
            self.confirm_pass_entry.configure(show="*")
            self.show_confirm_pass_button.configure(image=self.show_pass_image)

    def create_account(self):
        """Submit the data to the database."""
        if self.user_entry.get() == "":
            messagebox.showerror("Error", "Username is required!")
        elif self.pass_entry.get() == "":
            messagebox.showerror("Error", "Password is required!")
        elif self.confirm_pass_entry.get() == "":
            messagebox.showerror("Error", "Confirm Password is required!")
        elif self.pass_entry.get() != self.confirm_pass_entry.get():
            messagebox.showerror("Error", "Passwords do not match!")
        else:
            try:
                user = self.user_entry.get()
                password = self.pass_entry.get()
                user_name = self.db.check_username_uniqueness(user)
                if not user_name:
                    self.db.create_account(user, password)
                    messagebox.showinfo("Success",
                                        "Account created successfully!")
                else:
                    messagebox.showerror("Error", "Username already exists!")
            except pymysql.Error:
                print("Error: Could not create account.")
