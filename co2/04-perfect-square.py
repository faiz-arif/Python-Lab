from math import sqrt

start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

numlist = [n for n in range(start, end) if (int(sqrt(n)) * int(sqrt(n))) == n]

newlist = [n for n in numlist if all(int(a) % 2 == 0 for a in str(n))]

print(newlist)
        
            
            
