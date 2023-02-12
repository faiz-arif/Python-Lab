import os
import csv

path = os.getcwd()

if os.path.exists(path+"/username.csv"):
    file = open(path+"/username.csv","r")
    csvreader = csv.reader(file)
    print(next(csvreader))
    
    for row in csvreader:
        print(row)

    file.close()
else:
    print("File doesn't exist!")

