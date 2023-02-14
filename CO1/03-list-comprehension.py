# Input a list of numbers
n = int(input("How many numbers? : "))
list1 = []

print("Enter numbers: ")
for i in range (n):
    num = int(input(""))
    list1.append(num)

# Positive list of numbers
print("Positive numbers: ", [num for num in list1 if num >= 0])

# Square of N numbers
print("Squares of the numbers: ", [num * num for num in list1])

# Input a word
word = list(input("Enter a word: "))

# List of vowels from given word
print("Vowels in the word: ", [ltr for ltr in word if ltr in 'AEIOUaeiou'])

# Print ordinals of letters in word
print("Ordinal values of letters: ", [ord(ltr) for ltr in word])


