# read all lines
# separate the lines by newline only

# read lines of characters from a file
# inputFile = open("input5-debug.txt", "r")
inputFile = open("input5.txt", "r")

# Read input file and clean up newlines
inputFileLines = inputFile.readlines()

# variables to hold stack and move commands lines
stackLines = []
moveLines = []
isStackFound = False

# loop through each line until the end of line character only
for line in inputFileLines:
    if line == "\n":
        print("End of line")
        isStackFound = True
    else:
        if isStackFound:
            moveLines.append(line)
        else:
            stackLines.append(line)

# read the number of rows by counting the number of lines
# and subtracting 1 for the last line
numOfRows = len(stackLines) - 1
# read the last line of stackLines
# parse the line to read the last number
# that is the number of columns
numOfColumns = int(stackLines[numOfRows].split(" ")[-2])

# print the number of rows and columns
print("Number of rows: " + str(numOfRows))
print("Number of columns: " + str(numOfColumns))

# construct the array of stacks
stacks = []
# initialize the stacks array with empty arrays
for i in range(0, numOfColumns):
    stacks.append([])

# by reading the stackLines from back to front
for i in range(numOfRows - 1, -1, -1):
    print(stackLines[i])
    # loop through numbers of columns
    # and read four characters at a time
    for j in range(0, numOfColumns):
        # read four characters at a time
        # and append to the stack
        item = stackLines[i][j * 4:(j + 1) * 4]
        # if item starts with a [
        # then add the second character
        # to the stack
        if item[0] == "[":
            stacks[j].append(item[1])

# print the stacks
print("Stacks: ")
for stack in stacks:
    print(stack)

# print("Stack lines: " + str(stackLines))
# print("Move lines: " + str(moveLines))

# loop through the move lines
for moveLine in moveLines:
    # split the move line into a list of words
    moveLineWords = moveLine.split(" ")
    # read the second word
    # which is a count of blocks to move
    countOfBlocksToMove = int(moveLineWords[1])
    # read the fourth word which is the source stack
    sourceStack = int(moveLineWords[3])
    # read the sixth word which is the destination stack
    destinationStack = int(moveLineWords[5])

    # print the count of blocks to move
    print("move " + str(countOfBlocksToMove) + " blocks from stack " +
          str(sourceStack) + " to stack " + str(destinationStack))

    new_stack = []
    # loop through the count of blocks to move
    for i in range(0, countOfBlocksToMove):
        # pop the top block from the source stack
        # and append it to a new stack
        new_stack.append(stacks[sourceStack - 1].pop())
    
    # loop through the new stack
    for i in range(0, countOfBlocksToMove):
        # pop the top block from the new stack
        # and append it to the destination stack
        stacks[destinationStack - 1].append(new_stack.pop())

    print("Stacks: ")
    for stack in stacks:
        print(stack)

# print the top block of each stack in a line without a newline
# character or space
print("Top blocks of each stack: ")
for stack in stacks:
    print(stack[-1], end="")

# Close input file
inputFile.close()
