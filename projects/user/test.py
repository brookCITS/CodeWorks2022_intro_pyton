import user_acct as acct

acct.loadfile()

runtest = True

while runtest:
    uInput = input("What would you like to do?\n  - Enter 1 To create a new user\n  - Enter 2 to sign in\n  - Enter 3 to change your password\n  - Enter 4 to exit code\n    Response: ")
    if uInput == "1":
        print("\nSign up\n")
        name = input("Name: ")
        email = input("Email: ")
        password1 = input("Password: ")
        password2 = input("Confirm Password: ")
        acct.createUser(name, email, password1, password2)

    elif uInput == "2":
        print("\nSign in\n")
        email = input("Email: ")
        password = input("Password: ")
        acct.signIn(email, password)

    elif uInput == "3":
        print("\nChange Password\n")
        email = input("Email: ")
        CurrentPassword = input("Current Password: ")
        newPassword = input("New Password: ")
        acct.changePassword(email, CurrentPassword, newPassword)

    elif uInput == "4":
        acct.updateFile()
        runtest = False

    else:
        print("\nInput not identified!Try again\n\n")
