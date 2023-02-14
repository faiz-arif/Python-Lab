str1 = list(input("Enter a string: "))

print({i:str1.count(i) for i in set(str1)})
