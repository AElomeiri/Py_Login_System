import os


# Register function
def register():
    userName = input('User Name : ')
    password = input('Password : ')
    with open('passInfo.txt',
              'a') as f:  # Create a new file if it was not already exist and insert inside it the registration info.
        f.write('\n' + userName + '\n')
        f.write(password)
        f.close()
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print('''Done
            ---------------------''')


# Login function
def login():
    userName = input('User Name : ')
    password = input('Password : ')
    with open('passInfo.txt', 'r') as f:  # Open the passInfo.txt file and search for the registration info inside it.
        flag = True  # A variable to check if the operation is done or not.
        while flag:  # A While loop to loop over all contents of the file.
            un = f.readline().strip()
            pw = f.readline().strip()
            if un != '':  # To check if the content didn't over yet.
                if (un == userName) and (pw == password):
                    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                    print('Successfully Login')
                    break
            else:
                flag = False  # Change the variable value to the operation is done.

        if flag:  # To check if the operation did work and to go the new screen.
            afterLogin(un)
        else:
            print('Wrong login information')
        f.close()


# The new screen after the login
def afterLogin(username):
    print(f"Hi {username}")
    print("What do you want to do ?. \n1:Logout \n2:Delete a user")
    choice = input("You choice >> ")
    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        mainMenu()
    elif choice == '2':
        deleteUser(username)


# The function to delete a user
def deleteUser(us):
    userName = input('User Name : ')
    password = input('Password : ')
    flag = True  # A variable to check if the operation is done or not.
    with open('passInfo.txt', 'r+') as f:
        contents = f.readlines()  # To get the content of the file in a list to search for the users' info.
        for word in contents:
            if word.strip() == userName:  # To check if the username is correct.
                index = contents.index(word)
                if contents[index + 1][:-1] == password:  # To check if the password is correct.
                    del contents[index]  # Deleting the username.
                    del contents[index]  # Deleting the password.
                    flag = False  # Change the variable value to the operation is done.
                    break
        if flag:  # To check if the operation didn't work.
            print('There is no user with this Username or Password')
        else:  # Rewrite the file with the new contents.
            f.seek(0)
            f.writelines(contents)
            f.truncate()
            f.close()
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            afterLogin(us)


# This function display the main menu that tells the user the options.
def mainMenu():
    print("---Welcome---")
    print("1: Register \n2: Login \n3: Exist")
    choice = input("You choice >> ")
    if choice == '1':  # First check if the user's choice is register (1).
        register()
        mainMenu()  # Rerun the function so if the user want to register again or login.
    elif choice == '2':  # The user's choice is login (2), then the blew code well work.
        login()
    else:
        exit()


if __name__ == "__main__":
    mainMenu()
