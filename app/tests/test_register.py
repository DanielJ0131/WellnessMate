"""Test file for the register module."""

import unittest
from app.ui.register_frame import RegisterFrame


def main():
    """Run the test."""
    TestRegisterFrame.setUp()
    unittest.main()


class TestRegisterFrame(unittest.TestCase):
    """Test class for the RegisterFrame class."""

    def setUp(self):
        """Set up the TestRegisterFrame."""
        self.RegisterFrame = RegisterFrame(None, None, None)

    def test_RegisterFrame(self):
        """Test the RegisterFrame class."""
        self.assertIsInstance(self.RegisterFrame, RegisterFrame)

    def test_create_widgets(self):
        """Test the create_widgets method."""

    def test_toggle_password(self):
        """Test the toggle_password method."""

    def test_toggle_confirm_password(self):
        """Test the toggle_confirm_password method."""

    def test_create_account(self):
        """Test the create_account method."""

    def test_submit(self):
        """Test the submit method."""


if __name__ == '__main__':
    main()
