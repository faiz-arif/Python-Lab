import os
import csv

path = os.getcwd()


if os.path.exists(path+"/username.csv"):
    with open(path+"/username.csv",newline='') as file:
        reader = csv.DictReader(file)
        col = input("Enter the col to display(Username,Identifier,First name ,Last name) : ")
        for row in reader:
            print(row[col])

else:
    print("File doesn't exist!")
