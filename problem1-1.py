# Read input file with elves carrying calories with each elves calories partitioned by empty lines

# Open input file
inputFile = open("input1.txt", "r")

# Read input file
inputFileLines = inputFile.readlines()

# Initialize variables
elves_carrying_calories = []
current_elves_carrying_calories = 0

# Loop through input file lines
for line in inputFileLines:
    # If line is empty
    if line == "\n":
        # Add current elves carrying calories to elves carrying calories
        elves_carrying_calories.append(current_elves_carrying_calories)
        # Reset current elves carrying calories
        current_elves_carrying_calories = 0
    # Else
    else:
        # Add current line to current elves carrying calories
        current_elves_carrying_calories += int(line)

# Add last elves carrying calories to elves carrying calories
elves_carrying_calories.append(current_elves_carrying_calories)

# Print elves carrying calories
print(elves_carrying_calories)

# Find elves carrying calories with maximum calories
maximum_elves_carrying_calories = max(elves_carrying_calories)

# Print elves carrying calories with maximum calories
print("Elves carrying calories with maximum calories: " + str(maximum_elves_carrying_calories))

# Close input file
inputFile.close()
