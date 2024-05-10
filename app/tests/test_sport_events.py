"""Test the SportEvents class."""

from app.ui.sport_events_frame import SportEventsFrame
import unittest


def main():
    """Run the test."""
    TestSportEventsFrame.setUp()
    unittest.main()


class TestSportEventsFrame(unittest.TestCase):
    """Test class for the SportEventsFrame class."""

    def setUp(self):
        """Set up the TestSportEventsFrame."""
        # Create sport events frame
        self.SportEventsFrame = SportEventsFrame(None)

    def test_SportEventsFrame(self):
        """Test the SportEventsFrame class."""
        self.assertIsInstance(self.SportEventsFrame, SportEventsFrame)
