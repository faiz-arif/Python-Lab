num =  int(input("Enter size of the list: "));
numbers = []

print("Enter numbers: ")
for i in range(num):
    n = int(input())
    numbers.append(n)
    
print("The entered list is:", numbers)
    
for i in numbers:
    if (i % 2 == 0):
        numbers.remove(i)
        
print("The entered list with even numbers removed:", numbers)

