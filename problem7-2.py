# read a file and each line is either a command
# or a file and its size or a directory
# if it starts with a $ character, it is a command
# if it starts with a number, it is a file
# if it starts with a dir string, it is a directory

# read the file
inputFile = open("input7.txt", "r")

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

# print the size of the root directory
print(findSize(root))

# The total disk space available to the filesystem is 70000000
diskSpaceAvailable = 70000000

# The total disk space used by the filesystem
diskSpaceUsed = findSize(root)

# print available, used and free disk space
print("Available disk space: " + str(diskSpaceAvailable))
print("Used disk space: " + str(diskSpaceUsed))
print("Free disk space: " + str(diskSpaceAvailable - diskSpaceUsed))

# Make the free disk space of at least 30000000
# Find the smallest directory recursively, that, if deleted,
# would free up enough space on the filesystem
# to meet the requirement


# function to return list of all directories and subdirectories
# names and their sizes sorted by size


def findSortedListOfDirectories(directory):
    # initialize the list of directories
    listOfDirectories = []
    # add the root directory to the list of directories
    if directory["name"] == "root":
        listOfDirectories.append((directory["name"], findSize(directory)))
    # loop through the files and directories
    for child in directory["children"]:
        # if the child is a directory
        if child["type"] == "directory":
            # add the directory to the list of directories
            listOfDirectories.append(
                (child["name"], findSize(child)))
            # add the list of directories of the directory
            # to the list of directories
            listOfDirectories += findSortedListOfDirectories(child)
    # return the list of directories sorted by size
    return sorted(listOfDirectories, key=lambda x: x[1], reverse=True)


list_of_directories = findSortedListOfDirectories(root)
# print the list of directories sorted by size
print(list_of_directories)

# find the smallest directory of free space at least 30000000
previous_directory = None
for directory in list_of_directories:
    if directory[1] <= 30000000 - (diskSpaceAvailable - diskSpaceUsed):
        print("The smallest directory of size at least 30000000 is: " +
              previous_directory[0] + " with size: " +
              str(previous_directory[1]))
        break
    else:
        previous_directory = directory

# close the file
inputFile.close()
