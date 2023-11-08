import random

# Generate a random three-digit number
answer = random.randint(100, 999)

# Extract digits from the answer
a = answer // 100
b = (answer // 10) % 10
c = answer % 10

# Create a list of digits from the answer
l1 = [a, b, c]

# Take input from the user
n = int(input("Enter a three-digit number: "))

# Extract digits from the user input
x = n // 100
y = (n // 10) % 10
z = n % 10

# Create a list of digits from the user input
l2 = [x, y, z]

# Initialize a flag to track if the number is correct
correct = True

# Compare the digits and provide feedback
for i in range(3):
    if l2[i] == l1[i]:
        print("Fermi")
    elif l2[i] in l1:
        print("Pico")
    else:
        correct = False

# Print the final result
if correct:
    print("Fermi Fermi Fermi !!!")
else:
    print("Try again!")

