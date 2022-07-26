import json

users = {}

def loadfile():
    try:
        with open("users.json") as file:
            jsonString = json.load(file)
            print(jsonString)
            users.update(jsonString)
            print("File loaded to program")
            print(users)
    except:
        print("File could not be found")


def createUser(name, email, password1, password2):
    #does the email already exist?
    if email not in users:
        #Do the passwords match?
        if password1 == password2:
            users.update(
                {
                    email:{
                        'name':name,
                        'password': password1
                    }
                }
            )
            print("Welcome "+name+"!\n\n")
        else:
            print("Error: the passwords do not match\n\n")
    else:
        print("Error: user with this email already exist\n\n")

def signIn(email, password):
    #your code here
    if email in users and users[email]['password'] == password:
        print("Welcome "+users[email]['name']+"\n\n")
        return True
    else:
        print("Error: Incorrect login info, try again\n\n")
        return False
def changePassword(email, CurrentPassword, newPassword):
    #your code here
    if signIn(email, CurrentPassword):
        users[email]['password'] = newPassword
        print("Your password was updated succesfuly\n\n")

def updateFile():
    #your code here
    with open("users.json", 'w') as file:
        jsonString = json.dump(users, file)
