import re
import os
from databaseConn import DbConnection


def print_center(string):
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80  # Fallback value if terminal size cannot be determined

    padding = (terminal_width - len(string)) // 2
    print(" " * padding + string)


# To contain screens.
class Screens:
    def __init__(self):
        self.username = ""
        self.password = ""

    # To take user details input.
    def userDetails(self):
        self.username = input("Your username: ")
        self.password = input("Your password: ")

    # First screen will apper when the program start
    def mainScreen(self):
        print_center("---Welcome---")
        print("1: Register \n2: Login \n3: Exist")
        choice = input("Your choice >> ")
        if choice == '1':  # First check if the user chose to register (1).
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            self.registrationScreen()
        elif choice == '2':  # The user chose to log in (2), then the blew code well work.
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            self.logInScreen()
        elif choice == '3':  # the user chose to exist (3).
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print_center("<--Bye-->")
            exit()
        else:  # The user enter something else.
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print_center("<--Invalid input!-->")
            self.mainScreen()

    # The activity screen after successfully log in.
    def activityScreen(self):
        print_center(f"Hi {self.username}")
        print("What do you want to do ?. \n1:Modify your account. \n2:Delete your account \n3:Logout")
        choice = input("You choice >> ")
        if choice == '1':  # If the user chose to modify his/her account.
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            self.modifyScreen()
        elif choice == '2':  # If the user chose to delete his/her account.
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            self.deleteUserScreen()
        elif choice == '3':  # If the user chose to log out.
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print_center("<--You have LOGGED OUT!-->")
            self.mainScreen()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print_center("<--Invalid Input!-->")
            self.activityScreen()

    # The delete screen after the user choice to delete his account from activity screen.
    def deleteUserScreen(self):
        choice = input("Are you sure to delete your account?:(y/n)")
        if choice == "y":
            db = DbConnection(self.username)
            db.deleteUser()
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print("The account have been successfully deleted!")
            self.mainScreen()  # Return to the main screen because his account is no longer available.
        elif choice == "n":
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            self.activityScreen()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print_center("<--Invalid input!-->")
            self.deleteUserScreen()  # Return him to same screen again to late him try again.

    # The modify screen after the user choice to modify his account from activity screen.
    def modifyScreen(self):
        choice1 = input("Are you sure to modify your account?:(y/n)")
        if choice1 == "y":
            choice2 = input("""What do you want to modify?. 
1:USERNAME. 
2:PASSWORD. 
* If you want to modify both of them 
  return to activity screen and chose 'Delete your account' 
  after that register with the new delete.
Your choice: """)
            if choice2 == "1" or choice2 == "2":
                db = DbConnection(self.username)
                db.modifyUser(choice2)
                print_center("<--The account have been successfully modified!-->")
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                self.mainScreen()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                print_center("<--Invalid input!-->")
                self.modifyScreen()  # Return him to same screen again to late him try again.
        elif choice1 == "n":
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            self.activityScreen()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print_center("<--Invalid input!-->")
            self.modifyScreen()  # Return him to same screen again to late him try again.

    # Registration class.
    # This screen will apper if the user chose to register.
    def registrationScreen(self):
        pattern = r"^[a-zA-Z]+[0-9]+$"  # The correct pattern of username.
        self.userDetails()
        # To check if the username in correct length and pattern.
        if len(self.username) >= 7 and re.match(pattern, self.username):
            db = DbConnection(self.username, self.password)  # Create an instance and connection for the database.
            db.registrationChecker(
                self.registrationScreen)  # Check if the details are already in the database and if not save them in it.
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print_center("<--The registration have done successfully!-->")
            self.mainScreen()  # Return to the main screen.
        else:  # If the username isn't matching the conditions
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print_center("<--The username didn't meet the conditions!-->")
            self.registrationScreen()  # Return to Registration Screen to let the user try again.

    # Log in class
    # This screen will apper if the user chose to log in.
    def logInScreen(self):
        self.userDetails()
        db = DbConnection(self.username, self.password)  # Create an instance and connection for the database.
        if db.logInChecker():
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            self.activityScreen()  # Go to the activity screen.
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print_center("<--The username or password is wrong!-->")
            self.logInScreen()  # Return to the log in screen.


if __name__ == "__main__":
    start = Screens()
    start.mainScreen()
