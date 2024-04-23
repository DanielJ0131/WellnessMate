"""
Class definition for the habit model.
"""


class Habit:
    """
    Represents a habit in the application.
    """

    def __init__(self, title, category, frequency, reminder_time=None):
        """
        Initialize a new Habit object.

        Args:
            title (str): The title of the habit.
            category (str): The category of the habit.
            frequency (str): The reminder frequency of the habit
            (e.g., daily, weekly, monthly).
            reminder_time (str, optional):
            The time of day to receive the reminder.
                Required if frequency is daily, weekly, or monthly.
                Defaults to None.
        """
        self.title = title
        self.category = category
        self.frequency = frequency
        self.reminder_time = reminder_time
        self.completed = False
