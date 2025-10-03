import csv

with open("new_collected_names.csv", newline="") as csvfile:
    spam_reader = csv.reader(csvfile,
                             delimiter=" ",
                             quotechar="|")
    for row in spam_reader:
        print("FROM: csv.reader")
        print(",".join(row))

        data = ["apple", "banana", "cheery", "grapes", "pineapple"]
        print("\n".join(data))

    
