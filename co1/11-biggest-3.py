a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print ("The entered numbers are: ", a, b, c)

if (a > b) and (a > c):
    big = a
elif (b > a) and (b > c):
    big = b
elif (c > a) and (c > b):
    big = c
else:
    big = "Invalid input"

print ("The largest number is", big)

