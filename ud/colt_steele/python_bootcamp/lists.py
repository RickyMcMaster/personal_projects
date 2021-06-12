sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ""

for s in sounds:
    result += s

# print(result.upper())

# Create a list called instructors
instructors = []

# Add the following strings to the instructors list
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")

# Run the tests to make sure you've done this correctly!

instructors.pop(-1)
instructors.pop(0)
instructors.insert(0, "Done")
print(instructors)
