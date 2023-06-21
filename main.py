# Register fun
def register():
    userName = input('User Name : ')
    password = input('Password : ')
    with open('passInfo.txt', 'a') as f:  # Create a new file if it was not already exist and insert inside it the registration info.
        f.write('\n' + userName + '\n')
        f.write(password)
        f.close()
    print('''Done
            ---------------------''')


# Login fun
def login():
    userName = input('User Name : ')
    password = input('Password : ')
    with open('passInfo.txt', 'r') as f:  # Open the passInfo.txt file and search for the registration info inside it.
        flag = True
        while flag: # A While loop to loop over all contents of the file.
            buffer = f.readline()
            if buffer != '':
                if (buffer.strip() == userName) and (f.readline().strip() == password):
                    print('Successfully Login')
                    break
            else:
                flag = False

        if not flag:
            print('Wrong login information')
        f.close()


# This fun display the main menu that tells the user the options.
def mainMenu():
    print("---Welcome---")
    print("1: Register \n2: Login \n3: Exist")
    choice = input("You choice >> ")
    if choice == '1':  # First check if the user's choice is register (1).
        register()
        mainMenu()  # Rerun the fun so if the user want to register again or login.
    elif choice == '2':  # The user's choice is login (2), then the blew code well work.
        login()
    else:
        exit()


if __name__ == "__main__":
    mainMenu()
