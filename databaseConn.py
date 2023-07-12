import os
import sqlite3


def print_center(string):
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(string)) // 2
    print(" " * padding + string)


# To check matching in the database.
def check(rows, item, n):
    for row in rows:
        if row[n] == item:
            return False
    return True


class DbConnection:
    # Establish a connection to the database.
    def __init__(self, username, password=""):
        self.username = username
        self.password = password

        # Connect to the database
        self.connection = sqlite3.connect('database.db')

        # Create a cursor object
        self.cursor = self.connection.cursor()

        # Create a table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')

    # Insert data into the table
    def insertData(self):
        self.cursor.execute(f"INSERT INTO users (username, password) VALUES ('{self.username}', '{self.password}')")

    # Modify user's account's detail in the database by his/her id.
    def updateData(self, column_name, new_value, current_username):
        self.cursor.execute(f"UPDATE users SET {column_name} = '{new_value}' WHERE username = '{current_username}';")

    # Delete user's account from the database by his/her username.
    def deleteUser(self):
        self.cursor.execute(f"DELETE FROM users WHERE username = '{self.username}';")
        self.closeConn()

    # Check if the details are already in the database and if not save them in it.
    def registrationChecker(self, register_screen):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        flag1 = check(rows, self.username, 1)  # To check the username.
        flag2 = check(rows, self.password, 2)  # To check the password.

        if flag1 and flag2:  # If the details aren't used, save them.
            self.insertData()
            self.closeConn()  # Commit the changes and close the connection
        else:
            if not flag1 and not flag2:  # If both of them are used.
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                print_center(f"<--The password '{self.username}' is already exist!-->")
                print_center(f"<--The username '{self.password}' is already exist!-->")
                self.closeConn()  # Commit the changes and close the connection
                register_screen()  # Return to the registration screen.
            elif not flag1 and flag2:  # If the username is used only.
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                print_center(f"<--The username '{self.username}' is already exist!-->")
                self.closeConn()  # Commit the changes and close the connection
                register_screen()  # Return to the registration screen.
            elif not flag2 and flag1:  # If the password is used only.
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                print_center(f"<--The password '{self.password}' is already exist!-->")
                self.closeConn()  # Commit the changes and close the connection
                register_screen()  # Return to the registration screen.

    # Check if the login details are exist or not in the database.
    def logInChecker(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        flag1 = check(rows, self.username, 1)  # To check the username.
        flag2 = check(rows, self.password, 2)  # To check the password.

        if not flag1 and not flag2:  # If the details are exist.
            self.closeConn()  # Close the database connection.
            return True
        else:
            self.closeConn()  # Close the database connection.
            return False

    # Modify user's account's details by his/her choice.
    def modifyUser(self, choice):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        if choice == "1":  # If the user choice to modify the username,
            newUsername = input("Your new username: ")
            if check(rows, newUsername, 1):
                self.updateData("username", newUsername, self.username)
                self.closeConn()  # Close the database connection.
            else:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                print_center("<--The new username is used!-->")
                self.modifyUser(choice)
        elif choice == "2":  # If the user choice to modify the password.
            newPassword = input("Your new password: ")
            if check(rows, newPassword, 2):
                self.updateData("password", newPassword, self.username)
                self.closeConn()  # Close the database connection.
            else:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                print_center("<--The new password is used!-->")
                self.modifyUser(choice)

    # Commit the changes and close the connection
    def closeConn(self):
        self.connection.commit()
        self.connection.close()
