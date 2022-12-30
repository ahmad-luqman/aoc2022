# read a file and each line is either a command
# or a file and its size or a directory
# if it starts with a $ character, it is a command
# if it starts with a number, it is a file
# if it starts with a dir string, it is a directory

# read the file
inputFile = open("input7-debug.txt", "r")

# read the lines of the file and clean up with end of line characters
inputFileLines = [line.strip() for line in inputFile.readlines()]

# initialize a tree structure
# the root is the root directory
# the root directory has a list of files and directories
# each file has a name and a size
# each directory has a name and a list of files and directories
# the tree structure is a dictionary
# the key is the name of the file or directory
# the value is a list of files and directories
# the first element of the list is the size of the file
# the first element of the list is the name of the directory
# the second element of the list is a list of files and directories
# the third element of the list is the parent directory

# the root directory
root = {
    "name": "root",
    "children": [],
    "childDirectories": {},
    "parent": None,
    "type": "directory"
    }
# the current directory
currentDirectory = root

#
# function to create a directory
# the directory is a dictionary
# the key is the name of the directory
# the value is a list of files and directories
# the first element of the list is the name of the directory
# the second element of the list is a list of files and directories
# the third element of the list is the parent directory
#


def createDirectory(directoryName, parentDirectory, parentDirectoryName):
    # create the directory
    directory = {
        "name": directoryName,
        "children": [],
        "childDirectories": {},
        "type": "directory",
        "parent": parentDirectory
        }
    # add the directory to the parent directory
    parentDirectory["children"].append(directory)
    # add the directory to the parent directory's list of child directories
    parentDirectory["childDirectories"][directoryName] = directory
    # return the directory
    return directory

#
# function to create a file
# the file is a dictionary
# the key is the name of the file
# the value is the size of the file
#


def createFile(fileName, fileSize, parentDirectory):
    # create the file
    file = {"fileName": fileName, "fileSize": fileSize, "type": "file"}
    # add the file to the parent directory
    parentDirectory["children"].append(file)

#
# function to print the current directory
#


def printCurrentDirectory():
    # print the current directory
    print(currentDirectory["name"])


#
# function to print the full directory structure
# replace the root directory with a /
# prepend each line with spaces
# to indicate the level of the directory
# and also with a dash
# append a (dir) after the directory name
# append a (file, size={fileSize}) after the file name
#

def printFullDirectoryStructure(directory, level):
    # print the name of the directory
    if level == 0:
        print("- / (dir)")
    else:
        print("  " * level + "- " + directory["name"] + " (dir)")
    # loop through the files and directories
    for child in directory["children"]:
        # if the child is a file
        if child["type"] == "file":
            # print the name of the file
            print("  " * (level + 1) + "- " + child["fileName"] +
                  " (file, size=" + str(child["fileSize"]) + ")")
        # if the child is a directory
        elif child["type"] == "directory":
            # print the full directory structure of the directory
            printFullDirectoryStructure(child, level + 1)


#
# function to find size of a directory
#
def findSize(directory):
    # initialize the size
    size = 0
    # loop through the files and directories
    for child in directory["children"]:
        # if the child is a file
        if child["type"] == "file":
            # add the file size to the size
            size += child["fileSize"]
        # if the child is a directory
        elif child["type"] == "directory":
            # add the size of the directory to the size
            size += findSize(child)
    # return the size
    return size


# loop through the lines
for line in inputFileLines:
    # if the line starts with a $ character
    if line[0] == "$":
        # if the line is a cd command
        if line[2:4] == "cd":
            if line[5:] == "/":
                # if the line is a cd / command
                # go to the root directory
                currentDirectory = root
            # if the line is a cd .. command
            elif line[5:] == "..":
                # go to the parent directory
                currentDirectory = currentDirectory["parent"]
            # if the line is a cd command
            else:
                # go to the directory
                currentDirectory = \
                    currentDirectory["childDirectories"][line[5:]]

        # if the line is a ls command
        elif line[2:4] == "ls":
            continue
    # if the line starts with a number
    elif line[0].isdigit():
        # split the line into a filesize and a filename
        fileSize, fileName = line.split(" ")
        # create a file
        createFile(
            fileName,
            int(fileSize),
            currentDirectory)
    # if the line starts with a dir string
    elif line[0:3] == "dir":
        # create a directory
        createDirectory(
            line[4:],
            currentDirectory,
            currentDirectory["name"])

# print the full directory structure
printFullDirectoryStructure(root, 0)


# initialize the sum of the total sizes of the directories
sumOfTotalSizes = 0

# recursively find the size of all of the directories
# or subdirectories of the root directory and
# add the size to the sum of the total sizes of the directories
# if the size is at most 100000


def findSizeOfDirectories(directory):
    global sumOfTotalSizes
    # find the size of the directory
    size = findSize(directory)
    # if the size is at most 100000
    if size <= 100000:
        # add the size to the sum of the total sizes of the directories
        sumOfTotalSizes += size
    # loop through the children of the directory
    for child in directory["children"]:
        # if the child is a directory
        if child["type"] == "directory":
            # recursively find the size of all of the directories
            # or subdirectories of the directory and
            # add the size to the sum of the total sizes of the directories
            # if the size is at most 100000
            findSizeOfDirectories(child)


findSizeOfDirectories(root)


# print the sum of the total sizes of the directories
print(sumOfTotalSizes)

# close the file
inputFile.close()
