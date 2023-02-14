import csv
f = open("3.csv", "r")
csvfile = csv.DictReader(f)
col_name = input("Choose any option(Name/Age/Profession):\n")
for i in csvfile:
    print(i[col_name])
f.close()
