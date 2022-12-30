# Read file with two characters per line. 
# For opponent A as rocks, B as paper, C as scissors 
# For X as loss, Y as tie, Z as win

# Open input file
inputFile = open("input2.txt", "r")

# Read input file
inputFileLines = inputFile.readlines()

# Initialize variables
opponent = ""
result = ""
total_score = 0


# If me wins add 6 to round score
# If me loses add 0 to round score
# If me ties add 3 to round score

# If me is rocks and A add 1 to round score
# If me is paper and B add 2 to round score
# If me is scissors and C add 3 to round score

# Loop through input file lines
for line in inputFileLines:
    # parse line with opponent and result by space.
    # clean up line by removing new line character
    opponent, result = line.strip().split(" ")

    # Print opponent and result
    print("Opponent: " + opponent + " Result: " + result)

    round_score = 0

    if result == "X":
        round_score = 0
    elif result == "Y":
        round_score = 3
    elif result == "Z":
        round_score = 6

    # If opponent is A and a rock
    if opponent == "A":
        # If result is X and a loss
        if result == "X":
            # Me is scissors
            round_score += 3
        # If result is Y and a tie
        elif result == "Y":
            # Me is rocks
            round_score += 1
        # If result is Z and a win
        elif result == "Z":
            # Me is paper
            round_score += 2
    # If opponent is B and a paper
    elif opponent == "B":
        # If result is X and a loss
        if result == "X":
            # Me is rocks
            round_score += 1
        # If result is Y and a tie
        elif result == "Y":
            # Me is paper
            round_score += 2
        # If result is Z and a win
        elif result == "Z":
            # Me is scissors
            round_score += 3
    # If opponent is C and a scissors
    elif opponent == "C":
        # If result is X and a loss
        if result == "X":
            # Me is paper
            round_score += 2
        # If result is Y and a tie
        elif result == "Y":
            # Me is scissors
            round_score += 3
        # If result is Z and a win
        elif result == "Z":
            # Me is rocks
            round_score += 1

    # Print round score
    print("Round score: " + str(round_score))
    # Add round score to total score
    total_score += round_score

# Print total score
print("Total score: " + str(total_score))

# Close input file
inputFile.close()
