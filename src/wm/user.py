"""User module for the application."""


class User:
    """Represent user in the application."""

    def __init__(self, username, password, firstname, lastname, email):
        """
        Initialize a new User object.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
            firstname (str): The first name of the user.
            lastname (str): The last name of the user.
            email (str): The email address of the user.
        """
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.habits = []  # Initialize an empty list of habits for the user