run_code = True

#define the Functions
def getArea(length, width):
    return length*width

def getVolume(length, width, height):
    return length*width*height


#run the code
while run_code:
    choice = int(input("What would you like to do?\n Enter 1 to calculate area\n 2 to calculate volume\n3 to exit.\nChoice: "))
    if choice == 1:
        #get user input
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        #call getArea finction
        area = getArea(length, width)

        print(area)

    elif choice ==2:
        #get user input
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        height = int(input("Enter the height: "))
        #call getVolume finction
        volume = getVolume(length, width, height)

        print(volume)

    elif choice == 3:
        print("Good bye!")
        #set boolean to False and exit while loop
        run_code = False

    else:
        print("Sorry! Invalid input!\nPlease try again!")
