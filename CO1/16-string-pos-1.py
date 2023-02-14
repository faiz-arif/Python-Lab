str1 = input("Enter a string: ")
str2 = input("Enter another string: ")

newstr = str2[0] + str1[1:] + " " + str1[0] + str2[1:]
print(newstr)
