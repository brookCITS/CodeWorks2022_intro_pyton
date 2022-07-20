list = []
def fib(n):
    #base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    #recursive case
    if n > 1:
        return fib(n-1) + fib(n-2)

for i in range(11):
       print(fib(i))
