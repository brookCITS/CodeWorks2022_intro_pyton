def getLineCount(filename):
    file = open(filename)
    lineCount = 0

    for line in file:
        lineCount=lineCount+1

    print(lineCount)

getLineCount("files/story.txt")

getLineCount("files/ipsum.txt")
