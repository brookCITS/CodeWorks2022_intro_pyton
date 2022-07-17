#Emails will be stored in the this list
emails = []


#define the functions ------------------------------------------------
def send(email):
    emails.append(email)
    print("email sent")
    return emails

def printEmails():
    for email in emails:
        print("---------------------------New Email ---------------------------")
        print("From: "+email['sender'])
        print("To: "+email['reciver'])
        print("Subject: "+email['subject'])
        print(email['message'])
        print("----------------------------------------------------------------\n\n\n\n\n\n\n\n\n")


#use the Functions ------------------------------------------------

sender = "me"
reciver = "you"
subject = "Congradulations Your Code is Working!\n\n"
message = "Hello user,\n Congradulations your code seems to working perfectly.\n Just to be sure, run it again with diffirent parameters."


print(str(type(send({'sender':sender, 'reciver':reciver, 'subject':subject, 'message':message})))+"\n\n\n")

sender = "me again"
reciver = "you"
subject = "Congradulations Your Code is Working again!"
message = "Hello user,\n Congradulations your code seems to working perfectly, Again.\n Just to be extra sure, run it again with diffirent parameters."

print(str(type(send({'sender':sender, 'reciver':reciver, 'subject':subject, 'message':message})))+"\n\n\n")

printEmails()
