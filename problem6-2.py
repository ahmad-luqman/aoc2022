# read a line of characters from the input file
inputFile = open("input6.txt", "r")

# read the characters into a string
inputFileLine = inputFile.readline()

# function to check if a window of 14 characters
# make a sliding window of 14 characters
# and check if the window has all unique characters
# if it does return the index of last character
# in the window


def isUniqueWindow(inputString):
    # loop through the string
    for i in range(0, len(inputString) - 13):
        # make a window of 4 characters
        window = inputString[i:i + 14]
        # check if the window has all unique characters
        if len(set(window)) == 14:
            # return the index of the last character
            # in the window
            return i + 13
    # if no unique window is found
    # return -1
    return -1

# loop through the string
# and find the first unique window
# and print the index of the last character
# in the window


for i in range(0, len(inputFileLine)):
    # make a substring from the current index
    # to the end of the string
    substring = inputFileLine[i:]
    # find the first unique window
    # and print the index of the last character
    # in the window
    index = isUniqueWindow(substring)
    if index != -1:
        print(i + index + 1)
        break

# close the input file
inputFile.close()
