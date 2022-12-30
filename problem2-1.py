# Read file with two characters per line. 
# For opponent A as rocks, B as paper, C as scissors 
# For me X as rocks, Y as paper, Z as scissors

# Open input file
inputFile = open("input2.txt", "r")

# Read input file
inputFileLines = inputFile.readlines()

# Initialize variables
opponent = ""
me = ""
total_score = 0
round_score = 0

# If me wins add 6 to round score
# If me loses add 0 to round score
# If me ties add 3 to round score

# If me is rocks add 1 to round score
# If me is paper add 2 to round score
# If me is scissors add 3 to round score

# Loop through input file lines
for line in inputFileLines:
    # parse line with opponent and me by space.
    # clean up line by removing new line character
    opponent, me = line.strip().split(" ")

    # # print opponent and me
    # print("Opponent: " + opponent + " Me: " + me)

    # If me is rocks add 1 to score
    if me == "X":
        round_score += 1
    # If me is paper add 2 to score
    elif me == "Y":
        round_score += 2
    # If me is scissors add 3 to score
    elif me == "Z":
        round_score += 3

    # # Print round score
    # print("Round score: " + str(round_score))

    # If opponent is rocks
    if opponent == "A":
        # If me is rocks
        if me == "X":
            round_score += 3
        # If me is paper
        elif me == "Y":
            round_score += 6
        # If me is scissors
        elif me == "Z":
            round_score += 0

    # If opponent is paper
    elif opponent == "B":
        # If me is rocks
        if me == "X":
            round_score += 0
        # If me is paper
        elif me == "Y":
            round_score += 3
        # If me is scissors
        elif me == "Z":
            round_score += 6

    # If opponent is scissors
    elif opponent == "C":
        # If me is rocks
        if me == "X":
            round_score += 6
        # If me is paper
        elif me == "Y":
            round_score += 0
        # If me is scissors
        elif me == "Z":
            round_score += 3

    # # Print round score
    # print("Round score: " + str(round_score))

    # Add round score to total score
    total_score += round_score

    # Reset round score
    round_score = 0

# Print total score
print("Total score: " + str(total_score))

# Close input file
inputFile.close()
