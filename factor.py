range = range(0,50)
numbers = []
list = []

for num in range:
    numbers.append(num)
    if num % 7 == 0 and num % 5 != 0:
        list.append(num)

print(list)
print(numbers)
