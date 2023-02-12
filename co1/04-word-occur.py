word = input("Enter a line of text: ").split()

result = {i:word.count(i) for i in set(word)}

print(result)