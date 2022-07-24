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
    #your code here

def signIn(email, password):
    #your code here

def changePassword(email, CurrentPassword, newPassword):
    #your code here

def updateFile():
    #your code here
    
