"""Unit tests for database integration."""

import unittest
from app.src.database import Database


def main():
    """Run the test."""
    TestDatabase.setUp()
    unittest.main()


class TestDatabase(unittest.TestCase):
    """Test class for the Database class."""

    def setUp(self):
        """Set up the TestDatabase."""
        self.db = Database()

    def test_Database(self):
        """Test the Database class."""
        self.assertIsInstance(self.db, Database)

    def test_create_database(self):
        """Test the create_database method."""
        self.db.drop_database()
        self.db.create_database()

    def test_create_tables(self):
        """Test the create_tables method."""
        self.db.create_tables()

    def test_disconnect(self):
        """Test the disconnect method."""
        self.db.disconnect()

    def test_query(self):
        """Test the query method."""
        self.db.query("SELECT * FROM login")

    def test_check_user_existance(self):
        """Test the check_user_existance method."""
        self.db.check_user_existance("test", "test")

    def test_check_username(self):
        """Test the check_username method."""
        self.db.check_username_uniqueness("test")

    def test_create_account(self):
        """Test the create_account method."""
        self.db.create_account("test", "test")

    def test_delete_account(self):
        """Test the delete_account method."""
        self.db.delete_account("test")

    def test_drop_database(self):
        """Test the drop_database method."""
        self.db.drop_database()

    def test_commit(self):
        """Test the commit method."""
        self.db.commit()


if __name__ == "__main__":
    main()
