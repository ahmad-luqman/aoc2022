# read the file
inputFile = open("input8.txt", "r")

# read the lines of the file and clean up with end of line characters
inputFileLines = [line.strip() for line in inputFile.readlines()]

# create a 2d array of single digit numbers

# initialize the 2d array
grid = []

# loop through the lines of the file
for line in inputFileLines:
    # split the line into a list of single digit numbers
    singleDigitNumbers = [int(singleDigitNumber) for singleDigitNumber in line]
    # add the list of single digit numbers to the 2d array
    grid.append(singleDigitNumbers)

# output the 2d array in a grid format
for row in grid:
    print(row)

# number of rows
numberOfRows = len(grid)
# number of columns
numberOfColumns = len(grid[0])

# print the number of rows and columns
print("number of rows: " + str(numberOfRows))
print("number of columns: " + str(numberOfColumns))

# count the number of outside entries on all sides
numberOfVisibleEntriesOnSide = 0

# loop through the rows
for rowIndex in range(numberOfRows):
    # loop through the columns
    for columnIndex in range(numberOfColumns):
        # if the row index is 0 or the number of rows - 1
        # or the column index is 0 or the number of columns - 1
        # then it is an outside entry
        if rowIndex == 0 or rowIndex == numberOfRows - 1 or \
           columnIndex == 0 or columnIndex == numberOfColumns - 1:
            # add 1 to the number of visible entries on the side
            numberOfVisibleEntriesOnSide += 1


# print the number of visible entries on the side and bottom
print("number of visible entries on the side: " +
      str(numberOfVisibleEntriesOnSide))

# return a array of entries above the entry from a 2d array


def getEntriesAbove(grid, rowIndex, columnIndex):
    # initialize a list of entries above
    entriesAbove = []
    # loop through the rows above the entry
    for row in grid[:rowIndex]:
        # get the entry
        entry = row[columnIndex]
        # add the entry to the list of entries above
        entriesAbove.append(entry)
    # return the list of entries above
    return entriesAbove

# return a array of entries below the entry from a 2d array


def getEntriesBelow(grid, rowIndex, columnIndex):
    # initialize a list of entries below
    entriesBelow = []
    # loop through the rows below the entry
    for row in grid[rowIndex + 1:]:
        # get the entry
        entry = row[columnIndex]
        # add the entry to the list of entries below
        entriesBelow.append(entry)
    # return the list of entries below
    return entriesBelow

# return a array of entries to the left of the entry from a 2d array


def getEntriesToLeft(grid, rowIndex, columnIndex):
    # initialize a list of entries to the left
    entriesToLeft = []
    # loop through all columns to the left of the entry
    for column in range(columnIndex):
        # get the entry
        entry = grid[rowIndex][column]
        # add the entry to the list of entries to the left
        entriesToLeft.append(entry)
    # return the list of entries to the left
    return entriesToLeft

# return a array of entries to the right of the entry from a 2d array


def getEntriesToRight(grid, rowIndex, columnIndex):
    # initialize a list of entries to the right
    entriesToRight = []
    # loop through all columns to the right of the entry
    for column in range(columnIndex + 1, numberOfColumns):
        # get the entry
        entry = grid[rowIndex][column]
        # add the entry to the list of entries to the right
        entriesToRight.append(entry)
    # return the list of entries to the right
    return entriesToRight

# return count the number of entries till the entry
# that is greater than the current entry in the
# list of entries


def countGreaterThanCurrentEntry(entries, currentEntry):
    # count the number of entries till the entry
    # that is greater than the current entry in the
    # list of entries
    # if its the last entry add 1 to the count
    countGreaterThanCurrentEntry = 0
    # loop through the entries
    for idx, entry in enumerate(entries):
        if currentEntry > entry:
            # increment the number of entries till the entry
            # that is greater than the current entry in the
            # list of entries
            countGreaterThanCurrentEntry += 1
        # else
        else:
            countGreaterThanCurrentEntry += 1
            # break out of the loop
            break
    # return the count
    return countGreaterThanCurrentEntry


# highest scenic value score
highestScenicValueScore = 0

# loop through the rows
for rowIndex in range(numberOfRows):
    # loop through the columns
    for columnIndex in range(numberOfColumns):
        # if the row index is 0 or the number of rows - 1
        # or the column index is 0 or the number of columns - 1
        # then it is an outside entry
        if rowIndex == 0 or rowIndex == numberOfRows - 1 or \
           columnIndex == 0 or columnIndex == numberOfColumns - 1:
            # skip this entry
            continue
        # get the entry
        entry = grid[rowIndex][columnIndex]
        # get all the entries above the entry
        entriesAbove = getEntriesAbove(grid, rowIndex, columnIndex)
        entriesAbove.reverse()
        # get all the entries below
        entriesBelow = getEntriesBelow(grid, rowIndex, columnIndex)
        # get all the entries to the left
        entriesToLeft = getEntriesToLeft(grid, rowIndex, columnIndex)
        entriesToLeft.reverse()
        # get all the entries to the right
        entriesToRight = getEntriesToRight(grid, rowIndex, columnIndex)

        # count the number of entries till the entry
        # that is greater than the current entry in the
        # list of entries above
        countGreaterThanCurrentEntryAbove = \
            countGreaterThanCurrentEntry(entriesAbove, entry)

        # count the number of entries till the entry
        # that is greater than the current entry in the
        # list of entries below
        countGreaterThanCurrentEntryBelow = \
            countGreaterThanCurrentEntry(entriesBelow, entry)

        # count the number of entries till the entry
        # that is greater than the current entry in the
        # list of entries to the left
        countGreaterThanCurrentEntryLeft = \
            countGreaterThanCurrentEntry(entriesToLeft, entry)

        # count the number of entries till the entry
        # that is greater than the current entry in the
        # list of entries to the right
        countGreaterThanCurrentEntryRight = \
            countGreaterThanCurrentEntry(entriesToRight, entry)

        # compute scenic value of the entry
        scenicValueOfEntry = countGreaterThanCurrentEntryAbove * \
            countGreaterThanCurrentEntryBelow * \
            countGreaterThanCurrentEntryLeft * \
            countGreaterThanCurrentEntryRight

        # print scenic value of the entry with the row and column index
        print("scenic value of entry at row " + str(rowIndex) +
              " and column " + str(columnIndex) + " is " +
              str(scenicValueOfEntry) + " with " +
              str(countGreaterThanCurrentEntryAbove) + " above, " +
              str(countGreaterThanCurrentEntryLeft) + " left, " +
              str(countGreaterThanCurrentEntryRight) + "  right, " +
              str(countGreaterThanCurrentEntryBelow) + " below")

        # if the scenic value of the entry is greater than the
        # highest scenic value score
        if scenicValueOfEntry > highestScenicValueScore:
            # update the highest scenic value score
            highestScenicValueScore = scenicValueOfEntry

# print the highest scenic value score
print("highest scenic value score: " + str(highestScenicValueScore))

# close the file
inputFile.close()
