import csv
import os

path = os.getcwd()

fields = ['Username','Fname','Lname']

users = [
        {'Username':'booker12','Fname':'Rachel','Lname':'Booker'},
        {'Username':'grey07','Fname':'Laura','Lname':'Grey'},
        {'Username':'jhonson81','Fname':'Craig','Lname':'Jhonson'}
        ];


with open('file.csv','w') as csvfile :
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(users)

csvfile.close()


if os.path.exists(path+"/file.csv"):
    file = open(path+"/file.csv")
    csvrdr = csv.reader(file)

    for row in csvrdr:
        print(row)
    file.close()

else : 
    print("File doesn't exist!")
