import csv
fields=['username','age']
user=[{"username":"jithin","age":"22"},
{"username":"amal","age":"23"}]
a=open("cs.csv","w")
csvfile=csv.DictWriter(a,fieldnames=fields)
csvfile.writeheader()
csvfile.writerows(user)
a.close()
a=open("cs.csv","r")
csvv=csv.DictReader(a)
for i in csvv:
    print(i)
a.close()