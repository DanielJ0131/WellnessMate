"""Main module for the application."""

from login import Login  # type: ignore


def main():
    """Is the main function of the application."""
    login = Login()
    login.run()


if __name__ == "__main__":
    main()
