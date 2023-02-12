c_year = int(input("Enter current year: "))
f_year = int(input("Enter future year: "))

for i in range(c_year, f_year):
    if (i % 4 == 0):
        print(i)