def factorial(number):

    #base case
    if(number == 1):
        return 1
    #recursive
    elif(number > 1):
        return number * factorial(number-1)

my_number = int(input("Enter an intiger greater than zero: "))

print(factorial(my_number))
