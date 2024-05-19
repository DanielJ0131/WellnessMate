"""Test file for the login module."""

import unittest
from tkinter import ttk
from app.ui.login_frame import LoginFrame
from app.src.database import Database
from unittest.mock import patch


def main():
    """Run the test."""
    TestLoginFrame.setUp()
    unittest.main()


class TestLoginFrame(unittest.TestCase):
    """Test class for the LoginFrame class."""

    def setUp(self):
        """Set up the TestLoginFrame."""
        # Create the database class
        self.db = Database()

        # Create login frame
        self.LoginFrame = LoginFrame(None, None, self.db, None)

    def test_LoginFrame(self):
        """Test the LoginFrame class."""
        self.assertIsInstance(self.LoginFrame, LoginFrame)

    def test_toggle_password(self):
        """Test the toggle_password method."""
        self.password_entry = ttk.Entry()
        self.show_pass_button = ttk.Button()

        # Set the password entry to show asterisks
        self.password_entry.configure(show="*")

        # Toggle the password visibility
        self.LoginFrame.toggle_password()

        # Assert that the password entry now shows plain text
        self.assertEqual(self.password_entry.get(), "")

    # Test case for successful login
    def test_successful_login(self):
        """Test the login method for successful login."""
        username = "user1"
        password = "password123"
        self.LoginFrame.user_entry.insert(0, username)
        self.LoginFrame.pass_entry.insert(0, password)
        with patch("app.ui.login_frame.messagebox.showerror"), patch(
            "app.src.database.Database.check_username_uniqueness"
        ):
            self.LoginFrame.login()
            assert (
                self.LoginFrame.user_entry.get() == "user1"
                and self.LoginFrame.pass_entry.get() == "password123"
            )

    # Test case for unsuccessful login, no username
    def test_nouser_login(self):
        """Test the login method for unsuccessful login."""
        username = ""
        password = "password123"
        self.LoginFrame.user_entry.insert(0, username)
        self.LoginFrame.pass_entry.insert(0, password)
        with patch("app.ui.login_frame.messagebox.showerror"), patch(
            "app.src.database.Database.check_username_uniqueness"
        ):
            self.LoginFrame.login()
        assert self.LoginFrame.user_entry.get() == ""
        assert self.LoginFrame.pass_entry.get() == "password123"

    # Test case for unsuccessful login, no password
    def test_nopassword_login(self):
        """Test the login method for unsuccessful login."""
        username = "user1"
        password = ""
        self.LoginFrame.user_entry.insert(0, username)
        self.LoginFrame.pass_entry.insert(0, password)
        with patch("app.ui.login_frame.messagebox.showerror"), patch(
            "app.src.database.Database.check_username_uniqueness"
        ):
            self.LoginFrame.login()
        assert self.LoginFrame.user_entry.get() == "user1"
        assert self.LoginFrame.pass_entry.get() == ""

    # Test case for unsuccessful login, no username and password
    def test_nouser_nopassword_login(self):
        """Test the login method for unsuccessful login."""
        username = ""
        password = ""
        self.LoginFrame.user_entry.insert(0, username)
        self.LoginFrame.pass_entry.insert(0, password)
        with patch("app.ui.login_frame.messagebox.showerror"), patch(
            "app.src.database.Database.check_username_uniqueness"
        ):
            self.LoginFrame.login()
        assert self.LoginFrame.user_entry.get() == ""
        assert self.LoginFrame.pass_entry.get() == ""


if __name__ == "__main__":
    main()
