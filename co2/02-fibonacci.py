n = int(input("How many terms?: "))
count = 0
n1, n2 = 0, 1

print("Fibonacci sequence :")
while count < n:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1


