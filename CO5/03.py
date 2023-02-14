import csv
f = open("3.csv", "r")
csvfile = csv.reader(f)
for i in csvfile:
    print(i)
f.close()
