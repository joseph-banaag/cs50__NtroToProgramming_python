import csv

data = [
    ['Alice', 30, 'New York'],
    ['Bob', 24, 'London'],
    ['Charlie', 35, 'Paris']
]

header = ['Name', 'Age', 'City']

with open('collection_csvHeader.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)  # Write the header row
    writer.writerows(data)   # Write the data rows