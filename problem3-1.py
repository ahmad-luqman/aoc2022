# read lines of characters from a file
# and print the number of characters in each line

# Open input file
inputFile = open("input3.txt", "r")

# Read input file and clean up newlines
inputFileLines = inputFile.read().splitlines()

# Create a hash table to store the priority of each priority
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
priorityTable = {}
for i in range(1, 27):
    priorityTable[chr(i+96)] = i
    priorityTable[chr(i+64)] = i+26

# # print the priority table for each item type
# for key in priorityTable:
#     print(key, priorityTable[key])

# sum of the priorities of all items in the line
sumOfPriorities = 0

# split each line into two equal length chunks
# and store the two chunks into two variables
# and find a character repeated in both chunks
for line in inputFileLines:
    # split the line into two equal length chunks
    chunk1 = line[0:len(line)//2]
    chunk2 = line[len(line)//2:]
    repeatedChar = ""

    # find the character repeated in both chunks
    for char in chunk1:
        if char in chunk2:
            repeatedChar = char
            # sum the priorities of the repeated character
            sumOfPriorities += priorityTable[repeatedChar]
            break

# print the sum of all priorities
print(sumOfPriorities)

# Close input file
inputFile.close()
