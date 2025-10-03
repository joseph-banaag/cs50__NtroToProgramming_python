import csv

with open("new_collected_csvDict.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["first_name"], row["last_name"])
        print(row)