# Project 11 -- Modules

## Guess the number

Edit the file guess.py and create a python code that imports the 'random' module from the numpy library and asks users to guess the value of a randomly generated integer (if you haven't installed the numpy library yet, please install it now)
  - generate and save a random number as variable 'rm'
  - ask the user to input an integer
  - if the input is less than or greater than the random number, let the user know
  - if the input matches the random number, print out a congratulations message as the user if they want to play again. based on the response, exit or play the game again (wrap your code in a while loop)


## User Account Management

Create a python module named user_acct which opens 'users.json' and saves it as a dictionary of dictionaries and into a variable called users. It should also have the following functions:
  - createUser(): it has inputs name, email, password1, password2. If the email is not in the dictionary and the two passwords match it will save the into users

  ```shell
  #add new user to dictionary
  user.update({
    'user1@email.com': {
      'name': 'user1',
      'password': 'Password'
    }
  })

  ```

  - signIn(): has inputs email and password. Tries to match the email and password with a user in the dictionary. If there is a match, it will print out a welcome message and returns True. Otherwise, it will print out an error message and returns False (don't forget to close the file).

  - changePassword(): has inputs email, CurrentPassword, and newPassword. It calls the signIn() function and passes the email and CurrentPassword. If True is returned, it will update user's password in the dictionary and print's out a confirmation message. Otherwise, it will print out an error message

  - updateFile(): has no inputs. It will overwrite 'users.json' file by saving the dictionary into it.

  - run the test.py file and do the following:
    1) add two new users and close the program
    2) try to sign in using the two users you just created then close the program
    3) try to update both user's passwords
