# read lines of characters from a file
# and split them into two words by commas
# further split the words into two numbers
# separated by a dash
inputFile = open("input4.txt", "r")

# Read input file and clean up newlines
inputFileLines = inputFile.read().splitlines()

# count of complete inside the other ranges and overlap
countOverlap = 0

# Loop through each line
for line in inputFileLines:
    # Split line into two words by commas
    words = line.split(",")
    # Split each word into two numbers by dash and convert to int
    minA, maxA = map(int, words[0].split("-"))
    minB, maxB = map(int, words[1].split("-"))

    # find if one range is completely inside the other
    if (minA >= minB and maxA <= maxB) or (minB >= minA and maxB <= maxA):
        # print(minA >= minB and maxA <= maxB)
        # print("--------------------")
        # print(minB >= minA and maxB <= maxA)
        # print("One range is completely inside the other")
        countOverlap += 1
    # find if the ranges overlap
    elif (minA <= minB and maxA >= minB) or (minB <= minA and maxB >= minA):
        print("Ranges overlap")
        countOverlap += 1
    # find if the ranges do not overlap
    else:
        print("Ranges do not overlap")

print("Count of complete inside the other ranges: " + str(countOverlap))

# Close input file
inputFile.close()
