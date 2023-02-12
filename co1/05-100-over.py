num = int(input("Enter size of the list: "))
numbers = []

print("Enter numbers in the list:")
for i in range(num):
    n = int(input())
    numbers.append(n)

for i in range(num):
    if numbers[i] > 100:
        numbers[i] = "over"

print (numbers)


