import os
import math

path = os.getcwd()

if (os.path.exists(path + '/NewFolder') == False):
    os.mkdir(path + '/NewFolder')
    print('\nFolder NewFolder created.')
else:
    print('\nNewFolder already exists.')

if (os.path.exists(path + '/NewFolder/newfile.txt')):
    print('NewFile.txt already exists\n')
    f = open(path + '/NewFolder/newFile.txt', 'w')
else:
    f = open(path + '/NewFolder/newFile.txt', 'x')
    print("File newfile.txt created\n")

c = math.sqrt(64)
f.write(str(c))
f.close()
