#User account managment

users = [{'name':'default user', 'email':'email@email.com', 'password':'1234'}]

def creat_user(user_name, email, password1, password2):
    #YOUR CODE HERE
    for user in users:
        if user['email'] != email:
            if password1 == password2:
                users.append({'name':user_name, 'email':email, 'password':password1})
                print("New user added: "+user_name)
                break
            else:
                print("Password doesn't match")
        else:
            print("user already exists in list")

def get_user(email):
    #YOUR CODE HERE
    for user in users:
        if email == user['email']:
            print(user)
            break
        else:
            print("Errror: user not found")



def get_all_users():
    #YOUR CODE HERE
    email_list = []
    for user in users:
        email_list.append(user['email'])

    return email_list



creat_user('brook', 'brook@alsdkflasd.com', '1234', '1234')
emails = get_all_users()
print(emails)

#Testing the Code

## try creating three new users and print out the results

## Try adding one of the three users you added and print out the results

## Try adding a new user with passwords that don't matches and print out the results

## Get the second users print out their user name and email

## Get all users and print only their user names
