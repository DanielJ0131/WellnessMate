"""Main module for the application."""

from login import Login  # type: ignore
from registration import Registration  # type: ignore
from sport_events import SportEvents  # type: ignore


def main():
    """Is the main function of the application."""
    print("1. Login")
    print("2. Registration")
    print("3. Sport Events")
    print("4. Exit")
    choice = int(input("Enter >>> "))
    match (choice):
        case 1: Login()
        case 2: Registration()
        case 3: SportEvents()
        case 4: exit()
        case _: print("Invalid choice!")


if __name__ == "__main__":
    main()
