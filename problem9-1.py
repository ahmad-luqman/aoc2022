# read the file
inputFile = open("input9.txt", "r")

# read the lines of the file and clean up with end of line characters
inputFileLines = [line.strip() for line in inputFile.readlines()]

# define a list of directions and its corresponding
# x and y offsets
directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0)
}

# initialize the head and tail x and y coordinates
hx, hy = 0, 0
tx, ty = 0, 0

# initialize the min and max x and y coordinates
min_x, min_y = 0, 0
max_x, max_y = 0, 0

# initialize the set of visited coordinates
tail_visited = set()
tail_visited.add((tx, ty))

# function to extend the min and max x and y coordinates


def extendMinMax(x, y):
    global min_x, min_y, max_x, max_y
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y


# function to print the current position
# in a grid format with the current position marked with an X
# and the min and max x and y coordinates marked with a +
# and the rest of the grid marked with a .

def printGrid(x, y):
    global min_x, min_y, max_x, max_y
    # loop through the rows
    for i in range(max_x + 1, min_x, -1):
        # loop through the columns
        for j in range(min_y, max_y + 1):
            # if the current row and column is the current position
            if i == x and j == y:
                # print an X
                print("X", end="")
            # if the current row and column is the min
            # and max x and y coordinates
            elif i == min_x or i == max_x or j == min_y or j == max_y:
                # print a +
                print(".", end="")
            # otherwise
            else:
                # print a .
                print(".", end="")
        # print a new line
        print()


# function to check if the head is touching the tail


def touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


# loop through the lines of the file
for line in inputFileLines:
    # split the line into direction and distance
    direction = line[0]
    distance = int(line[1:])
    # print the direction and distance of the line
    # on a single line
    # print("direction: " + direction + ", distance: " + str(distance))

    # get the x and y offsets of the direction
    xOffset, yOffset = directions[direction]
    # print the x and y offsets of the direction
    # multiplied by the distance
    # print("x offset: " + str(xOffset * distance) +
    #       ", y offset: " + str(yOffset * distance))

    # add the x and y offsets of the direction
    # in a loop for the distance
    for i in range(distance):
        # add the x and y offsets of the direction
        # to the x and y coordinates of the head
        hx += xOffset
        hy += yOffset

        # trailing tail to follow the head
        # if the head is not touching the tail
        if not touching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += sign_x
            ty += sign_y

            # if the tail is not in the set of visited coordinates
            if (tx, ty) not in tail_visited:
                # add the tail to the set of visited coordinates
                tail_visited.add((tx, ty))

        # print the x and y coordinates
        # print("x: " + str(hx) + ", y: " + str(hy))
        extendMinMax(hx, hy)
        # printGrid(hx, hy)
        # print a new line
        # print()

# print the lines of the file
print(inputFileLines)

# print the visited coordinates of the tail count
print("visited coordinates of the tail count: " + str(len(tail_visited)))

# close the file
inputFile.close()
