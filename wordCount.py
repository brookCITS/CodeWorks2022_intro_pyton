par = "Hey, Nayima Sup, Sabrina Hey, Naomi Love your features With a little bit of rouge on the cheek Bronze, little bombshells, cruise by the beach Louis on the clutch, 'Boutin on the feets I'm doing too much with your dude in the sheets Now you soft like 300 count Little rubber band tuckin' 300 thou' Throw it on the floor, make 300 bounce Can you make a 16 come out 300 mouths? Cause I might have the check in the mail I might get 'em wetter like I'm underneath the sail Hungry little bunny I am coming for your tail So I can keep my mommy up and spend a hundred on the nails"
#par = "I be flying high, shawty, I be flying high I be flying high, shawty, I be flying high I be flying high, shawty, I be flying high"

#clean up the paragraph
par = par.replace(',','')
par = par.replace('\'','')
print("The paragraph: ")
print(par)

#turn the paragraph into a list of words
list = par.split(' ')

#the variable where you will store the dictionary file
myDict = dict()

#your code here
#------------------------------------#------------------------------------
#Hints:
#1) loop through the list

#2) check if the word is counted or not. if it's not counted add it to the dictionary as a new element but if it is count, update the count.

#------------------------------------#------------------------------------

#print out the dictionary
print(myDict)
