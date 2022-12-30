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

# sum of all priorities
sumOfPriorities = 0

# read each 3 line of input file and find repeating character
# in all 3 lines
for i in range(0, len(inputFileLines), 3):
    # Get 3 lines of input file
    line1 = inputFileLines[i]
    line2 = inputFileLines[i+1]
    line3 = inputFileLines[i+2]
    # Get the repeating character in all 3 lines
    repeatingChar = ""
    for char in line1:
        if char in line2 and char in line3:
            repeatingChar = char
            break
    # Get the priority of the repeating character
    priority = priorityTable[repeatingChar]
    # Print the priority of the repeating character
    print(priority)
    # Add the priority to the sum of all priorities
    sumOfPriorities += priority

# Print the sum of all priorities
print("Sum of all priorities: " + str(sumOfPriorities))

# Close input file
inputFile.close()
