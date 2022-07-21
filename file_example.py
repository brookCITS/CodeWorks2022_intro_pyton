#read from python
#1
ipsum_file = open(“files/ipsum.txt”)
for line in ipsum_file:
    print(line)
    #print(line.rstrip())

#2
#ipsum_file.seek(0)
#lines = ipsum_file.readlines()
#print(lines)

#3
#with open("files/ipsum.txt") as ipsum_file:
#    line = ipsum_file.readlines()
#    print(line)


#write to python
#1
#with open('files/write.txt', 'w') as file:
#    file.write("I love Python so much\n")
#    file.write("I really love Python soooooooo much")


#with open('files/write.txt', 'w') as file:
#    file.write("\nI dream about python sometimes!")


#2
#quotes = [
#    '\npeace',
#    '\nlove',
#    '\nand rock n roll'
#]
#with open('files/write.txt', 'a') as file:
#    file.write("\nI dream about python sometimes!")
