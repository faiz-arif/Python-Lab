words = input("Enter a list of words, separated by spaces: ").split()

print(sorted(words, key=len)[-1])
