par = ''
file = open("files/paragraph.txt")
for line in file:
    par = par+line

par = par.replace(',','')
par = par.replace('\'','')

#turn the paragraph into a list of words
list = par.split(' ')

#the variable where you will store the dictionary file
myDict = dict()

for word in list:
    if word not in myDict:
        myDict.update({ word : 1 })
    else:
        myDict[word] = myDict[word] + 1


print(myDict)

with open("files/wordcount.txt", 'w') as file:
    file.writelines(str(myDict))

#your code
