# Daily challenge gold exercise 
print("Challenge Gold: Remove Consecutive Duplicates")

word = input("Enter a word: ")

# Remove consecutive duplicates
result = ""
for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        result += word[i]

print("Output:", result)
