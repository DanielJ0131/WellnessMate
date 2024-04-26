"""Database integration methods."""
import pymysql


class Database:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = "wellnessmate1234"
        try:
            self.db = pymysql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database="wm_db"
            )
            self.create_database()  # Create database if it does not exist
            self.db.close()
            self.db = pymysql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database="wm_db"
            )
            self.create_tables()  # Create tables if they do not exist
            self.cur = self.db.cursor()
        except pymysql.Error:
            print("Error: Could not connect to database.")

    def create_database(self):
        try:
            self.cur.execute("""
                CREATE SCHEMA IF NOT EXISTS `wm_db`
                DEFAULT CHARACTER SET utf8;
            """)
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not create database.")

    def create_tables(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS `wm_db`.`login` (
                    `idlogin` INT NOT NULL AUTO_INCREMENT,
                    `user` VARCHAR(45) NOT NULL,
                    `pass` VARCHAR(45) NOT NULL,
                    PRIMARY KEY (`idlogin`),
                    UNIQUE INDEX `idlogin_UNIQUE` (`idlogin` ASC) VISIBLE,
                    UNIQUE INDEX `user_UNIQUE` (`user` ASC) VISIBLE)
                ENGINE = InnoDB;
            """)
            self.cur.execute("""
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
            """)
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not create tables.")

    def disconnect(self):
        try:
            self.db.close()
        except pymysql.Error:
            print("Error: Could not disconnect from database.")

    def query(self, query: str):
        try:
            self.cur.execute(query)
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not execute query.")

    def commit(self):
        try:
            self.db.commit()
        except pymysql.Error:
            print("Error: Could not commit changes to database.")
