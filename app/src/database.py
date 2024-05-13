"""Database integration methods."""

import pymysql


class Database:
    """Database class to interact with the database."""

    def __init__(self):
        """Initialize the database connection."""
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "hyT9mon#"
        try:
            self.server = pymysql.connect(
                host=self.__host, user=self.__user, password=self.__password
            )
            self.create_database()  # Create database if it does not exist
            self.server.close()
            self.db = pymysql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database="wm_db",
            )
            self.cur = self.db.cursor()
            self.create_tables()  # Create tables if they do not exist
        except pymysql.Error:
            print("Error: Could not connect to database.")

    def create_database(self):
        """Create the database if it does not exist."""
        try:
            self.server.cursor().execute(
                """
                CREATE SCHEMA IF NOT EXISTS `wm_db`
                DEFAULT CHARACTER SET utf8;
            """
            )
            self.server.commit()
        except pymysql.Error:
            print("Error: Could not create database.")

    def create_tables(self):
        """Create tables in the database."""
        try:
            self.cur.execute(
                """
                CREATE TABLE IF NOT EXISTS `wm_db`.`login` (
                    `idlogin` INT NOT NULL AUTO_INCREMENT,
                    `user` VARCHAR(45) NOT NULL,
                    `pass` VARCHAR(45) NOT NULL,
                    PRIMARY KEY (`idlogin`),
                    UNIQUE INDEX `idlogin_UNIQUE` (`idlogin` ASC) VISIBLE,
                    UNIQUE INDEX `user_UNIQUE` (`user` ASC) VISIBLE)
                ENGINE = InnoDB;
            """
            )
            self.cur.execute(
                """
                CREATE TABLE IF NOT EXISTS `wm_db`.`habit` (
                    `idhabit` INT NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(45) NOT NULL,
                    `frequency` INT NOT NULL,
                    `login_idlogin` INT NOT NULL,
                    PRIMARY KEY (`idhabit`, `login_idlogin`),
                    UNIQUE INDEX `idhabit_UNIQUE` (`idhabit` ASC) VISIBLE,
                    INDEX `fk_habit_login1_idx` (`login_idlogin` ASC) VISIBLE,
                    UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
                    CONSTRAINT `fk_habit_login1`
                        FOREIGN KEY (`login_idlogin`)
                        REFERENCES `wm_db`.`login` (`idlogin`)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION)
                ENGINE = InnoDB;
            """
            )
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not create tables.")

    def disconnect(self):
        """Disconnect from the database."""
        try:
            self.db.close()
        except pymysql.Error:
            print("Error: Could not disconnect from database.")

    def query(self, query: str):
        """Execute a query on the database."""
        try:
            self.cur.execute(query)
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not execute query.")

    def check_user_existance(self, username, password):
        """Check if the user exists in the database."""
        try:
            self.cur.execute(
                "SELECT * FROM login WHERE " + "user = %s AND pass = %s",
                (username, password),
            )
            self.db.commit()
            return self.cur.fetchone()

        except pymysql.Error:
            print("Error: Could not check user existence query.")

    def check_username_uniqueness(self, username):
        """Check if the username already exists in the database."""
        try:
            self.cur.execute("SELECT * FROM login WHERE user=%s", (username))
            self.db.commit()
            result = self.cur.fetchone()
            if result:
                return True
            else:
                return False
        except pymysql.Error:
            print("Error: Could not check username.")

    def create_account(self, username, password):
        """Create a new account in the database."""
        try:
            self.cur.execute(
                "INSERT INTO login(user, pass) values(%s, %s)",
                (username, password)
            )
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not create account.")

    def get_user_id(self, username):
        """Get the user ID from the database."""
        try:
            self.cur.execute("SELECT idlogin FROM login WHERE user=%s",
                             (username))
            self.db.commit()
            return self.cur.fetchone()[0]
        except pymysql.Error:
            print("Error: Could not get user ID.")

    def get_habits(self, user_id):
        """Get habits from the database."""
        try:
            self.cur.execute("SELECT name FROM habit WHERE login_idlogin=%s",
                             (user_id))
            self.db.commit()
            return self.cur.fetchall()
        except pymysql.Error:
            print("Error: Could not get habits from user.")

    def add_habit(self, habit_name, user_id):
        """Add a habit to the database."""
        try:
            self.cur.execute(
                "INSERT INTO habit(name, frequency,"
                + "login_idlogin) values(%s, %s, %s)",
                (habit_name, 0, user_id),
            )
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not add habit to the database.")

    def delete_habit(self, habit_name):
        """Delete a habit from the database."""
        try:
            self.cur.execute("DELETE FROM habit WHERE name=%s", (habit_name))
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not delete habit from the database.")

    def edit_habit(self, habit_id, habit_name):
        """Edit a habit in the database."""
        try:
            self.cur.execute(
                "UPDATE habit SET name=%s WHERE idhabit=%s",
                (habit_name, habit_id)
            )
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not update habit in the database.")

    def commit(self):
        """Commit changes to the database."""
        try:
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not commit changes to database.")

    # Function 1 to delete account to test the database in test_database.py
    def delete_account(self, username):
        """Delete an account from the database."""
        try:
            self.cur.execute("DELETE FROM login WHERE user=%s", (username))
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not delete account.")

    # Function 2 to drop database to test the database in test_database.py
    def drop_database(self):
        """Drop the database."""
        try:
            self.server.cursor().execute("DROP DATABASE IF EXISTS wm_db")
            self.server.commit()
        except pymysql.Error:
            print("Error: Could not drop database.")
