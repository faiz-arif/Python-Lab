word = input("Enter a string: ")

if len(word) < 2:
    print (word)
else:
    print (word[-1] + word[1:-1] + word[0])

