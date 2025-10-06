import csv

# this will get the information from the user instead of hard coding the data.
data_user = [
    [input("What is your name? "),
     int(input("How old are you? ")),
     input("Where do you live? ")]
]

data = [
    ['Alice', 30, 'New York'],
    ['Bob', 24, 'London'],
    ['Charlie', 35, 'Paris']
]

header = ['Name', 'Age', 'City']
sample_text = ["apple", "banana", "cherry"]

with open('collection_csvHeader.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(sample_text)

    writer.writerow(header)  # Write the header row
    writer.writerows(data)   # Write the data rows
    writer.writerow(sample_text)