password = "Password123"
trial = 3

while trial > 0:
    user_password = input("Please enter your password: ")
    if user_password == password:
        print("Welcome User")
        break

    else:
        print("Error: Password incorect")
        trial = trial - 1
