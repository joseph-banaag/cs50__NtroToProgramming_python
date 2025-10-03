import csv

data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 24, 'City': 'London'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Paris'}
]

fieldnames = ['Name', 'Age', 'City'] # Define the order of columns in the header

with open('collection_csvDictHeader.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row based on fieldnames
    writer.writerows(data) # Write the data rows