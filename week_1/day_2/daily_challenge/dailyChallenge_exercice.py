print("Challenge 1: Multiples of a Number")

# Ask user for input
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Generate multiples
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print("Output:", multiples)


print("\nChallenge 2: Remove Consecutive Duplicate Letters")

# Ask user for a string
word = input("Enter a word: ")

# Remove consecutive duplicates
result = ""
for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        result += word[i]

print("Output:", result)
