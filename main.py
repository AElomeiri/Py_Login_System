
# This fun display the main menu that tells the user the options.
def mainMenu():
    print("---Welcome---")
    print("1: Register \n2: Login")
    choice = input("You choice >> ")
    # First check if the user's choice is register (1).
    if choice == '1':
        userName = input('User Name : ')
        password = input('Password : ')
        # Create a new file and name it like the username to insert inside the register info.
        fileName = userName + '.txt'
        with open(fileName, 'w') as f:
            f.write(userName + '\n')
            f.write(password)
            f.close()
        print('''Done
        ---------------------''')
        # Rerun the fun so if the user want to register again or login.
        mainMenu()
    # The user's choice is login (2), then the blew code well work.
    else:
        userName = input('User Name : ')
        password = input('Password : ')
        # Open a file which it's name like the username and search for the register info inside it.
        fileName = userName + '.txt'
        with open(fileName, 'r') as f:
            if (f.readline().strip() == userName) and (f.readline().strip() == password):
                print('Successfully Login')
            else:
                print('Wrong login information')
            f.close()


if __name__ == "__main__":
    mainMenu()
