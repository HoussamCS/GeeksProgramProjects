print("Challenge 1: Multiples of a Number")

# Ask user for input
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Generate multiples
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print("Output:", multiples)

