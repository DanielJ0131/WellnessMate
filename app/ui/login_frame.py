"""Tkinter GUI for user login form."""

from tkinter import Frame, Label, PhotoImage, Entry, Button, messagebox


class LoginFrame(Frame):
    """Login frame for the application."""

    def __init__(self, master, main_ui, db):
        """Init method for the LoginFrame class."""
        super().__init__(master, bg="#82AACF")
        self.master = master
        self.main_ui = main_ui
        self.db = db
        self.show_pass_image = PhotoImage(file="app/assets/" +
                                          "show_pass.png").subsample(25, 25)
        self.hide_pass_image = PhotoImage(file="app/assets/" +
                                          "hide_pass.png").subsample(25, 25)
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the login frame."""
        # Add login form elements here
        Label(self, text="Login", font=("Helvetica", 26),
              bg="#82AACF").pack(pady=20)

        # Create a frame to input the username
        self.username_frame = Frame(self, bg="#82AACF")
        self.username_frame.pack(pady=10)

        Label(self.username_frame, text="Username:",
              bg="#82AACF").pack(side="left")
        self.user_entry = Entry(self.username_frame, width=30)
        self.user_entry.pack(side="left", padx=10)

        # Create a frame to input the password
        self.pass_frame = Frame(self, bg="#82AACF")
        self.pass_frame.pack(pady=10)

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

        # Create a button to submit data
        self.submit_button = Button(
            self,
            text="Login",
            bg="white",
            width=15,
            borderwidth=1,
            height=2,
            cursor="hand2",
            command=self.submit,
        )
        self.submit_button.pack(pady=20)

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

    def submit(self):
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
            user = self.db.check_user_existance(username,password)
            if user:
                messagebox.showinfo("Success", "Login successful!")
                self.main_ui.show_dashboard_frame({'username': username})
                # Call a method in the main application to load the
                # dashboard frame, for example:
                # self.master.load_dashboard_frame()
            else:
                messagebox.showerror("Error", "Invalid username or password")
