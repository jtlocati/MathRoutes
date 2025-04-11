# TI-84 Plus CE Compatible Python Code

print("Problem number")
ProbNum = input("> ")  # Prompt user

print("What is problem " + ProbNum)
Poblem = input("> ")  # Prompt user

try:
    with open("REC.txt", "a") as writer:
        writer.write(ProbNum + "," + Poblem + "\n")
        print("Entry saved successfully")
except OSError as e:  # TI-Python uses OSError for file issues
    print("Error writing file:", e)
