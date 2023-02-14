word = input("Enter a string: ")

if (word[-3:] == 'ing'):
    print(word+"ly")
else:
    print(word+"ing")