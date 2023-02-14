import csv

# Sample dictionary
data = {'name': 'John Smith', 'age': 35, 'city': 'New York'}

# Writing dictionary to CSV file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)

# Reading CSV file
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
