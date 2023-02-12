import os

path = os.getcwd()

if (os.path.exists(path+"/file1.txt") and os.path.exists(path+"/file2.txt")):

    file1 = open(path+"/file1.txt","r")
    file2 = open(path+"/file2.txt","w")
    
    count = 1  
    for line in file1:
        if(count %2 != 0):
            file2.write(line)
        count = count + 1
    file1.close()
    file2.close()
else:
    print("Files doesn't exist")



file2 = open(path+"/file2.txt","r")
for line in file2:
    print(line)

file2.close()
