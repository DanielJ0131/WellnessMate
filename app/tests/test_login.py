"""Test file for the login module."""

import unittest
# GUI Mocker called TTK, tests GUI without creating one
from tkinter import ttk
from app.ui.login_frame import LoginFrame


def main():
    """Run the test."""
    TestLoginFrame.setUp()
    unittest.main()


class TestLoginFrame(unittest.TestCase):
    """Test class for the LoginFrame class."""

    def setUp(self):
        """Set up the TestLoginFrame."""
        self.LoginFrame = LoginFrame(None, None, None)

    def test_LoginFrame(self):
        """Test the LoginFrame class."""
        self.assertIsInstance(self.LoginFrame, LoginFrame)

    def test_create_widgets(self):
        """Test the create_widgets method."""
        # self.LoginFrame.create_widgets()

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

    def submit(self):
        """Test the submit method."""


if __name__ == '__main__':
    main()
