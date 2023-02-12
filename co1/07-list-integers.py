num1 = int(input("Enter size of list 1:"))
l1 = []
l2 = []

print("Enter numbers in list 1:")
for i in range(num1):
    n1 = int(input())
    l1.append(n1)
    
num2 = int(input("Enter size of list 2:"))

print("Enter numbers in list 2:")
for i in range(num2):
    n2 = int(input())
    l2.append(n2)
    
if(num1 == num2):
    print("The lists are of the same length.")
else:
    print("The lists are NOT of the same length.")
    
if (sum(l1) == sum(l2)):
   print("The sum of both lists are equal.")
else:
    print("The sum of both lists are NOT equal.")

comm = set(l1).intersection(l2)
if (comm == None):
    print("There are no common values in the lists")
else:
    print("The common values in the lists are:", comm)


    
    