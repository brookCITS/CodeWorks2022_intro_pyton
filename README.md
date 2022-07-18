# Project 7 -- Functions

To open project files:
```shell
cd src/project
```

## 1 - Even numbers
Create a program that will take two inputs (start and end) and generate a list containing all the even numbers between the two inputs. ex: start = 10 and end = 20 will out put [10,12,14,16,18,20]


## 2 - Odd numbers
Create a program that will take two inputs (start and end) and generate a list containing all the odd numbers between the two inputs. ex: start = 10 and end = 20 will out put [11,13,15,17,19]


## 3 - Game
Edit game.py by adding function that let player move() (change the position value) to the left or the right (position - or + speed). The function should have inputs direction and speed, and out put the updated position.

## 4 - User Account
Create a program that will store Users in a list of dictionaries called users. Your programs need to have these functions:
- creat_user(user_name, email, password1, password2 ):
    takes four inputs (user_name, email, password1, and password2 ). This functions first checks if the email exists in users. If it already exists, return an error message stating that. if it doesn't check to see if the two passwords match. If the passwords match, add the user to the list and return a welcome message. If they don't, return an error message stating that.

- get_user(email):
    takes one input (an email) and looks for a user the matches the email input. If the user is not found, the function returns an error message. If it finds the user, it will return the user.

- get_all_users():
    Doesn't take any input but just returns the email_list


## 5 - Fibonnaci

The Fibonacci Sequence is computed based on the following formula:

fib(n)=0 if n=0
fib(n)=1 if n=1
fib(n)=fib(n-1)+fib(n-2) if n>1

Please write a program with a recursive function that compute the value of fib(n) given user input n.
