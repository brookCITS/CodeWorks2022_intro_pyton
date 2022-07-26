#your code here
from numpy import random as rand


play = True

while play:
    rm = rand.randint(11)
    guess = int(input("Guess a number between 0 and 10: "))
    while guess != rm:
        if guess > rm:
            print("your guess is bigger than the number")
        if guess < rm:
            print("your guess is smaller than the number")
        guess = int(input("Try again: "))
    print("You guessed right, the number is :"+ str(rm))
    num = input("Do you want to play again? (y|n): ")
    if num == 'n':
        play = False
