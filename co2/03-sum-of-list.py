n = int(input("How many numbers: "))
list1 = []

print("Enter number(s):")
for i in range(n):
    num = int(input(""))
    list1.append(num)
    
print("The sum of numbers in list is: ", sum(list1))